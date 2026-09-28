# Notebook BDA dengan kernel lokal Windows

Seluruh data dibaca dan ditulis pada folder proyek lokal. Pada mesin asal: D:\Private Project\bda\BDA_Olist_Project. Pada komputer lain, buka root repository atau notebooks/; gunakan BDA_PROJECT_DIR bila kernel mulai di folder lain. Ketiga notebook tidak menggunakan Colab atau Google Drive.

## Menjalankan melalui VS Code

1. Tutup dan buka ulang notebook agar source dari disk termuat.
2. Klik Select Kernel, Select Another Kernel, lalu Python Environments.
3. Pilih interpreter proyek .venv\Scripts\python.exe, atau BDA Local (Python 3.11) bila muncul.
4. Jalankan Run All pada 01, kemudian 02, lalu 03.

Sel pertama harus mencetak BDA LOCAL WINDOWS, interpreter .venv proyek, dan folder hasil pada drive D. Kernel Colab akan ditolak dengan pesan yang jelas.

Alternatif: jalankan run_local_notebooks.py menggunakan .venv\Scripts\python.exe. Script mengeksekusi dan menyimpan ketiga notebook secara berurutan.

## Environment proyek

Python lokal menggunakan PySpark 4.0.4. Microsoft OpenJDK 17, Hadoop Windows native helpers, dan Spark berada dalam .runtime. Sumber dan checksum native helpers dicatat pada .runtime/hadoop/sources.json. Launcher Spark diperbaiki agar path dengan spasi dapat digunakan. Staging, file sementara, dan warehouse juga berada dalam proyek. Environment diterapkan pada proses kernel tanpa perubahan PATH sistem. Spark memakai empat thread lokal; ini prototipe satu mesin.

## Aturan data

Header CSV dibaca dengan utf-8-sig untuk menghapus BOM. Reviews dibaca sebagai logical records multiline. ID, tipe, key, jumlah record, null, dan round-trip Parquet diperiksa. Raw CSV tidak diubah.

Primary seller/product berasal dari order_item_id terkecil. Delapan delivered orders tanpa tanggal actual dikeluarkan dari data berlabel. Delay default berdasarkan timestamp; opsi calendar_date harus sama pada notebook 02 dan 03. Imputasi bobot tetap konstanta 500 gram, bukan median kategori.

Metrik strength graph menghitung order. Betweenness memakai jalur topologis tanpa bobot volume dan tidak membuktikan transit paket yang diamati. Model memakai split berbasis hash order_id dan belum menguji generalisasi ke periode masa depan.

## Penanganan kelas tidak seimbang

Notebook 02 membagi development/test melalui hash order_id (xxhash64 dengan salt 42), kemudian membagi development menjadi train/validation melalui hash dengan salt 43, sehingga proporsi keseluruhan sekitar 64/16/20. Hash membuat pembagian tetap meskipun Spark mengubah partisi. model_data_split_manifest.csv menyimpan anggota setiap partisi. Anggota test run lama tidak tersimpan, sehingga angka historis bukan perbandingan berpasangan. Pembanding unweighted dengan ambang 0,5 dievaluasi pada test yang sama setelah pemilihan kandidat dibekukan. Jumlah baris dan tidak adanya order yang tumpang tindih diperiksa. Bobot kelas seimbang dihitung hanya dari label train. Dua kandidat, unweighted dan balanced_class_weights, dibandingkan berdasarkan F1 validation. Ambang dipilih dari seluruh skor validation yang berbeda; skor yang sama diperlakukan bersama. Jika F1 sama, precision lebih tinggi diprioritaskan, kemudian ambang lebih tinggi. Data test tidak digunakan untuk pemilihan kandidat atau ambang.

model_validation_comparison.csv mencatat perbandingan kandidat; model_validation_thresholds.csv mencatat kurva pemilihan ambang. model_evaluation_report.json dan model_confusion_matrix.csv memakai kandidat serta ambang terpilih, dengan metrik ambang 0,5 pada model yang sama sebagai pembanding. F1 adalah tujuan sementara tanpa biaya bisnis yang ditetapkan. Skor model belum dikalibrasi sebagai probabilitas. Backup hasil lama telah dihapus saat pembersihan proyek; gunakan hasil terbaru.

## Output

Notebook 01 menghasilkan sembilan tabel datasets_parquet, ingestion_summary_report.csv, dan ingestion_null_profile.json.
Notebook 02 menghasilkan feature dataset, audit persiapan, laporan state, feature importance, confusion matrix, dan evaluasi ROC-AUC/PR-AUC/precision/recall/F1 serta baseline.
Notebook 03 menghasilkan laporan rute, metrik node, dan audit konsistensi dengan notebook 02.

Semua laporan berada pada outputs_ml_graph. Output sel disimpan pada notebook setelah eksekusi. Gunakan angka terbaru untuk memperbarui laporan. Backup notebook lama telah dihapus saat pembersihan proyek; versi yang dipublikasikan selanjutnya dilacak melalui Git.

## Repository lintas perangkat

Lihat ../README.md untuk dependensi, dataset dan runtime Windows yang tidak disertakan di Git. Source konfigurasi kini menemukan root proyek atau menggunakan BDA_PROJECT_DIR. Output tersimpan berasal dari run lokal sebelumnya; perubahan konfigurasi path tidak mengubah logika analitik.
