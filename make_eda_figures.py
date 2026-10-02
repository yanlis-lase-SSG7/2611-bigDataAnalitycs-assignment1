"""Render four report figures from measured aggregate EDA outputs, at 300 DPI."""

import csv
import json
import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib.ticker import FuncFormatter
import numpy as np

ROOT = Path(os.environ.get("BDA_PROJECT_DIR", Path(__file__).resolve().parent)).resolve()
SOURCE = ROOT / "outputs_ml_graph"
FIGURES = ROOT / "figures"

def records(name):
    with (SOURCE / name).open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def save(fig, name):
    fig.savefig(FIGURES / name, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main():
    FIGURES.mkdir(exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False})
    status = records("eda_order_status.csv")
    state = records("eda_state_delay.csv")
    quality = json.loads((SOURCE / "eda_quality_profile.json").read_text(encoding="utf-8"))
    national = quality["national"]
    if (int(national["orders"]), int(national["delayed"])) != (96470, 7826):
        raise ValueError("National figures differ from validated Olist baseline")

    # Architecture is a proposal; the blue bottom ribbon identifies what ran.
    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)
    ax.axis("off")
    boxes = [
        (0.2, 2.4, "Sumber batch\n9 CSV Olist"),
        (2.2, 2.4, "Ingestion Spark\nskema + FAILFAST"),
        (4.2, 2.4, "Data lake target\nS3/HDFS + Parquet"),
        (6.2, 2.4, "Cluster Spark\n3 worker awal*"),
        (8.2, 2.4, "Agregat / fitur\nlaporan"),
    ]
    for x, y, label in boxes:
        ax.add_patch(FancyBboxPatch((x, y), 1.6, 1.25,
                                   boxstyle="round,pad=0.08", facecolor="#e9f2f7",
                                   edgecolor="#276389", linewidth=1.5))
        ax.text(x + .8, y + .625, label, ha="center", va="center", fontsize=8)
    for x in (1.8, 3.8, 5.8, 7.8):
        ax.add_patch(FancyArrowPatch((x, 3.025), (x + .36, 3.025),
                                     arrowstyle="->", mutation_scale=16, color="#276389"))
    ax.text(5.0, 1.8, "Zona curated: Parquet Snappy; partisi waktu setelah uji volume/skew",
            ha="center", fontsize=10, color="#143e55")
    ax.add_patch(FancyBboxPatch((.25, .45), 9.5, .65, boxstyle="round,pad=0.04",
                                facecolor="#28668b", edgecolor="none"))
    ax.text(5, .78, "Yang diuji: CSV lokal → validasi → Parquet lokal → EDA; Spark local[4]",
            color="white", ha="center", va="center", fontsize=10)
    ax.text(5, .18, "*Cluster adalah hipotesis kapasitas; perlu benchmark dan evaluasi biaya sebelum dipilih.",
            ha="center", fontsize=8, color="#444444")
    save(fig, "fig0_enterprise_architecture.png")

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    names = [r["order_status"] for r in status][::-1]
    counts = [int(r["orders"]) for r in status][::-1]
    ax.barh(names, counts, color="#276389")
    ax.set_xscale("log")
    ax.set_xlim(1, max(counts) * 2.3)
    ax.set_xlabel("Jumlah order (skala logaritmik)")
    ax.set_title("Distribusi status seluruh order Olist (n = 99.441)", loc="left")
    for pos, count in enumerate(counts):
        ax.text(count * 1.09, pos, f"{count:,}".replace(",", "."), va="center")
    fig.tight_layout()
    save(fig, "fig1_order_status_distribution.png")

    delayed = int(national["delayed"])
    on_time = int(national["orders"]) - delayed
    fig, ax = plt.subplots(figsize=(6.4, 5.1))
    ax.pie([on_time, delayed], startangle=90, counterclock=False,
           colors=["#28668b", "#d15b41"],
           wedgeprops={"width": .35, "edgecolor": "white", "linewidth": 2})
    ax.text(0, .12, f"{national['delay_rate_pct']:.2f}%", ha="center", va="center",
            fontsize=24, weight="bold", color="#a43e2a")
    ax.text(0, -.18, "terlambat", ha="center", va="center", fontsize=11)
    ax.legend([f"Tepat waktu: {on_time:,} (91,89%)".replace(",", ".", 1),
               f"Terlambat: {delayed:,} (8,11%)".replace(",", ".", 1)],
              loc="lower center", bbox_to_anchor=(.5, -.1), frameon=False)
    ax.set_title("Keterlambatan order delivered berlabel (n = 96.470)")
    save(fig, "fig2_delivery_delay_ratio.png")

    top = sorted(state, key=lambda r: (-float(r["delay_rate_pct"]), r["customer_state"]))[:10]
    fig, ax = plt.subplots(figsize=(9, 5.1))
    bars = ax.bar([r["customer_state"] for r in top],
                  [float(r["delay_rate_pct"]) for r in top], color="#b7513d")
    ax.set_ylim(0, max(float(r["delay_rate_pct"]) for r in top) * 1.21)
    ax.set_ylabel("Delay rate (%), berdasarkan state pelanggan")
    ax.set_title("Sepuluh state dengan delay rate tertinggi", loc="left")
    for bar, row in zip(bars, top):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + .35,
                f"{bar.get_height():.2f}%\nn={int(row['orders']):,}".replace(",", "."),
                ha="center", fontsize=8)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.0f}%"))
    fig.tight_layout()
    save(fig, "fig3_top10_state_delay_rate.png")

    nulls = []
    for table, info in quality["tables"].items():
        for column, profile in info["fields"].items():
            if profile["null_count"]:
                nulls.append((table.removeprefix("olist_").removesuffix("_dataset"),
                              column, profile["null_pct"], profile["null_count"]))
    top_nulls = sorted(nulls, key=lambda row: (-row[2], row[0], row[1]))[:10]
    values = np.array([[r[2]] for r in top_nulls])
    fig, ax = plt.subplots(figsize=(8.2, 5.1))
    chart = ax.imshow(values, cmap="YlOrRd", aspect="auto", vmin=0, vmax=100)
    short_name = {
        "review_comment_title": "judul ulasan",
        "review_comment_message": "teks ulasan",
        "order_delivered_customer_date": "tanggal diterima",
        "order_delivered_carrier_date": "tanggal ke kurir",
        "order_approved_at": "tanggal disetujui",
        "product_category_name": "kategori produk",
        "product_description_lenght": "panjang deskripsi",
        "product_name_lenght": "panjang nama",
        "product_photos_qty": "jumlah foto",
    }
    ax.set_yticks(range(len(top_nulls)),
                  [f"{table}: {short_name.get(column, column)}" for table, column, _, _ in top_nulls],
                  fontsize=10)
    ax.set_xticks([0], ["Persentase null per field"])
    ax.set_title("Profil field dengan null terbanyak pada sembilan tabel", loc="left")
    for i, (_, _, pct, count) in enumerate(top_nulls):
        ax.text(0, i, f"{pct:.2f}%  ({count:,})".replace(",", "."),
                ha="center", va="center", color="white" if pct > 55 else "#17212b", fontsize=10)
    fig.colorbar(chart, ax=ax, label="Null (%)", fraction=.03, pad=.02)
    fig.tight_layout()
    save(fig, "fig4_null_profile_heatmap.png")
    print("PASS: four 300 DPI figures generated from measured EDA aggregates")


if __name__ == "__main__":
    main()
