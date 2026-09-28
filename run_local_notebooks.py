"""Execute and save the project notebooks using the local project kernel."""
import sys
from pathlib import Path
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parent

def started(cell, cell_index, **kwargs):
    print(f'  Starting cell {cell_index}', flush=True)

def finished(cell, cell_index, **kwargs):
    print(f'  Completed cell {cell_index}', flush=True)

names = sys.argv[1:] or [
    '01_Ingestion_and_Parquet_Conversion.ipynb',
    '02_Feature_Engineering_and_ML_Prep.ipynb',
    '03_Graph_Analytics.ipynb',
]
for name in names:
    path = ROOT / 'notebooks' / name
    if path.resolve().parent != (ROOT / 'notebooks').resolve():
        raise ValueError('Notebook path must remain in the project notebooks folder')
    notebook = nbformat.read(path, as_version=4)
    client = NotebookClient(notebook, timeout=1200, kernel_name='bda-local',
                            resources={'metadata': {'path': str(ROOT)}},
                            on_cell_start=started, on_cell_executed=finished)
    print(f'RUNNING {name}', flush=True)
    try:
        client.execute()
    finally:
        nbformat.write(notebook, path)
        for c in notebook.cells:
            for o in c.get('outputs', []):
                if o.output_type == 'stream':
                    print(o.text, flush=True)
                elif o.output_type == 'error':
                    print(f'{o.ename}: {o.evalue}', flush=True)
    print(f'PASSED {name}', flush=True)
print('All requested notebooks executed and saved locally.', flush=True)
