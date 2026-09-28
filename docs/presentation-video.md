# Rencana presentasi dan live demo Assignment I

Target rekaman: 9 menit 15 detik dalam satu video. Presentasi 7 menit, live demo 2 menit, penutup 15 detik. Batas tugas 10 menit. Ini storyboard dan naskah untuk pembuatan PPT; berkas PPTX belum dibuat. Sesuaikan narasi dengan pemahaman sendiri dan latih dengan stopwatch.

Fokus utama tetap Assignment I: masalah bisnis, rancangan teknologi, tata kelola, persiapan dan organisasi data. Hasil ML/graf menunjukkan eksplorasi awal. Jangan menyebut dampak intervensi, deployment database, dashboard, atau cluster sebagai hasil yang sudah tercapai.

## Storyboard PPT

### 1. Analitik keterlambatan pengiriman Olist (00:00–00:20)

Tampilan: judul, nama Yanlis Alim Sang Putra Lase, NIM 2702751284, COMP8035041, Assignment I. Tambahkan subjudul “Rancangan solusi dan persiapan data”.

Narasi: “Saya membahas rancangan analitik untuk keterlambatan pengiriman pada dataset historis Olist 2016–2018. Saya menjelaskan masalah dan keputusan rancangan, lalu menunjukkan pemeriksaan hasil proyek langsung di VS Code setelah presentasi.”

### 2. Masalah pengiriman dan pengguna hasil (00:20–01:15)

Tampilan: 8,11% terlambat, 7.826 dari 96.470 order berlabel, review tepat waktu 4,2943 dan terlambat 2,5665. Tabel kecil pengguna/keputusan: Logistics/investigasi rute, Merchant Performance/peninjauan order setelah approval, Executive/pemantauan agregat.

Narasi: “Label terlambat membandingkan timestamp penerimaan dengan estimasi. Delapan order delivered tidak mempunyai tanggal label yang valid sehingga dikeluarkan. Perbedaan review dihitung per order yang mempunyai review, bukan seluruh order. Hubungan ini merupakan asosiasi. Tujuannya mendukung investigasi keterlambatan dan peninjauan order berisiko. Dampak penurunan keterlambatan harus diukur setelah intervensi pada populasi sebanding.”

Catatan sumber: laporan Bab 1; feature_preparation_audit.json, graph_preparation_audit.json, notebook 02 untuk agregasi review.

### 3. Konteks pasar dan kebutuhan bisnis (01:15–02:05)

Tampilan: DHL 2026 sebagai konteks preferensi pengiriman, OECD 2019 sebagai konteks kepercayaan platform. Sertakan keterangan terlihat: “Konteks global berbeda dari data Olist 2016–2018”.

Narasi: “Survei DHL mencakup 29.000 pembeli online dan 5.800 bisnis di 29 negara. Dua puluh persen pembeli menyatakan pengiriman lebih cepat dapat mendorong penyelesaian pembelian. OECD membahas peran ulasan dan rating dalam kepercayaan platform. Sumber ini menjelaskan relevansi masalah, sementara prioritas operasional tetap memakai data Olist. Preferensi kecepatan berbeda dari terlambat terhadap estimasi. Studi ini belum mengukur penghematan biaya ataupun menetapkan target penurunan numerik.”

Catatan sumber untuk speaker notes: [DHL Group, 2 Juni 2026](https://group.dhl.com/en/media-relations/press-releases/2026/dhl-ecommerce-trends-report-2026-old-rules-do-not-apply-in-the-age-of-ai.html), [OECD, Unpacking E-commerce, 2019](https://doi.org/10.1787/23561431-en). Parafrase, jangan kutip panjang.

### 4. Pipeline dan status implementasi (02:05–03:10)

Tampilan: urutan bernomor CSV raw, ingestion PySpark, Parquet Snappy, fitur per order, eksplorasi RF/graf. Tabel status: Parquet dan notebook/terimplementasi; warehouse/konseptual; NoSQL dan graph database/pengembangan berdasarkan kebutuhan; dashboard/rencana.

Narasi: “Notebook 01 memvalidasi sembilan tabel dan menulis Parquet. Notebook 02 mengagregasi detail menjadi fitur per order sebelum join. Notebook 03 membentuk jaringan state asal seller dan tujuan customer. Semua berjalan lokal di Windows. Spark memakai local[4] pada satu mesin. NetworkX merupakan library graf dalam memori. Rancangan warehouse belum menjadi server SQL, dan audit JSON atau teks review belum menjadi document store. Saya menunda server tambahan sampai kebutuhan akses bersama dan kueri persisten benar-benar diuji.”

Catatan sumber: laporan Bab 2 dan 4; notebooks/README.md. Hindari menyebut simulasi empat database atau produksi cluster.

### 5. Kualitas data dan organisasi tabel (03:10–04:10)

Tampilan: sembilan tabel, 120,341 MiB CSV menjadi 54,236 MiB Parquet, hemat 54,93%. Tampilkan tiga aturan yang memang dijalankan: raw tetap utuh, casting/ID/key/round-trip checks, aggregate-before-join dengan grain order.

Narasi: “Validasi mencakup parsing, typed cast, ID dan key yang sesuai, jumlah baris, null profile, serta pemeriksaan hasil setelah penyalinan. Teks review yang kosong dan duplikasi geolocation diprofilkan. Keduanya tidak dihapus diam-diam dari raw. Item dan payment diagregasi sebelum join agar nilai tidak berulang. Uji ilustrasi join mentah memperlihatkan inflasi price 4,48 persen. Penghematan Parquet adalah ukuran storage, belum merupakan bukti kueri lebih cepat.”

Catatan sumber: ingestion_summary_report.csv, ingestion_null_profile.json, feature_preparation_audit.json, laporan bagian grain dan bukti join.

### 6. Tata kelola dan perlindungan data (04:10–05:00)

Tampilan: dua kolom “Praktik prototipe” dan “Kontrol rancangan”. Praktik: raw dipertahankan, audit hasil, Git hanya ringkasan agregat dan kode. Rancangan: akses sesuai peran, retensi, pemeriksaan teks ulasan dan minimisasi data sesuai kebutuhan.

Narasi: “ID yang terlihat seperti hash tidak otomatis menjamin anonimitas, dan teks ulasan dapat memuat data pribadi. Prototipe mempertahankan sumber untuk audit, sementara Git mengecualikan raw, runtime, credential dan output besar. Untuk penggunaan operasional saya merancang akses sesuai peran, kebijakan retensi dan pemeriksaan informasi pribadi pada teks. Kontrol rancangan ini perlu implementasi dan pengujian. Saya tidak mengklaim prototipe sudah membuktikan kepatuhan hukum.”

Catatan sumber: laporan Bab 3 dan referensi hukum yang tercantum di sana. Jangan menampilkan ulasan pelanggan atau data pribadi selama demo.

### 7. Justifikasi teknologi dan grain (05:00–06:00)

Tampilan: matriks ringkas pilihan/alasan/batas. PySpark/integrasi DataFrame dan MLlib/runtime lebih kompleks; Parquet/tipe dan columnar/benchmark kueri belum ada; NetworkX/27 state dan 409 rute/memori satu mesin; warehouse dimensional/grain terpisah/konseptual.

Narasi: “Pada sekitar 120 MiB, pandas masih layak. Saya memilih Spark untuk pembelajaran dan integrasi pipeline dalam satu framework, bukan karena VS Code mengharuskan Spark. VS Code mendukung keduanya. Fitur memakai satu baris per order karena label berada pada order. Rancangan dimensional memisahkan grain item, pengiriman, payment dan review. Pemindahan ke cluster memerlukan pengujian konfigurasi, keamanan dan performa. Pertumbuhan data bukan alasan untuk menyebut kode sudah production-ready.”

Catatan sumber: laporan bagian 2.4 dan docs/presentation-notes.md.

### 8. Eksplorasi awal model dan graf (06:00–06:40)

Tampilan: threshold 0,099536 dipilih pada validation; test recall 45,41%, precision 14,47%; graf SP–RJ 8.158 order dan delay 15,49%. Tampilkan label “Sinyal peninjauan, manfaat operasional belum diuji”.

Narasi: “Model membandingkan RF tanpa bobot dan bobot kelas. Validation F1 memilih kandidat tanpa bobot dengan ambang lebih rendah. Pada test yang sama, recall meningkat dari nol pada ambang 0,5 menjadi 45,41 persen, tetapi precision hanya 14,47 persen. Graf memprioritaskan investigasi SP–RJ. Graf asal–tujuan ini tidak mencatat transit dan belum menentukan lokasi hub. Validasi temporal dan biaya intervensi menjadi pekerjaan selanjutnya.”

Catatan sumber: model_validation_comparison.csv, model_evaluation_report.json, seller_customer_routes_report.csv. Jangan menyebut recall training atau validation sebagai hasil test.

### 9. Pemeriksaan hasil di VS Code (06:40–07:00)

Tampilan: tiga pemeriksaan demo: ringkasan ingestion, konsistensi evaluasi model, populasi graf dan rute. Keterangan terlihat “Pemeriksaan laporan tersimpan; pipeline penuh telah dijalankan sebelumnya”.

Narasi: “Saya beralih ke VS Code dalam video yang sama. Script read-only akan memeriksa konsistensi file hasil yang sudah tersimpan. Demo ini menjalankan kode pemeriksaan secara langsung. Saya tidak menjalankan ulang ingestion atau pelatihan penuh dalam dua menit.”

## Live demo (07:00–09:00)

Siapkan terminal PowerShell di root proyek, font cukup besar, Explorer dan notebook 02 sudah terbuka. Tutup akun, notifikasi, tab pribadi, serta panel yang menampilkan credential. Pertahankan rekaman saat berpindah dari slide ke VS Code.

Perintah berikut memakai interpreter lokal dan hanya membaca ringkasan agregat. Bisa memakai `python` atau `py -3.11` pada laptop lain karena script tidak membutuhkan package tambahan.

**07:00–07:30:** jalankan:

```powershell
.\.venv\Scripts\python.exe demo_assignment1.py --section ingestion
```

Jelaskan sembilan tabel, status round-trip yang tercatat, serta total penghematan storage. Script memeriksa konsistensi ringkasan, bukan membaca ulang seluruh Parquet. Untuk memperlihatkan logika aslinya, tunjukkan bagian validasi notebook 01 tanpa Run All.

**07:30–08:20:** jalankan:

```powershell
.\.venv\Scripts\python.exe demo_assignment1.py --section model
```

Tunjukkan bahwa kandidat/threshold cocok dengan tabel validation, jumlah split cocok, CSV/JSON confusion matrix sama, dan metrik dihitung ulang dari confusion matrix. Jelaskan kompromi recall dengan false positive. Buka bagian pemilihan ambang notebook 02 bila waktunya cukup. Pemeriksaan ringkasan tidak membuktikan tidak ada overlap order atau leakage; notebook/manifest mendukung pemeriksaan tersebut.

**08:20–09:00:** jalankan:

```powershell
.\.venv\Scripts\python.exe demo_assignment1.py --section graph
```

Tunjukkan jumlah rute/node, konsistensi total order dan SP–RJ. Script menjumlahkan rute dan memeriksa persentase terhadap count. Model memiliki 96.455 order eligible, sedangkan graf dan label valid 96.470; selisih 15 merupakan eksklusi predictor, bukan error populasi. Tutup dengan batas graf asal–tujuan.

Jika butuh satu perintah untuk latihan/pemeriksaan:

```powershell
.\.venv\Scripts\python.exe demo_assignment1.py
```

Jika muncul FAIL, hentikan persiapan rekaman dan periksa sumber ketidaksesuaian. Jangan mengubah angka agar demo lolos. Script tidak mengganti hasil notebook. Jalankan ulang pipeline hanya bila hasil memang belum mutakhir, kemudian latihan ulang.

## Penutup (09:00–09:15)

“Studi ini menyiapkan baseline, pipeline bertipe dan rancangan solusi yang dapat diaudit. Langkah berikutnya adalah validasi temporal dan penilaian biaya intervensi sebelum tindakan operasional, serta pengembangan dashboard berdasarkan kebutuhan pengguna. Terima kasih.”

## Urutan persiapan berikutnya

1. Buat PPT 16:9 dari sembilan storyboard di atas. Salin narasi dan sumber ke speaker notes. Gunakan tabel/grafik hasil proyek sebagai bukti dan hindari memadatkan seluruh narasi pada slide.
2. Periksa seluruh slide, lalu latihan perpindahan PowerPoint ke VS Code. Target akhir 9:15, sisakan 45 detik terhadap batas tugas.
3. Mahasiswa melengkapi deklarasi AI dan meninjau Word, kemudian ekspor PDF final. Jangan mengambil PDF QA lama sebagai versi pengumpulan jika Word telah berubah.
4. Rekam satu video berisi PPT, demo dan penutup. Periksa audio, keterbacaan terminal, dan durasi akhir maksimal 10 menit.

PPTX belum tersedia karena dependency loader/runtime `@oai/artifact-tool` yang diwajibkan skill Presentations tidak tersedia di sesi penyiapan ini. Storyboard, narasi dan script demo sudah dapat digunakan untuk latihan atau pembuatan slide di PowerPoint.
