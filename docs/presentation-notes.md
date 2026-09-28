# Catatan presentasi: justifikasi studi Olist

Gunakan bersama Bab 1 dan bagian 2.4 laporan terbaru. Catatan ini merupakan bahan justifikasi dan jawaban dosen, bukan tambahan durasi di luar presentasi. Alur sembilan slide dan demo dalam satu video ada di [presentation-video.md](presentation-video.md), dengan target total 9:15 dan batas 10 menit. Sesuaikan kalimat dengan pemahaman sendiri.

## Konteks pasar dan business drivers

“Dua sumber eksternal membantu menjelaskan relevansi masalah. Survei DHL 2026 mencakup 29.000 pembeli online dan 5.800 bisnis di 29 negara; 20% pembeli menyatakan pengiriman lebih cepat dapat mendorong penyelesaian pembelian. OECD 2019 menjelaskan peran ulasan dan rating dalam membangun kepercayaan pengguna platform. Ini konteks pasar global, bukan survei pelanggan Olist 2016–2018.

Karena itu, saya menggunakan baseline Olist untuk menentukan prioritas operasional: investigasi rute SP–RJ, peninjauan order berisiko, dan pelaporan agregat. Keberhasilan yang dituju adalah penurunan delay rate dan evaluasi review pada populasi yang sebanding setelah intervensi. Saya belum menetapkan persentase penurunan atau penghematan biaya karena belum ada intervensi maupun data kompensasi.”

Sumber untuk Bab 1.2: [DHL Group, 2 Juni 2026](https://group.dhl.com/en/media-relations/press-releases/2026/dhl-ecommerce-trends-report-2026-old-rules-do-not-apply-in-the-age-of-ai.html) dan [OECD, Unpacking E-commerce, 2019](https://doi.org/10.1787/23561431-en). Preferensi pengiriman cepat berbeda dari keterlambatan terhadap estimasi; hubungan review–delay pada proyek tetap berupa asosiasi.

## Tujuan dan pengguna

“Prioritas studi saya adalah mendukung penurunan keterlambatan pengiriman. Baseline historisnya 8,11%, yaitu 7.826 dari 96.470 order dengan tanggal label valid. Rata-rata review per order adalah 4,2943 untuk kelompok tepat waktu dan 2,5665 untuk kelompok terlambat. Perbedaan ini menunjukkan asosiasi; belum membuktikan bahwa keterlambatan merupakan satu-satunya penyebab review rendah.

Pengguna utama adalah VP of Logistics, Head of Merchant Performance, dan manajemen eksekutif. VP of Logistics dapat memprioritaskan investigasi SP–RJ: 8.158 order dengan delay rate 15,49%. Graf ini memakai asal seller dan tujuan customer, sehingga belum menggambarkan transit paket atau menentukan lokasi hub. Model menjadi sinyal untuk peninjauan order setelah approval, belum menjadi penilaian seller atau keputusan otomatis. Dashboard eksekutif masih direncanakan.”

## Pilihan framework dan penyimpanan

“Pada dataset sekitar 120 MiB, kebutuhan cluster belum terbukti. Alasan memakai PySpark adalah pembelajaran dan integrasi ingestion, transformasi, serta MLlib dalam satu framework. Eksekusi local[4] menggunakan satu mesin; bukan demonstrasi cluster terdistribusi. pandas tetap layak sebagai alternatif lokal, dan VS Code mendukung kedua framework. Notebook graf memang menggunakan pandas dan NetworkX.

Parquet Snappy dipilih untuk tabel bertipe dan format columnar. Storage seluruh sembilan tabel turun dari 120,341 menjadi 54,236 MiB, hemat 54,93%. CSV raw dipertahankan untuk audit. Saya belum menguji percepatan kueri, sehingga rasio storage tidak saya gunakan sebagai klaim performa komputasi.”

## Grain dan batas arsitektur

“Saya memakai satu baris per order untuk fitur karena label delay berada pada order. Detail item dan payment terlebih dahulu diagregasi sebelum join. Uji ilustrasi menunjukkan join mentah kedua tabel akan menaikkan jumlah price sebesar 4,48%. Pipeline saat ini mencegah pengulangan tersebut. Rancangan dimensional mempertahankan grain item, pengiriman, pembayaran, dan review secara terpisah untuk pelaporan rinci.

Parquet sudah diimplementasikan. Warehouse adalah rancangan konseptual; NetworkX adalah library graf dalam memori; teks reviews dan audit JSON belum membentuk NoSQL document store. Server database ditunda untuk membatasi kompleksitas prototipe. Deployment berikutnya bergantung pada kebutuhan akses bersama, kueri persisten, kapasitas, dan target waktu proses. Instruksi tugas belum menetapkan deployment database fisik sebagai kewajiban tahap berikutnya.”

## Jawaban singkat untuk pertanyaan dosen

- **Mengapa Spark pada data kecil?** Untuk mempelajari dan menyatukan pipeline Spark SQL/DataFrame dan MLlib; bukan karena pandas terbukti tidak mampu. Biaya tambahan berupa Java dan konfigurasi runtime.
- **Sudah production-ready?** Masih prototipe lokal. Path, deployment, keamanan, monitoring, resource, dan performa perlu diuji sebelum produksi.
- **Mengapa belum memasang MongoDB/Neo4j?** Belum ada kebutuhan document query atau graf persisten bersama yang diuji. Library graf sudah cukup untuk eksplorasi 27 node dan 409 rute saat ini.
- **Apakah model sudah layak untuk tindakan otomatis?** Belum. Test recall 45,41%, precision 14,47%, dan terdapat 4.186 false positive. Perlu validasi temporal, analisis biaya intervensi, dan evaluasi tambahan.
- **Apakah kepuasan atau keterlambatan sudah membaik?** Belum ada intervensi. Angka merupakan baseline historis; dampak harus diukur pada populasi sebanding dengan definisi label konsisten.
- **Bagaimana dengan R$ 15,74M?** Belum digunakan sebagai pendapatan diakui. Jumlah price, payment_value, dan freight memiliki definisi/populasi berbeda; ukuran finansial perlu direkonsiliasi sebelum masuk dashboard.

## Angka dan klaim yang sudah dikoreksi

- Review 4,15 versus 1,62 diganti dengan statistik per order terverifikasi 4,2943 versus 2,5665.
- Penghematan seluruh dataset 71,64% diganti dengan 54,93%. Geolocation sendiri 71,88%.
- Narasi Colab/Google Drive diganti dengan eksekusi dan penyimpanan Windows lokal dalam folder proyek.
- Simulasi empat database diganti dengan status implementasi yang benar; deployment tahap berikutnya dinyatakan sebagai opsi.
- Potensi migrasi Spark tidak dianggap otomatis atau tanpa perubahan, dan pertumbuhan Olist ke terabyte tidak dianggap temuan dataset historis.

Rujukan teknis dan bukti perbandingan tersedia dalam laporan bagian 2.4 dan notebook terkait. Alur rekaman lengkap tersedia di docs/presentation-video.md.
