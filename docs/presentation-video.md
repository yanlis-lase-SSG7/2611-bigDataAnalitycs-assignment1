# Panduan rekaman Assignment I: seluruhnya di PowerPoint

[Buka PPT](../presentations/Big%20Data%20Analytics%20-%20Laporan%202702751284.pptx). Versi terbaru terdiri dari 11 slide dengan desain navy–teal dan sudah memuat arsitektur data lake, empat grafik EDA, serta hasil tiga notebook dan demo yang dijalankan. Seluruh penjelasan dapat dilakukan di PowerPoint, tanpa berpindah ke VS Code. Salinan speaker notes ada di [presentation-notes.md](presentation-notes.md).

Target total 9 menit 30 detik, dengan batas tugas 10 menit. Narasi sekitar 1.260 kata memerlukan sekitar 133 kata per menit tanpa jeda; untuk memberi ruang jeda dan pergantian slide, latihan pada laju sekitar 140 kata per menit. Ini perencanaan, bukan durasi rekaman terukur. Jika latihan melewati 10 menit, ringkas contoh dan pengulangan angka, bukan mempercepat semua kalimat.

## Alur slide

| Slide | Isi | Target waktu |
|---|---|---|
| 1 | Analitik keterlambatan pengiriman Olist | 00:00–00:25 |
| 2 | Latar belakang masalah | 00:25–01:20 |
| 3 | Tujuan proyek dan pengguna hasil | 01:20–02:05 |
| 4 | Distribusi order dan definisi keterlambatan | 02:05–02:50 |
| 5 | Tech stack dan alasan pemilihan | 02:50–04:00 |
| 6 | Arsitektur data lake dan batas implementasi | 04:00–05:00 |
| 7 | Hasil ingestion dan kualitas data | 05:00–05:50 |
| 8 | Profil null dan tata kelola data | 05:50–06:35 |
| 9 | Hasil model dan pemilihan ambang | 06:35–07:55 |
| 10 | Wilayah berisiko dan prioritas rute | 07:55–08:50 |
| 11 | Ringkasan validasi dan langkah berikutnya | 08:50–09:30 |

## Membaca notes tanpa menampilkannya pada rekaman

Dengan dua monitor, tampilkan Slide Show di layar yang direkam dan Presenter View di layar pribadi. Pastikan software rekaman hanya menangkap layar atau jendela Slide Show, bukan semua layar.

Dengan satu monitor, buka salinan naskah pada ponsel/perangkat kedua di dekat kamera, sementara komputer menampilkan Slide Show. Hindari merekam seluruh desktop ketika panel Notes atau Presenter View terlihat. Pilih cara yang sesuai dengan perangkat rekaman Anda.

Narasi merupakan bagian awal setiap speaker note, terpisah dari referensi dan target waktu. Referensi, label waktu, dan pemisah tidak perlu dibacakan. Ambil jeda pendek antarparagraf dan sesuaikan ungkapan dengan gaya bicara sendiri. Slide berganti manual.

Buat uji rekaman sekitar 20 detik terlebih dahulu. Putar kembali untuk memastikan hanya slide/wajah yang diinginkan tampil, notes tidak ikut terlihat, teks slide terbaca pada resolusi video, dan audio jelas. Setelah itu, rekam seluruh presentasi dalam satu video. Jika sudah ada video versi PPT lama, rekam ulang bagian yang berubah atau buat satu video baru agar isi video dan laporan final tetap sama.

## Cara menjelaskan hasil demo

Slide 4 menegaskan perbedaan populasi semua status dan delivered berlabel. Slide 6 membedakan prototipe lokal dari rancangan cluster. Slide 8 menampilkan profil null terukur; slide 10 membedakan delay menurut state customer dari rute seller–customer. Slide 7, 9 dan 10 juga menyampaikan hasil ingestion, model, dan graf. Slide 11 merangkum pemeriksaan sebagai PASS. Semua hasil sudah dijalankan sebelumnya; gambar pada PPT bukan eksekusi live saat rekaman dan tidak membuktikan manfaat operasional sudah tercapai.

Angka utama: 99.441 semua status, 96.470 delivered berlabel, 7.826 delayed (8,11%); sembilan tabel dan storage hemat 54,93%; null judul/teks review 88,34%/58,70%; RF tanpa bobot dengan threshold 0,099536 dan validation F1 0,2168; test recall 45,41%, precision 14,47%, 4.186 false positive; graf 27 node/409 rute, SP–RJ 8.158 order/15,49%.

Script demo_assignment1.py tetap tersedia untuk pemeriksaan sebelum rekaman atau pertanyaan dosen. Tidak perlu menjalankannya dalam presentasi versi ini. Pemeriksaan membaca ringkasan agregat tersimpan, bukan mengulang seluruh ingestion/pelatihan.

## Sebelum pengumpulan

1. Latihan seluruh narasi; jika durasinya melewati 10 menit, ringkas kalimat sambil mempertahankan angka, alasan pilihan teknologi dan batas hasil.
2. Periksa keterbacaan slide, audio dan durasi video final.
3. Mahasiswa meninjau dan melengkapi deklarasi AI. Pastikan video dan berkas yang dikirim memakai PPT dan laporan final yang sama; PDF laporan saat ini berjumlah 24 halaman.

PPT diedit dari versi proyek yang sudah ada dan hasilnya diperiksa melalui ekspor PDF PowerPoint lokal. Notebook, raw data dan laporan Word tidak diubah dalam persiapan video ini.
