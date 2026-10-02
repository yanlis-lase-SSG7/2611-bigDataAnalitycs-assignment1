# Naskah presentasi Olist: bahasa percakapan

Naskah ini sama dengan narasi pada speaker notes PPT. Target total tetap 9 menit 30 detik; durasi nyata harus diuji lewat latihan. Referensi dan target waktu tidak perlu dibacakan.

Baca satu paragraf sebagai satu gagasan. Ambil jeda singkat saat berpindah ke gagasan berikutnya. Tidak perlu menambahkan kata pengisi pada setiap kalimat; biarkan penjelasan dan contoh yang membuatnya terdengar seperti percakapan.

## Slide 1: Analitik keterlambatan pengiriman Olist

Target waktu: 00:00–00:25

Halo, saya Yanlis Alim Sang Putra Lase. Kali ini saya akan menjelaskan proyek analitik keterlambatan pengiriman menggunakan data Olist.

Alurnya dimulai dari masalah yang ingin saya pahami, cara saya menyiapkan datanya, lalu hasil analisisnya. Jadi, selain menunjukkan angka, saya juga akan menjelaskan kenapa saya memilih cara kerja dan teknologi tersebut.

Sumber: COMP8035041, Assignment I. Dataset Olist 2016–2018.

## Slide 2: Latar belakang masalah

Target waktu: 00:25–01:20

Saya mulai dari datanya dulu. Olist merupakan data transaksi e-commerce di Brasil, dengan periode transaksi tahun 2016 sampai 2018. Informasinya tersebar di sembilan tabel. Misalnya, data pesanan ada di tabel order, rincian barang ada di tabel item, dan penilaian pelanggan ada di tabel review.

Masalah yang saya fokuskan adalah pengiriman terlambat. Di sini, terlambat berarti waktu penerimaan aktual melewati waktu estimasi. Jadi, saya memakai perbandingan timestamp, bukan sekadar selisih hari.

Dari sekitar 96 ribu order dengan tanggal yang valid, ada 7.826 order terlambat, atau 8,11 persen. Rata-rata review kelompok tepat waktu sekitar 4,29, sedangkan kelompok terlambat sekitar 2,57.

Angka ini menjadi titik awal atau baseline saya. Ada hubungan yang perlu diperhatikan, tetapi belum bisa disimpulkan bahwa keterlambatan merupakan satu-satunya penyebab review rendah.

Sumber: Laporan Bab 1; outputs_ml_graph/feature_preparation_audit.json; notebook 02 untuk review per order.

## Slide 3: Tujuan proyek dan pengguna hasil

Target waktu: 01:20–02:05

Dari masalah tadi, saya ingin membuat data transaksi ini lebih mudah dipakai untuk meninjau keterlambatan. Jadi, pekerjaan saya bukan berhenti pada menghitung berapa order yang terlambat, tetapi juga menyiapkan dasar untuk menentukan bagian mana yang perlu diperiksa.

Contohnya, tim Logistics bisa melihat rute dengan keterlambatan tinggi. Tim Merchant Performance bisa meninjau order yang ditandai berisiko setelah approval. Sementara itu, manajemen bisa memakai ringkasan hasil untuk memantau kondisi keseluruhan.

Untuk Assignment I, fokus utamanya adalah rancangan solusi dan persiapan data. Model dan graf menjadi eksplorasi tambahan. Jadi, hasil saat ini membantu menyusun prioritas investigasi. Penurunan keterlambatan yang sebenarnya baru bisa dibuktikan setelah ada tindakan dan evaluasi dampaknya.

Sumber: Laporan Bab 1 dan 2; lingkup Assignment I pada instruksi tugas lokal.

## Slide 4: Distribusi order dan definisi keterlambatan

Target waktu: 02:05–02:50

Di sini saya ingin memperjelas dari mana angka keterlambatan tadi berasal. Grafik kiri mencakup semua 99.441 order; sebagian besar, yaitu 96.478, berstatus delivered. Sumbu jumlah memakai skala log agar status yang jumlahnya kecil masih terlihat. Status lain seperti canceled dan shipped tetap ada di data, tetapi tidak ikut dihitung dalam delay rate.

Ada delapan order delivered tanpa tanggal penerimaan aktual. Setelah delapan itu dikeluarkan, tersisa 96.470 order yang bisa dibandingkan dengan tanggal estimasi. Dari populasi inilah 7.826 order, atau 8,11 persen, tercatat terlambat. Jadi, dua grafik ini memakai denominator berbeda. Saya perlu menyebutkannya supaya angka 8,11 persen tidak disalahartikan sebagai persentase dari seluruh order.

Sumber: outputs_ml_graph/eda_order_status.csv; outputs_ml_graph/eda_quality_profile.json; laporan Tabel 4.5.

## Slide 5: Tech stack dan alasan pemilihan

Target waktu: 02:50–04:00

Untuk mengerjakan proyek ini, saya memakai Python, dengan VS Code sebagai editor. Jupyter Notebook membantu saya menyusun proses per langkah, sehingga kode dan hasilnya bisa dilihat bersama.

Pengolahan tabel menggunakan PySpark. Java 17 dibutuhkan agar Spark dapat berjalan. Alasan saya memakai Spark adalah pembelajaran sekaligus menyatukan pengolahan data dan model dalam satu framework. Untuk ukuran data sekitar 120 MiB, pandas sebenarnya masih cukup. Spark saya jalankan di satu komputer, jadi skalabilitas cluster belum saya uji.

Hasil tabel disimpan sebagai Parquet dengan kompresi Snappy. Parquet menyimpan data per kolom dan mempertahankan tipe data, sedangkan Snappy membantu mengecilkan ukuran file.

Untuk model, saya memakai Random Forest dari MLlib, yaitu gabungan banyak pohon keputusan. Untuk graf, saya memakai pandas dan NetworkX karena jaringan state ini masih kecil. NumPy dan SciPy membantu perhitungan evaluasi numerik.

Git dan GitHub mencatat versi kode, laporan, serta ringkasan hasil. Jadi, kalau melanjutkan pekerjaan di perangkat lain, saya punya versi proyek yang jelas.

Sumber: requirements.txt; notebooks/README.md; docs/runtime-prerequisites.md; laporan bagian 2.4.

## Slide 6: Arsitektur data lake dan batas implementasi

Target waktu: 04:00–05:00

Diagram ini membedakan sistem yang sudah saya jalankan dari rancangan pengembangannya. Pada prototipe, sembilan CSV dibaca Spark dengan skema dan mode FAILFAST, divalidasi, lalu disimpan sebagai Parquet Snappy lokal. Skrip EDA dan notebook berikutnya membaca tabel tersebut. Semua ini berjalan di satu komputer dengan Spark local[4].

Untuk skala enterprise, saya mengusulkan zona raw dan curated pada S3 atau HDFS, lalu pemrosesan pada cluster Spark. Tiga worker pada diagram hanya contoh titik awal, bukan kebutuhan kapasitas yang sudah terbukti. Jumlah worker, partisi waktu, biaya, dan kinerja masih harus diuji.

Sebelum membuat fitur satu baris per order, saya juga merangkum item dan payment per order. Langkah itu mencegah angka terlipat akibat join pada dua tabel yang sama-sama punya banyak baris per order. Warehouse, NoSQL, dan graph database fisik belum dibangun.

Sumber: laporan Bab 2 dan 4; figures/fig0_enterprise_architecture.png; notebook 01–03.

## Slide 7: Hasil ingestion dan kualitas data

Target waktu: 05:00–05:50

Sekarang masuk ke hasil ingestion. Dari pemeriksaan yang sudah saya jalankan, sembilan tabel menghasilkan PASS. Pada ringkasan, status round-trip semuanya True. Artinya, hasil pengecekan yang dicatat notebook, termasuk jumlah baris dan profil nilai kosong setelah proses baca-tulis, sudah sesuai.

Ukuran seluruh CSV sekitar 120,34 MiB. Setelah menjadi Parquet, ukurannya sekitar 54,24 MiB. Jadi, penghematan storage mencapai 54,93 persen. Ini penghematan ruang penyimpanan; kecepatan kueri belum saya ukur.

Data raw tetap saya simpan agar sumber awal bisa diperiksa lagi. Nilai kosong pada review dan duplikasi geolocation saya catat dalam profil kualitas data.

Perlu dibedakan juga: demo membaca ringkasan hasil tersimpan. Pemeriksaan pembacaan dan konversi lengkap sudah dilakukan lewat notebook pertama sebelumnya.

Sumber: Hasil demo pengguna, bagian ingestion; outputs_ml_graph/ingestion_summary_report.csv dan ingestion_null_profile.json.

## Slide 8: Profil null dan tata kelola data

Target waktu: 05:50–06:35

Grafik ini menunjukkan bahwa nilai kosong paling banyak ada pada judul dan teks ulasan: masing-masing sekitar 88 dan 59 persen. Keduanya bersifat opsional, jadi saya tidak menghapus record hanya karena teks review tidak diisi. Sebaliknya, kolom kunci yang penting untuk perhitungan diuji null-nya, dan empat relasi order–customer, item–order, item–seller, serta item–product yang saya periksa tidak menghasilkan orphan.

Untuk privasi, skrip EDA memakai token seller SHA-256 bersalt sementara di memori Spark, lalu hanya mengeluarkan agregat per state. Itu membantu membatasi ID pada output, tetapi bukan berarti dataset sudah anonim atau siap memenuhi seluruh kewajiban LGPD. Akses sesuai peran, retensi, enkripsi, dan pemeriksaan teks pribadi masih bagian dari rancangan deployment.

Sumber: outputs_ml_graph/eda_quality_profile.json; eda_assignment1.py; figures/fig4_null_profile_heatmap.png; laporan Bab 3–4.

## Slide 9: Hasil model dan pemilihan ambang

Target waktu: 06:35–07:55

Untuk model, tantangan utamanya adalah jumlah order terlambat jauh lebih sedikit. Kalau model selalu menjawab tepat waktu, accuracy bisa terlihat tinggi, tetapi tidak membantu menemukan keterlambatan.

Saya membandingkan Random Forest tanpa bobot dengan versi yang memberi bobot lebih besar pada kelas terlambat. Data train dipakai untuk belajar, validation untuk memilih kandidat dan ambang, lalu test untuk evaluasi akhir. Jadi, test tidak dipakai untuk menentukan pilihan.

Ambang adalah batas skor untuk menandai order berisiko. Berdasarkan F1 validation, kandidat tanpa bobot dipilih dengan ambang sekitar 0,10. Nilai tepatnya ada di slide. F1 menyeimbangkan precision dan recall.

Pada test yang sama, recall naik dari nol menjadi 45,41 persen. Artinya, sekitar 45 dari 100 kasus terlambat berhasil ditemukan. Tetapi precision hanya 14,47 persen: dari 100 order yang ditandai, sekitar 14 benar-benar terlambat.

Ada 4.186 false positive, yaitu order tepat waktu yang ikut ditandai. Jadi, hasil ini masih untuk peninjauan. Ambang tersebut berasal dari skor model yang belum dikalibrasi sebagai probabilitas.

Sumber: Hasil demo pengguna, bagian model; model_evaluation_report.json; model_validation_comparison.csv; model_confusion_matrix.csv.

## Slide 10: Wilayah berisiko dan prioritas rute

Target waktu: 07:55–08:50

Grafik di kiri mengurutkan state tujuan customer berdasarkan delay rate. AL terlihat paling tinggi, 23,93 persen dari 397 order. Karena volumenya jauh lebih kecil daripada beberapa state lain, saya tidak boleh memilih prioritas hanya dari persentase itu.

Analisis graf melihat hal yang berbeda: state asal primary seller menuju state tujuan customer. Dari agregat ini terbentuk 27 node dan 409 rute. Rute SP ke RJ memuat 8.158 order, dengan 15,49 persen terlambat, sehingga layak diperiksa karena persentase dan volumenya sama-sama berarti. Delay nasional untuk populasi berlabel adalah 8,11 persen.

Graf ini hanya mencatat asal dan tujuan. Tidak ada informasi titik transit atau lokasi hub, jadi saya tidak mengklaim sudah menemukan penyebab fisik keterlambatan. Angka per state customer dan angka per rute juga punya grain berbeda; keduanya tidak dijumlahkan.

Sumber: outputs_ml_graph/eda_state_delay.csv; figures/fig3_top10_state_delay_rate.png; graph_preparation_audit.json; seller_customer_routes_report.csv.

## Slide 11: Ringkasan validasi dan langkah berikutnya

Target waktu: 08:50–09:30

Dari seluruh proses tadi, ketiga pemeriksaan sudah berhasil: ingestion, model, dan graf. PASS di sini berarti hasil yang diperiksa konsisten, bukan berarti masalah keterlambatan sudah selesai.

Hasil demo saya tampilkan sebagai pemeriksaan yang sudah dijalankan sebelumnya. Jadi, presentasi ini bisa dijelaskan sepenuhnya lewat PowerPoint.

Kesimpulannya, proyek ini sudah menyediakan baseline, data bertipe yang bisa diaudit, dan rancangan analisis untuk meninjau risiko keterlambatan. Berikutnya, model perlu diuji pada periode berbeda dan dibandingkan dengan biaya intervensi. Kebutuhan dashboard juga perlu dibahas bersama pengguna.

Dengan langkah itu, analisis bisa berkembang menjadi keputusan yang manfaatnya dapat diukur. Terima kasih.

Sumber: Hasil tiga perintah demo yang dibagikan pengguna; demo_assignment1.py; laporan batas implementasi.

## Latihan singkat sebelum merekam (tidak dibacakan)

Coba jelaskan tiga hal berikut dengan kalimat sendiri tanpa melihat naskah. Jika masih ragu, baca kembali paragraf terkait sebelum rekaman.

- Mengapa item dan payment diringkas sebelum join? Satu order punya banyak detail pada kedua tabel; join langsung bisa mengulang nilai.
- Apa bedanya recall dan precision? Recall melihat kasus terlambat yang berhasil ditemukan; precision melihat ketepatan order yang ditandai.
- Apa arti PASS? Ringkasan hasil konsisten dengan pemeriksaan yang dijalankan. PASS tidak menunjukkan model sempurna atau keterlambatan bisnis sudah berkurang.
