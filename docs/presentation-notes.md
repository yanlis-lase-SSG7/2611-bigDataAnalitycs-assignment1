# Naskah presentasi Olist: bahasa percakapan

Naskah ini sama dengan narasi pada speaker notes PPT. Total sekitar 1,238 kata, target 9 menit 30 detik atau rata-rata 130 kata per menit. Ini perkiraan, bukan durasi rekaman terukur. Referensi dan target waktu tidak perlu dibacakan.

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

## Slide 4: Konteks pasar dan urgensi bisnis

Target waktu: 02:05–02:40

Lalu, kenapa masalah pengiriman ini penting? Dalam e-commerce, pelanggan bukan hanya mempertimbangkan barangnya, tetapi juga kapan barang itu sampai.

Sebagai konteks, survei DHL tahun 2026 menyebut dua puluh persen pembeli merasa pengiriman lebih cepat dapat mendorong mereka menyelesaikan pembelian. OECD juga membahas peran ulasan dan rating dalam kepercayaan pada platform.

Saya memakai sumber ini untuk menjelaskan relevansi masalah. Namun, survei tersebut berbeda dari data Olist yang saya olah. Jadi, sumber eksternal memberi konteks, sedangkan angka dan prioritas analisis tetap saya ambil dari data proyek.

Sumber: DHL Group (2026): https://group.dhl.com/en/media-relations/press-releases/2026/dhl-ecommerce-trends-report-2026-old-rules-do-not-apply-in-the-age-of-ai.html
OECD (2019): https://doi.org/10.1787/23561431-en

## Slide 5: Tech stack dan alasan pemilihan

Target waktu: 02:40–04:00

Untuk mengerjakan proyek ini, saya memakai Python, dengan VS Code sebagai editor. Jupyter Notebook membantu saya menyusun proses per langkah, sehingga kode dan hasilnya bisa dilihat bersama.

Pengolahan tabel menggunakan PySpark. Java 17 dibutuhkan agar Spark dapat berjalan. Alasan saya memakai Spark adalah pembelajaran sekaligus menyatukan pengolahan data dan model dalam satu framework. Untuk ukuran data sekitar 120 MiB, pandas sebenarnya masih cukup. Spark saya jalankan di satu komputer, jadi skalabilitas cluster belum saya uji.

Hasil tabel disimpan sebagai Parquet dengan kompresi Snappy. Parquet menyimpan data per kolom dan mempertahankan tipe data, sedangkan Snappy membantu mengecilkan ukuran file.

Untuk model, saya memakai Random Forest dari MLlib, yaitu gabungan banyak pohon keputusan. Untuk graf, saya memakai pandas dan NetworkX karena jaringan state ini masih kecil. NumPy dan SciPy membantu perhitungan evaluasi numerik.

Git dan GitHub mencatat versi kode, laporan, serta ringkasan hasil. Jadi, kalau melanjutkan pekerjaan di perangkat lain, saya punya versi proyek yang jelas.

Sumber: requirements.txt; notebooks/README.md; docs/runtime-prerequisites.md; laporan bagian 2.4.

## Slide 6: Alur pipeline dan batas implementasi

Target waktu: 04:00–05:00

Supaya prosesnya mudah diikuti, saya membaginya menjadi tiga notebook. Notebook pertama menangani pembacaan CSV, pemeriksaan data, dan penyimpanan ke Parquet. Notebook kedua menyusun fitur dan model. Notebook ketiga menangani analisis graf.

Bagian pentingnya ada pada cara menggabungkan tabel. Satu order bisa mempunyai beberapa item dan beberapa catatan pembayaran. Kalau langsung digabung, nilai yang sama bisa muncul berulang dan totalnya menjadi terlalu besar.

Karena itu, detail item dan payment saya ringkas lebih dulu per order. Setelah itu baru saya lakukan join. Hasil fitur akhirnya mempunyai satu baris untuk satu order. Itu yang dimaksud dengan grain order.

Parquet sudah berjalan. Warehouse masih berupa rancangan, sementara server NoSQL, graph database fisik, dan dashboard belum saya bangun. NetworkX yang saya gunakan saat ini adalah library graf dalam memori.

Sumber: notebooks/01_Ingestion_and_Parquet_Conversion.ipynb; notebook 02/03; laporan Bab 2 dan 4.

## Slide 7: Hasil ingestion dan kualitas data

Target waktu: 05:00–05:50

Sekarang masuk ke hasil ingestion. Dari pemeriksaan yang sudah saya jalankan, sembilan tabel menghasilkan PASS. Pada ringkasan, status round-trip semuanya True. Artinya, hasil pengecekan yang dicatat notebook, termasuk jumlah baris dan profil nilai kosong setelah proses baca-tulis, sudah sesuai.

Ukuran seluruh CSV sekitar 120,34 MiB. Setelah menjadi Parquet, ukurannya sekitar 54,24 MiB. Jadi, penghematan storage mencapai 54,93 persen. Ini penghematan ruang penyimpanan; kecepatan kueri belum saya ukur.

Data raw tetap saya simpan agar sumber awal bisa diperiksa lagi. Nilai kosong pada review dan duplikasi geolocation saya catat dalam profil kualitas data.

Perlu dibedakan juga: demo membaca ringkasan hasil tersimpan. Pemeriksaan pembacaan dan konversi lengkap sudah dilakukan lewat notebook pertama sebelumnya.

Sumber: Hasil demo pengguna, bagian ingestion; outputs_ml_graph/ingestion_summary_report.csv dan ingestion_null_profile.json.

## Slide 8: Tata kelola dan perlindungan data

Target waktu: 05:50–06:35

Selain menghasilkan analisis, saya juga perlu memastikan data dikelola dengan jelas. Karena itu, raw tetap tersedia untuk audit, sedangkan yang masuk GitHub adalah kode, laporan, dan ringkasan agregat. Dataset raw, credential, serta runtime tidak ikut dipublikasikan.

Untuk penggunaan operasional, saya merancang akses sesuai peran, batas penyimpanan data, dan pemeriksaan informasi pribadi pada teks ulasan. Misalnya, tim yang hanya membutuhkan ringkasan rute tidak harus mendapat akses ke seluruh teks review.

ID yang terlihat seperti hash juga tidak otomatis membuat seluruh dataset anonim. Informasi pribadi masih mungkin muncul pada teks.

Jadi, ada praktik yang sudah berjalan di prototipe dan ada kontrol yang masih perlu diterapkan. Saya belum menganggap prototipe ini membuktikan kepatuhan operasional.

Sumber: Laporan Bab 3; .gitignore. Rujukan hukum lengkap terdapat pada laporan.

## Slide 9: Hasil model dan pemilihan ambang

Target waktu: 06:35–07:55

Untuk model, tantangan utamanya adalah jumlah order terlambat jauh lebih sedikit. Kalau model selalu menjawab tepat waktu, accuracy bisa terlihat tinggi, tetapi tidak membantu menemukan keterlambatan.

Saya membandingkan Random Forest tanpa bobot dengan versi yang memberi bobot lebih besar pada kelas terlambat. Data train dipakai untuk belajar, validation untuk memilih kandidat dan ambang, lalu test untuk evaluasi akhir. Jadi, test tidak dipakai untuk menentukan pilihan.

Ambang adalah batas skor untuk menandai order berisiko. Berdasarkan F1 validation, kandidat tanpa bobot dipilih dengan ambang sekitar 0,10. Nilai tepatnya ada di slide. F1 menyeimbangkan precision dan recall.

Pada test yang sama, recall naik dari nol menjadi 45,41 persen. Artinya, sekitar 45 dari 100 kasus terlambat berhasil ditemukan. Tetapi precision hanya 14,47 persen: dari 100 order yang ditandai, sekitar 14 benar-benar terlambat.

Ada 4.186 false positive, yaitu order tepat waktu yang ikut ditandai. Jadi, hasil ini masih untuk peninjauan. Ambang tersebut berasal dari skor model yang belum dikalibrasi sebagai probabilitas.

Sumber: Hasil demo pengguna, bagian model; model_evaluation_report.json; model_validation_comparison.csv; model_confusion_matrix.csv.

## Slide 10: Hasil graf dan prioritas rute

Target waktu: 07:55–08:50

Untuk graf, saya melihat hubungan antar-state, yaitu wilayah asal seller dan wilayah tujuan customer. Node mewakili state, sedangkan edge mewakili rute asal ke tujuan. Dari data ini terbentuk 27 node dan 409 rute.

Hasil pemeriksaan PASS karena jumlah order dari seluruh rute cocok dengan populasi graf. Sebagai contoh, rute SP ke RJ mempunyai 8.158 order dengan delay 15,49 persen. Angka itu lebih tinggi dari delay nasional, yaitu 8,11 persen.

Karena volumenya cukup besar dan persentase terlambatnya tinggi, rute ini masuk prioritas investigasi. Namun, kita baru mengetahui asal dan tujuan. Kita belum mengetahui tempat transit atau proses yang menyebabkan keterlambatan.

Jadi, graf ini membantu menentukan rute yang perlu diperiksa lebih lanjut. Untuk menentukan lokasi hub atau penyebab fisik masalah, saya masih membutuhkan data operasional yang lebih rinci.

Sumber: Hasil demo pengguna, bagian graph; graph_preparation_audit.json; seller_customer_routes_report.csv.

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
