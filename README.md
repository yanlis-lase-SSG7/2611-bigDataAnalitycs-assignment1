# Assignment I — Big Data Analytics: Olist

Prototipe persiapan data dan rancangan analitik untuk dataset historis Brazilian E-Commerce Public Dataset by Olist (2016–2018). Fokus Assignment I: masalah bisnis, stakeholder, ingestion/storage/framework, tata kelola, serta organisasi dan model data. ML dan graf merupakan eksplorasi awal; manfaat operasional belum diuji.

## Berkas utama

- [Laporan final](Laporan%20Big%20Data%20Analytics%20-%202702751284.docx): Bab 1–4, justifikasi teknologi, bukti data, batas implementasi, dan referensi. Deklarasi AI masih harus dilengkapi mahasiswa.
- [Notebook 01](notebooks/01_Ingestion_and_Parquet_Conversion.ipynb): ingestion sembilan CSV, validasi, konversi Parquet Snappy.
- [Notebook 02](notebooks/02_Feature_Engineering_and_ML_Prep.ipynb): fitur per order, split hash, perbandingan bobot kelas dan pemilihan ambang pada validation.
- [Notebook 03](notebooks/03_Graph_Analytics.ipynb): graf state asal–tujuan dan analisis rute dengan NetworkX.
- [Panduan notebook](notebooks/README.md), [catatan presentasi](docs/presentation-notes.md), dan [status pekerjaan](docs/current-task.md).
- [PPT Assignment I](presentations/Assignment_I_Olist_2702751284.pptx): 11 slide 16:9 dengan speaker notes natural, penjelasan proyek/tech stack, dan hasil demo yang telah dijalankan.
- [Panduan rekaman](docs/presentation-video.md) dan [naskah siap baca](docs/presentation-notes.md): seluruh presentasi di PowerPoint, target 9 menit 30 detik tanpa perpindahan ke VS Code.
- `demo_assignment1.py`: pemeriksaan read-only atas konsistensi ringkasan hasil tersimpan; jalankan `python demo_assignment1.py`. Script ini tidak menjalankan ulang pipeline notebook dan tidak membutuhkan package tambahan.
- `outputs_ml_graph/`: ringkasan hasil CSV/JSON kecil dari eksekusi lokal. Dataset fitur, daftar order per split, dan seluruh tabel ambang tidak dipublikasikan.

## Hasil tersimpan

| Ukuran | Hasil |
|---|---|
| CSV → Parquet, sembilan tabel | 120,341 → 54,236 MiB; hemat 54,93% |
| Order berlabel / terlambat | 96.470 / 7.826; delay 8,11% berdasarkan timestamp |
| Review rata-rata per order | Tepat waktu 4,2943; terlambat 2,5665, hanya order dengan review |
| ML eligible; train / validation / test | 96.455; 61.826 / 15.513 / 19.116 |
| Kandidat dan ambang | Random Forest tanpa bobot; 0,099536, dipilih pada validation |
| Test ROC-AUC / PR-AUC / F1 | 0,6610 / 0,1409 / 0,2194 |
| Test precision / recall | 14,47% / 45,41%; belum layak untuk tindakan otomatis |
| Graf | 27 node / 409 rute; SP → RJ: 8.158 order, delay 15,49% |

Review menunjukkan asosiasi, bukan kausalitas. Graf tidak merekam transit atau menentukan lokasi hub. Warehouse dimensional masih konseptual; NoSQL/graph database fisik serta dashboard belum dibangun. Spark berjalan dengan `local[4]` pada satu mesin; kapasitas cluster/produksi belum diuji.

## Menjalankan di Windows lokal

Prasyarat: Python 3.11, Java 17, dan runtime Windows Spark/Hadoop yang sesuai. VS Code adalah editor; gunakan kernel lokal, bukan Colab.

```powershell
git clone https://github.com/yanlis-lase-SSG7/2611-bigDataAnalitycs-assignment1.git
Set-Location 2611-bigDataAnalitycs-assignment1
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --user --name bda-local --display-name "BDA Local (Python 3.11)"
```

1. Unduh sembilan CSV dari [dataset Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) sesuai ketentuan sumber dan letakkan langsung pada `datasets_raw/`. Nama tabel: `olist_customers_dataset.csv`, `olist_geolocation_dataset.csv`, `olist_order_items_dataset.csv`, `olist_order_payments_dataset.csv`, `olist_order_reviews_dataset.csv`, `olist_orders_dataset.csv`, `olist_products_dataset.csv`, `olist_sellers_dataset.csv`, serta `product_category_name_translation.csv`.
2. Pulihkan runtime yang telah diuji dari mesin asal: `.runtime/jdk-*/` (Java 17), `.runtime/hadoop/bin/` (`winutils.exe`, `hadoop.dll`), dan `.runtime/spark-home/` (`bin`, `jars` untuk Spark 4.0.4). Cache/temp tidak perlu disalin. Git tidak menyertakan runtime ini; instalasi Python saja belum cukup. Launcher lokal telah diperbaiki untuk path dengan spasi. Detail sumber/checksum ada pada [runtime prerequisites](docs/runtime-prerequisites.md).
3. Buka root repository di VS Code dan pilih `.venv\Scripts\python.exe` atau kernel BDA Local. Jalankan notebook **01 → 02 → 03**. Input, staging dan output tetap di checkout lokal. Jika kernel dimulai di folder lain, atur `$env:BDA_PROJECT_DIR = (Get-Location).Path` sebelum membuka kernel, atau set environment kernel ke root checkout.
4. Alternatif dari root: `.\.venv\Scripts\python.exe run_local_notebooks.py`. Perintah ini menjalankan ulang dan menyimpan output ketiga notebook, serta mengganti artefak hasil yang dihasilkan pipeline.

Sumber notebook sudah menggunakan penemuan root/`BDA_PROJECT_DIR` untuk lintas perangkat. Output sel tersimpan berasal dari run Windows sebelumnya; perubahan path ini tidak mengubah logika perhitungan.

## Isi yang tetap lokal

Dataset raw/Parquet, `.venv`, `.runtime`, backup, ekspor besar, materi kuliah, file sementara, serta script migrasi/revisi sekali pakai diabaikan dari Git. Tidak menggunakan Git LFS. Folder tersebut dapat dipulihkan terpisah atau hasilnya dibuat ulang. Repository menyertakan notebook dengan output tersimpan dan ringkasan hasil untuk memudahkan pemeriksaan dosen.

Pengembangan berikutnya: slide/video maksimal 10 menit, deklarasi AI oleh mahasiswa, kemudian validasi temporal dan analisis biaya intervensi sesuai tahap tugas berikutnya. Konteks lintas perangkat dipelihara melalui `AGENTS.md` dan `docs/current-task.md`.

## Workflow Codex lintas perangkat

Di kantor, berikan tugas biasa kepada Codex. Codex otomatis membaca AGENTS.md, status tugas, Git dan berkas terkait sebelum bekerja, lalu memperbarui dokumentasi yang menjadi tidak sesuai. Saat diminta commit atau commit dan push, Codex menyinkronkan dokumentasi dan melakukan validasi yang sesuai sebelum menyimpan perubahan. Permintaan commit saja tidak memicu push.

Di rumah, lakukan `git pull` / Get Latest, buka proyek di VS Code, lalu langsung berikan tugas berikutnya. Tidak perlu perintah khusus resume atau handoff. Source dan riwayat Git menjadi acuan utama; docs/current-task.md menyimpan keadaan pekerjaan saat ini, bukan catatan setiap sesi.

Aturan ini berlaku pada sesi Codex yang membaca repository; tidak memasang layanan otomatis atau Git hook. Perubahan baru harus di-commit dan di-push agar tersedia di laptop lain. Dataset, environment dan runtime tetap perlu dipulihkan terpisah sebagaimana panduan di atas.
