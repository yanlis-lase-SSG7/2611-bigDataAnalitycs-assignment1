"""Read-only consistency demo for the pipeline's saved aggregate reports.

Uses only Python's standard library. Does not train a model, read private raw
records, modify reports, or claim that the full notebook pipeline ran live.
"""

import argparse
import csv
import json
import math
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_csv(folder, name):
    with (folder / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def read_json(folder, name):
    return json.loads((folder / name).read_text(encoding="utf-8-sig"))


def close(actual, expected, label):
    require(math.isclose(float(actual), expected, rel_tol=1e-9, abs_tol=1e-9),
            f"Inconsistent {label}")


def ingestion(folder):
    rows = read_csv(folder, "ingestion_summary_report.csv")
    require(len(rows) == 9 and len({r['Table Name'] for r in rows}) == 9,
            "Expected nine distinct ingestion tables")
    raw = parquet = 0.0
    for row in rows:
        require(row['Round Trip Validated'].lower() == 'true',
                f"Round-trip validation failed: {row['Table Name']}")
        require(int(row['Row Count']) > 0, "Empty ingestion table")
        source_size = float(row['CSV Size (MiB)'])
        target_size = float(row['Parquet Size (MiB)'])
        require(source_size > 0 and target_size > 0, "Invalid storage size")
        close(row['Storage Savings (%)'], 100 * (1 - target_size / source_size),
              'table storage savings')
        raw += source_size
        parquet += target_size
    print('\n[01] INGESTION / PARQUET')
    print(f'PASS: {len(rows)} distinct tables; saved round-trip checks all True')
    print(f'CSV {raw:.3f} MiB / Parquet {parquet:.3f} MiB')
    print(f'Total storage savings: {100 * (1 - parquet / raw):.2f}%')
    print('Storage reduction is not a query-speed benchmark.')


def model(folder):
    result = read_json(folder, 'model_evaluation_report.json')
    audit = read_json(folder, 'feature_preparation_audit.json')
    candidates = read_csv(folder, 'model_validation_comparison.csv')
    winner = max(candidates, key=lambda r: (float(r['validation_f1']),
                 float(r['validation_precision']), float(r['selected_threshold'])))
    require(winner['candidate'] == result['selected_candidate'],
            'Selected candidate differs from validation comparison')
    close(result['selected_threshold'], float(winner['selected_threshold']),
          'selected validation threshold')
    close(result['threshold'], float(result['selected_threshold']), 'test threshold')
    require(sum(result[key] for key in ('train_orders', 'validation_orders',
            'test_orders')) == result['eligible_orders'], 'Split sizes do not sum')
    require(result['eligible_orders'] + result['excluded_missing_predictors'] ==
            audit['feature_orders'], 'Feature/eligible populations disagree')
    require(result['delay_definition'] == audit['delay_definition'],
            'Delay definitions differ')
    counts = result['confusion_matrix']
    tn, fp, fn, tp = (counts[key] for key in ('tn', 'fp', 'fn', 'tp'))
    require(all(isinstance(n, int) and n >= 0 for n in (tn, fp, fn, tp)),
            'Invalid confusion counts')
    require(tn + fp + fn + tp == result['test_orders'], 'Test count differs')
    confusion_rows = read_csv(folder, 'model_confusion_matrix.csv')
    actual = {(int(r['is_delayed']), int(r['prediction'])): int(r['count'])
              for r in confusion_rows}
    require(len(confusion_rows) == 4 and actual ==
            {(0, 0): tn, (0, 1): fp, (1, 0): fn, (1, 1): tp},
            'CSV/JSON confusion matrices differ')
    require(tp + fp > 0 and tp + fn > 0, 'Cannot compute precision/recall')
    precision, recall = tp / (tp + fp), tp / (tp + fn)
    close(result['delay_precision'], precision, 'test precision')
    close(result['delay_recall'], recall, 'test recall')
    close(result['delay_f1'], 2 * tp / (2 * tp + fp + fn), 'test F1')
    close(result['accuracy'], (tn + tp) / result['test_orders'], 'test accuracy')
    close(result['positive_test_prevalence'], (tp + fn) / result['test_orders'],
          'test prevalence')
    default = result['default_threshold_test_metrics']
    dc = default['confusion_matrix']
    require(sum(dc.values()) == result['test_orders'] and
            dc['tp'] + dc['fn'] == tp + fn, 'Default threshold population differs')
    close(default['delay_recall'], dc['tp'] / (dc['tp'] + dc['fn']),
          'default threshold recall')
    print('\n[02] VALIDATION SELECTION / TEST METRICS')
    print(f"Selected: {winner['candidate']}; threshold {result['threshold']:.6f}")
    print(f"Validation F1: {float(winner['validation_f1']):.4f}")
    print(f"Test recall: {default['delay_recall']:.2%} at threshold 0.5 / {recall:.2%} at selected threshold")
    print(f'Test precision: {precision:.2%}; false positives: {fp:,}')
    print('PASS: selection, populations and recalculated test metrics agree')
    print('Limited precision: use as a review signal; temporal validation remains future work.')


def graph(folder):
    audit = read_json(folder, 'graph_preparation_audit.json')
    features = read_json(folder, 'feature_preparation_audit.json')
    routes = read_csv(folder, 'seller_customer_routes_report.csv')
    nodes = read_csv(folder, 'graph_network_metrics.csv')
    require(len(nodes) == audit['nodes'] and len({r['State'] for r in nodes}) ==
            audit['nodes'], 'Graph node count differs')
    require(len(routes) == audit['routes'] and len({(r['seller_state'],
            r['customer_state']) for r in routes}) == audit['routes'],
            'Graph route count differs')
    require(sum(int(r['transaction_volume']) for r in routes) ==
            audit['graph_orders'], 'Route volume does not sum to graph orders')
    require(sum(int(r['delayed_orders']) for r in routes) ==
            audit['delayed_orders'], 'Route delayed counts differ')
    require(audit['graph_orders'] == features['feature_orders'] and
            audit['delayed_orders'] == features['delayed_orders'] and
            audit['delay_definition'] == features['delay_definition'] and
            audit['primary_item_rule'] == features['primary_item_rule'],
            'Graph/feature populations or definitions differ')
    states = {r['State'] for r in nodes}
    for route in routes:
        volume, delayed = int(route['transaction_volume']), int(route['delayed_orders'])
        require(volume > 0 and 0 <= delayed <= volume, 'Invalid route counts')
        require(route['seller_state'] in states and route['customer_state'] in states,
                'Unknown route state')
        require(abs(float(route['route_delay_rate_pct']) - 100 * delayed / volume)
                <= 0.005000001, 'Rounded route delay rate differs')
    route = next(r for r in routes if r['seller_state'] == 'SP' and
                 r['customer_state'] == 'RJ')
    print('\n[03] STATE NETWORK / ROUTE PRIORITY')
    print(f"PASS: {audit['nodes']} nodes / {audit['routes']} routes; counts agree")
    print(f"National delay: {audit['delayed_orders']:,} / {audit['graph_orders']:,} = "
          f"{audit['delayed_orders'] / audit['graph_orders']:.2%}")
    print(f"SP to RJ: {int(route['transaction_volume']):,} orders; delay {route['route_delay_rate_pct']}%")
    print('State origin/destination graph: no observed transit or physical hub locations.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--section', choices=('all', 'ingestion', 'model', 'graph'),
                        default='all')
    parser.add_argument('--reports-dir', type=Path,
                        default=Path(__file__).resolve().parent / 'outputs_ml_graph')
    args = parser.parse_args()
    print('OLIST ASSIGNMENT I: LIVE CHECK OF SAVED REPORTS')
    print('Read-only. Full ingestion/training/graph pipeline is not rerun here.')
    try:
        for name, action in (('ingestion', ingestion), ('model', model), ('graph', graph)):
            if args.section in ('all', name):
                action(args.reports_dir)
    except (OSError, ValueError, KeyError, StopIteration, ZeroDivisionError) as error:
        parser.exit(1, f'\nFAIL: {error}\n')
    print('\nDemo checks completed successfully.')


if __name__ == '__main__':
    main()
