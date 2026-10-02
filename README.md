# Assignment I — Big Data Analytics: Olist

Prototipe persiapan data dan rancangan analitik untuk dataset historis Brazilian E-Commerce Public Dataset by Olist (2016–2018). Fokus Assignment I: masalah bisnis, stakeholder, ingestion/storage/framework, tata kelola, serta organisasi dan model data. ML dan graf merupakan eksplorasi awal; manfaat operasional belum diuji.

## Berkas utama

- Laporan kerja lokal `Big Data Analytics - Laporan 2702751284.docx`: Bab 1–4, cetak biru arsitektur, EDA terukur, batas implementasi, dan referensi. Berkas ini sengaja di-ignore dari Git sesuai instruksi pemilik proyek; deklarasi AI tetap milik mahasiswa.
- [Laporan PDF](Big%20Data%20Analytics%20-%20Laporan%202702751284.pdf): ekspor dari Word hasil revisi. Periksa kembali deklarasi dan batas 25 halaman sebelum pengumpulan; ekspor ulang jika Word diubah.
- [Notebook 01](notebooks/01_Ingestion_and_Parquet_Conversion.ipynb): ingestion sembilan CSV, validasi, konversi Parquet Snappy.
- [Notebook 02](notebooks/02_Feature_Engineering_and_ML_Prep.ipynb): fitur per order, split hash, perbandingan bobot kelas dan pemilihan ambang pada validation.
- [Notebook 03](notebooks/03_Graph_Analytics.ipynb): graf state asal–tujuan dan analisis rute dengan NetworkX.
- [Panduan notebook](notebooks/README.md), [catatan presentasi](docs/presentation-notes.md), dan [status pekerjaan](docs/current-task.md).
- [PPT Assignment I](presentations/Big%20Data%20Analytics%20-%20Laporan%202702751284.pptx): 11 slide 16:9 bergaya navy–teal dengan speaker notes percakapan, arsitektur lokal-versus-enterprise, empat grafik EDA, serta hasil ingestion, model dan graf yang telah dijalankan.
- [Panduan rekaman](docs/presentation-video.md) dan [naskah siap baca](docs/presentation-notes.md): seluruh presentasi di PowerPoint, target latihan 9 menit 30 detik tanpa perpindahan ke VS Code.
- `demo_assignment1.py`: pemeriksaan read-only atas konsistensi ringkasan hasil tersimpan; jalankan `python demo_assignment1.py`. Script ini tidak menjalankan ulang pipeline notebook dan tidak membutuhkan package tambahan.
- `outputs_ml_graph/`: ringkasan hasil CSV/JSON kecil dari eksekusi lokal. Dataset fitur, daftar order per split, dan seluruh tabel ambang tidak dipublikasikan.
- `eda_assignment1.py`: profil sembilan tabel Parquet tervalidasi, pembacaan orders bertipe dengan FAILFAST, empat orphan assertion, distribusi status, delay per state pelanggan, dan ringkasan state penjual. Skrip mengekspor agregat, bukan ID pelanggan/penjual.
- `make_eda_figures.py` dan `figures/`: diagram cetak biru serta empat grafik EDA 300 DPI yang membaca laporan agregat terukur. Angka state tidak diisi manual.

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

Prasyarat: Windows x64, Python 3.11 64-bit, internet untuk setup, dan sembilan CSV Olist. Java/Hadoop/Spark lokal disiapkan oleh `setup_runtime.py`; tidak perlu menyertakan `.runtime` atau `.venv` dalam ZIP untuk dosen. VS Code adalah editor; gunakan kernel lokal, bukan Colab.

```powershell
git clone https://github.com/yanlis-lase-SSG7/2611-bigDataAnalitycs-assignment1.git
Set-Location 2611-bigDataAnalitycs-assignment1
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe setup_runtime.py
.\.venv\Scripts\python.exe -m ipykernel install --user --name bda-local --display-name "BDA Local (Python 3.11)"
```

1. Unduh sembilan CSV dari [dataset Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) sesuai ketentuan sumber dan letakkan langsung pada `datasets_raw/`. Nama tabel: `olist_customers_dataset.csv`, `olist_geolocation_dataset.csv`, `olist_order_items_dataset.csv`, `olist_order_payments_dataset.csv`, `olist_order_reviews_dataset.csv`, `olist_orders_dataset.csv`, `olist_products_dataset.csv`, `olist_sellers_dataset.csv`, serta `product_category_name_translation.csv`.
2. Pastikan `setup_runtime.py` selesai dengan PASS. Script mengunduh Java dan helper Hadoop dengan SHA-256 tersemat, menyalin Spark dari package PySpark 4.0.4 dengan verifikasi RECORD, memperbaiki launcher untuk path dengan spasi, lalu menguji tulis/baca lima baris Parquet. Pengulangan setup memverifikasi runtime yang sudah ada. `setup_runtime.py --check` memeriksa tanpa unduhan. Detail sumber/checksum dan penanganan error ada pada [runtime prerequisites](docs/runtime-prerequisites.md).
3. Buka root repository di VS Code dan pilih `.venv\Scripts\python.exe` atau kernel BDA Local. Jalankan notebook **01 → 02 → 03**. Input, staging dan output tetap di checkout lokal. Jika kernel dimulai di folder lain, atur `$env:BDA_PROJECT_DIR = (Get-Location).Path` sebelum membuka kernel, atau set environment kernel ke root checkout.
4. Alternatif dari root: `.\.venv\Scripts\python.exe run_local_notebooks.py`. Perintah ini menjalankan ulang dan menyimpan output ketiga notebook, serta mengganti artefak hasil yang dihasilkan pipeline.

Untuk mengulang EDA dan gambar setelah notebook 01 selesai:

```powershell
.\.venv\Scripts\python.exe eda_assignment1.py
.\.venv\Scripts\python.exe make_eda_figures.py
```

Skrip EDA menjalankan Spark di satu mesin dan membaca Parquet keluaran notebook 01. Rancangan S3/HDFS, partisi berdasarkan waktu, katalog, dan Spark cluster dalam laporan adalah opsi enterprise yang belum diuji; tiga worker contoh adalah hipotesis sizing yang perlu benchmark.

Sumber notebook sudah menggunakan penemuan root/`BDA_PROJECT_DIR` untuk lintas perangkat. Output sel tersimpan berasal dari run Windows sebelumnya; perubahan path ini tidak mengubah logika perhitungan.

## Isi yang tetap lokal

Dataset raw/Parquet, `.venv`, `.runtime`, backup, ekspor besar, materi kuliah, file sementara, serta script migrasi/revisi sekali pakai diabaikan dari Git. Tidak menggunakan Git LFS. Folder tersebut dapat dipulihkan terpisah atau hasilnya dibuat ulang. Repository menyertakan notebook dengan output tersimpan dan ringkasan hasil untuk memudahkan pemeriksaan dosen.

Mahasiswa menyatakan video versi sebelumnya sudah tersedia di SharePoint. Karena PPT telah diperbarui, periksa apakah video yang akan dikumpulkan memakai slide final; rekam ulang bila perlu. Sebelum pengumpulan LMS, periksa akses tautan, durasi maksimal 10 menit dan deklarasi AI. Pengembangan berikutnya: validasi temporal dan analisis biaya intervensi sesuai tahap tugas berikutnya. Konteks lintas perangkat dipelihara melalui `AGENTS.md` dan `docs/current-task.md`.

## Workflow Codex lintas perangkat

Di kantor, berikan tugas biasa kepada Codex. Codex otomatis membaca AGENTS.md, status tugas, Git dan berkas terkait sebelum bekerja, lalu memperbarui dokumentasi yang menjadi tidak sesuai. Saat diminta commit atau commit dan push, Codex menyinkronkan dokumentasi dan melakukan validasi yang sesuai sebelum menyimpan perubahan. Permintaan commit saja tidak memicu push.

Di rumah, lakukan `git pull` / Get Latest, buka proyek di VS Code, lalu langsung berikan tugas berikutnya. Tidak perlu perintah khusus resume atau handoff. Source dan riwayat Git menjadi acuan utama; docs/current-task.md menyimpan keadaan pekerjaan saat ini, bukan catatan setiap sesi.

Aturan ini berlaku pada sesi Codex yang membaca repository; tidak memasang layanan otomatis atau Git hook. Perubahan baru harus di-commit dan di-push agar tersedia di laptop lain. Dataset, environment dan runtime tetap perlu dipulihkan terpisah sebagaimana panduan di atas.
