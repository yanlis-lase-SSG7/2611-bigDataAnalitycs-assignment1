# Naskah presentasi Olist: versi penuh PowerPoint

Naskah berikut sama dengan speaker notes PPT. Bagian narasi dapat dibaca langsung; sumber dan target waktu tidak perlu dibacakan. Gunakan jeda pendek dan intonasi percakapan. Target 9:10 untuk seluruh 11 slide, belum merupakan durasi rekaman terukur.

## Slide 1: Analitik keterlambatan pengiriman Olist

Target waktu: 00:00–00:20

Halo, saya Yanlis Alim Sang Putra Lase. Di presentasi ini, saya membahas proyek analitik keterlambatan pengiriman Olist.

Fokusnya adalah memahami masalah bisnis, menyiapkan data yang bisa dipercaya, lalu merancang analisis yang sesuai. Saya juga akan menjelaskan teknologi yang saya gunakan dan hasil pemeriksaan proyek yang sudah saya jalankan.

Sumber: COMP8035041, Assignment I. Dataset Olist 2016–2018.

## Slide 2: Latar belakang masalah

Target waktu: 00:20–01:10

Olist adalah dataset transaksi e-commerce Brasil. Datanya tersebar di sembilan tabel, mulai dari order, customer, seller, sampai item, payment, dan review.

Masalah yang saya angkat adalah keterlambatan pengiriman. Dari 96.470 order yang tanggal labelnya valid, 7.826 terlambat, atau sekitar 8,11 persen.

Saya membandingkan waktu penerimaan aktual dengan waktu estimasi. Rata-rata review kelompok tepat waktu sekitar 4,29, sedangkan kelompok terlambat sekitar 2,57.

Jadi, ada hubungan yang perlu diperhatikan. Namun, angka ini belum membuktikan bahwa keterlambatan adalah satu-satunya penyebab review rendah.

Itulah alasan saya mulai dari baseline dan kualitas data sebelum membahas tindakan operasional.

Sumber: Laporan Bab 1; outputs_ml_graph/feature_preparation_audit.json; notebook 02 untuk review per order.

## Slide 3: Tujuan proyek dan pengguna hasil

Target waktu: 01:10–01:55

Yang ingin saya selesaikan adalah bagaimana mengubah data transaksi yang terpisah menjadi informasi yang bisa dipakai untuk meninjau risiko keterlambatan. Ada dua tujuan utama: menyiapkan pipeline yang konsisten dan membantu menentukan prioritas investigasi.

Tim Logistics dapat melihat rute yang perlu diperiksa. Merchant Performance dapat meninjau order berisiko setelah approval.

Manajemen dapat memantau hasil agregat. Untuk Assignment I, pekerjaan utamanya adalah rancangan solusi dan persiapan data.

Model dan graf saya gunakan sebagai eksplorasi awal. Jadi, saya belum mengatakan keterlambatan sudah turun atau biaya sudah hemat.

Dampak itu baru bisa diukur setelah ada intervensi.

Sumber: Laporan Bab 1 dan 2; lingkup Assignment I pada instruksi tugas lokal.

## Slide 4: Konteks pasar dan urgensi bisnis

Target waktu: 01:55–02:30

Masalah ini juga relevan dengan konteks e-commerce yang lebih luas. Dalam survei DHL tahun 2026, dua puluh persen pembeli menyatakan pengiriman lebih cepat dapat mendorong penyelesaian pembelian.

OECD juga membahas peran ulasan dan rating dalam membangun kepercayaan pada platform. Saya memakai sumber ini untuk menjelaskan relevansi masalah, bukan untuk menyimpulkan perilaku pelanggan Olist.

Survei global tahun 2026 berbeda dari transaksi Olist tahun 2016 sampai 2018. Karena itu, keputusan analitik dalam proyek ini tetap berangkat dari baseline Olist yang saya hitung.

Sumber: DHL Group (2026): https://group.dhl.com/en/media-relations/press-releases/2026/dhl-ecommerce-trends-report-2026-old-rules-do-not-apply-in-the-age-of-ai.html
OECD (2019): https://doi.org/10.1787/23561431-en

## Slide 5: Tech stack dan alasan pemilihan

Target waktu: 02:30–03:40

Untuk pengembangannya, saya memakai Python 3.11, VS Code, dan Jupyter Notebook. Python menjadi bahasa utama, VS Code sebagai editor, dan notebook membantu saya menjelaskan proses sekaligus menyimpan output tiap langkah.

Pengolahan tabel memakai PySpark 4.0.4, dengan Java 17 sebagai runtime Spark. Saya memilih Spark untuk belajar dan menyatukan transformasi serta MLlib dalam satu framework.

Dengan data sekitar 120 MiB, pandas sebenarnya masih layak. Jadi, ini bukan klaim bahwa dataset kecil harus memakai cluster.

Parquet dengan Snappy menyimpan tabel bertipe secara lebih ringkas. MLlib menyediakan Random Forest untuk eksplorasi prediksi.

NumPy dan SciPy membantu perhitungan numerik untuk evaluasi. Untuk graf, saya memakai pandas dan NetworkX karena jaringan state masih kecil dan bisa dianalisis dalam memori.

Terakhir, Git dan GitHub menyimpan kode, laporan, serta ringkasan hasil supaya pekerjaan dapat dilanjutkan lintas perangkat. Raw data dan runtime tetap lokal.

Sumber: requirements.txt; notebooks/README.md; docs/runtime-prerequisites.md; laporan bagian 2.4.

## Slide 6: Alur pipeline dan batas implementasi

Target waktu: 03:40–04:40

Pipeline saya terdiri dari tiga notebook yang dijalankan berurutan. Notebook pertama membaca sembilan CSV, memvalidasi data, lalu menulis Parquet.

Notebook kedua menyusun fitur per order dan melakukan eksplorasi model. Detail item dan payment diagregasi lebih dulu supaya join tidak menggandakan nilai.

Notebook ketiga membentuk graf asal seller dan tujuan customer. Untuk fitur, grain atau unit tiap baris adalah satu order karena label delay juga berada pada order.

Parquet sudah diimplementasikan, sedangkan warehouse masih berupa rancangan dimensional. NetworkX juga belum menjadi graph database fisik.

NoSQL dan dashboard masih rencana, dan baru perlu ditambahkan jika kebutuhan pengguna mendukungnya.

Sumber: notebooks/01_Ingestion_and_Parquet_Conversion.ipynb; notebook 02/03; laporan Bab 2 dan 4.

## Slide 7: Hasil ingestion dan kualitas data

Target waktu: 04:40–05:40

Pada bagian ingestion, pemeriksaan demo yang saya jalankan menghasilkan PASS untuk sembilan tabel. Status round-trip pada ringkasan semuanya benar.

Total ukuran CSV sekitar 120,341 MiB, sedangkan Parquet sekitar 54,236 MiB. Jadi, penghematan storage keseluruhannya 54,93 persen.

Ini ukuran penyimpanan, belum bukti proses kueri lebih cepat. Saya tetap mempertahankan raw untuk audit.

Data juga diperiksa dari sisi tipe, ID dan key, jumlah baris, serta profil nilai kosong. Teks review yang kosong dan duplikasi geolocation saya profilkan, bukan langsung hapus dari raw.

Demo ini memeriksa ringkasan hasil tersimpan. Validasi pembacaan dan konversi penuh sudah dilakukan sebelumnya melalui notebook pertama.

Sumber: Hasil demo pengguna, bagian ingestion; outputs_ml_graph/ingestion_summary_report.csv dan ingestion_null_profile.json.

## Slide 8: Tata kelola dan perlindungan data

Target waktu: 05:40–06:20

Selain proses analitik, saya juga mempertimbangkan tata kelola. Praktik yang sudah berjalan adalah mempertahankan raw untuk audit dan menyimpan ringkasan agregat serta kode di Git.

Dataset raw, credential, runtime, dan output besar tidak masuk repository. Untuk penggunaan operasional, saya merancang akses sesuai peran, retensi, minimisasi data, dan pemeriksaan informasi pribadi pada teks ulasan.

Penting juga untuk tidak menganggap ID berbentuk hash otomatis anonim. Kontrol operasional ini masih perlu diimplementasikan dan diuji.

Jadi, saya membedakan praktik prototipe yang sudah berjalan dengan rancangan perlindungan data untuk tahap berikutnya.

Sumber: Laporan Bab 3; .gitignore. Rujukan hukum lengkap terdapat pada laporan.

## Slide 9: Hasil model dan pemilihan ambang

Target waktu: 06:20–07:30

Kelas terlambat jauh lebih sedikit, sehingga accuracy saja bisa menyesatkan. Saya membandingkan Random Forest tanpa bobot dengan model berbobot kelas.

Kandidat dan ambang dipilih berdasarkan F1 pada validation, lalu dievaluasi pada test. Kandidat tanpa bobot menang, dengan ambang sekitar 0,099536 dan F1 validation sekitar 0,2168.

Pada partisi test yang sama, ambang 0,5 menghasilkan recall nol. Setelah ambang diturunkan, recall menjadi 45,41 persen.

Artinya, model menangkap sekitar empat puluh lima persen kasus terlambat dalam test. Tetapi precision hanya 14,47 persen, dan ada 4.186 false positive.

Jadi, banyak peringatan yang belum tepat. Hasil demo PASS karena pilihan kandidat, jumlah populasi, dan metrik yang dihitung ulang dari confusion matrix konsisten.

Untuk saat ini model cocok sebagai sinyal peninjauan, dan belum cukup untuk keputusan otomatis.

Sumber: Hasil demo pengguna, bagian model; model_evaluation_report.json; model_validation_comparison.csv; model_confusion_matrix.csv.

## Slide 10: Hasil graf dan prioritas rute

Target waktu: 07:30–08:25

Untuk graf, node mewakili state, sedangkan edge mewakili hubungan asal seller dengan tujuan customer. Hasilnya adalah 27 node dan 409 rute.

Demo yang saya jalankan menghasilkan PASS karena jumlah order pada rute sesuai dengan total populasi graf. Delay nasional tetap 8,11 persen.

Salah satu rute yang perlu diprioritaskan adalah SP ke RJ, dengan 8.158 order dan delay 15,49 persen. Nilainya lebih tinggi dari baseline nasional, sehingga layak diinvestigasi.

Namun, graf ini tidak mencatat perjalanan transit paket. Saya belum bisa memakai hasil ini untuk menentukan lokasi hub atau menyatakan penyebab fisik bottleneck.

Analisis lanjutan memerlukan data operasional pengiriman yang lebih rinci.

Sumber: Hasil demo pengguna, bagian graph; graph_preparation_audit.json; seller_customer_routes_report.csv.

## Slide 11: Ringkasan validasi dan langkah berikutnya

Target waktu: 08:25–09:10

Dari hasil tadi, ketiga bagian pemeriksaan demo sudah berhasil. Ingestion konsisten, pemilihan ambang dan evaluasi model cocok, lalu jumlah populasi graf juga sesuai.

Hasil ini saya tampilkan langsung di PowerPoint sebagai hasil pemeriksaan yang sudah dijalankan, bukan eksekusi live saat presentasi. Kesimpulan proyek ini adalah kita sudah mempunyai baseline, pipeline data bertipe, dan rancangan solusi yang dapat diaudit.

Langkah berikutnya adalah menguji model pada periode waktu berbeda, menghitung biaya intervensi, dan menilai kebutuhan dashboard bersama pengguna. Dengan begitu, analisis bisa berkembang menjadi keputusan operasional yang lebih terukur.

Sekian presentasi saya. Terima kasih.

Sumber: Hasil tiga perintah demo yang dibagikan pengguna; demo_assignment1.py; laporan batas implementasi.
