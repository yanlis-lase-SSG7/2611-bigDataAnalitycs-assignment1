# Panduan rekaman Assignment I: seluruhnya di PowerPoint

[Buka PPT](../presentations/Assignment_I_Olist_2702751284.pptx). Versi terbaru terdiri dari 11 slide. Seluruh hasil demo yang sudah dijalankan masuk ke slide; tidak perlu berpindah ke VS Code saat merekam. Speaker notes menggunakan bahasa percakapan dan dapat dibaca langsung. Salinan narasi ada di [presentation-notes.md](presentation-notes.md).

Target total 9 menit 30 detik, dengan batas tugas 10 menit. Target ini belum merupakan durasi rekaman terukur. Narasi sekitar 1.238 kata membutuhkan rata-rata sekitar 130 kata per menit untuk target tersebut. Sisakan jeda singkat dan ukur saat latihan; jika bacaan lebih lambat, ringkas penjelasan daripada mempercepat seluruh video.

## Alur slide

| Slide | Isi | Target waktu |
|---|---|---|
| 1 | Analitik keterlambatan pengiriman Olist | 00:00–00:25 |
| 2 | Latar belakang masalah | 00:25–01:20 |
| 3 | Tujuan proyek dan pengguna hasil | 01:20–02:05 |
| 4 | Konteks pasar dan urgensi bisnis | 02:05–02:40 |
| 5 | Tech stack dan alasan pemilihan | 02:40–04:00 |
| 6 | Alur pipeline dan batas implementasi | 04:00–05:00 |
| 7 | Hasil ingestion dan kualitas data | 05:00–05:50 |
| 8 | Tata kelola dan perlindungan data | 05:50–06:35 |
| 9 | Hasil model dan pemilihan ambang | 06:35–07:55 |
| 10 | Hasil graf dan prioritas rute | 07:55–08:50 |
| 11 | Ringkasan validasi dan langkah berikutnya | 08:50–09:30 |

## Membaca notes tanpa menampilkannya pada rekaman

Dengan dua monitor, tampilkan Slide Show di layar yang direkam dan Presenter View di layar pribadi. Pastikan software rekaman hanya menangkap layar atau jendela Slide Show, bukan semua layar.

Dengan satu monitor, buka salinan naskah pada ponsel/perangkat kedua di dekat kamera, sementara komputer menampilkan Slide Show. Hindari merekam seluruh desktop ketika panel Notes atau Presenter View terlihat. Pilih cara yang sesuai dengan perangkat rekaman Anda.

Narasi merupakan bagian awal setiap speaker note, terpisah dari referensi dan target waktu. Referensi, label waktu, dan pemisah tidak perlu dibacakan. Ambil jeda pendek antarparagraf dan sesuaikan ungkapan dengan gaya bicara sendiri. Slide berganti manual.

Buat uji rekaman sekitar 20 detik terlebih dahulu. Putar kembali untuk memastikan hanya slide/wajah yang diinginkan tampil, notes tidak ikut terlihat, dan audio jelas. Setelah itu, rekam seluruh presentasi dalam satu video.

## Cara menjelaskan hasil demo

Slide 7, 9 dan 10 menampilkan hasil pemeriksaan ingestion, model, dan graf. Slide 11 merangkum ketiganya sebagai PASS. Sebut sebagai pemeriksaan yang sudah dijalankan sebelumnya. Tampilan tersebut bukan eksekusi live di dalam rekaman dan tidak membuktikan manfaat operasional sudah tercapai.

Angka utama: sembilan tabel, storage hemat 54,93%; RF tanpa bobot dengan threshold 0,099536 dan validation F1 0,2168; test recall 45,41%, precision 14,47%, 4.186 false positive; graf 27 node/409 rute, nasional 8,11%, SP–RJ 8.158 order/15,49%.

Script demo_assignment1.py tetap tersedia untuk pemeriksaan sebelum rekaman atau pertanyaan dosen. Tidak perlu menjalankannya dalam presentasi versi ini. Pemeriksaan membaca ringkasan agregat tersimpan, bukan mengulang seluruh ingestion/pelatihan.

## Sebelum pengumpulan

1. Latihan seluruh narasi; jika durasinya melewati 10 menit, ringkas kalimat sambil mempertahankan angka, alasan pilihan teknologi dan batas hasil.
2. Periksa keterbacaan slide, audio dan durasi video final.
3. Mahasiswa melengkapi deklarasi AI dan mengekspor PDF laporan setelah finalisasi Word.

PPT diperbarui melalui Microsoft PowerPoint lokal, sesuai persetujuan pengguna. Notebook, raw data dan laporan Word tidak berubah.
