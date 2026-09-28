# Panduan rekaman Assignment I: seluruhnya di PowerPoint

[Buka PPT](../presentations/Assignment_I_Olist_2702751284.pptx). Versi terbaru terdiri dari 11 slide. Seluruh hasil demo yang sudah dijalankan masuk ke slide; tidak perlu berpindah ke VS Code saat merekam. Speaker notes menggunakan bahasa percakapan dan dapat dibaca langsung. Salinan narasi ada di [presentation-notes.md](presentation-notes.md).

Target total 9 menit 10 detik, dengan batas tugas 10 menit. Target ini belum merupakan durasi rekaman terukur. Sekitar 1.040 kata narasi menyediakan ruang untuk jeda singkat; latihan dengan stopwatch tetap diperlukan.

## Alur slide

| Slide | Isi | Target waktu |
|---|---|---|
| 1 | Analitik keterlambatan pengiriman Olist | 00:00–00:20 |
| 2 | Latar belakang masalah | 00:20–01:10 |
| 3 | Tujuan proyek dan pengguna hasil | 01:10–01:55 |
| 4 | Konteks pasar dan urgensi bisnis | 01:55–02:30 |
| 5 | Tech stack dan alasan pemilihan | 02:30–03:40 |
| 6 | Alur pipeline dan batas implementasi | 03:40–04:40 |
| 7 | Hasil ingestion dan kualitas data | 04:40–05:40 |
| 8 | Tata kelola dan perlindungan data | 05:40–06:20 |
| 9 | Hasil model dan pemilihan ambang | 06:20–07:30 |
| 10 | Hasil graf dan prioritas rute | 07:30–08:25 |
| 11 | Ringkasan validasi dan langkah berikutnya | 08:25–09:10 |

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
