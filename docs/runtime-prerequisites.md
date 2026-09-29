# Runtime Windows lokal

Environment yang telah menjalankan notebook: Python 3.11, PySpark 4.0.4, Microsoft OpenJDK 17, dan native helpers Hadoop Windows 3.3.6. Dependensi Python dicatat dalam requirements.txt. Runtime tidak masuk Git karena besar dan spesifik mesin.

Struktur yang diperiksa sel konfigurasi notebook:

```text
.runtime/
  jdk-*/bin/java.exe
  hadoop/bin/winutils.exe
  hadoop/bin/hadoop.dll
  spark-home/bin/
  spark-home/jars/
```

## Setup otomatis untuk perangkat dosen

Gunakan Windows x64 dan Python 3.11 64-bit. Dari root proyek, setelah membuat `.venv` dan menginstal requirements.txt:

```powershell
.\.venv\Scripts\python.exe setup_runtime.py
.\.venv\Scripts\python.exe -m ipykernel install --user --name bda-local --display-name "BDA Local (Python 3.11)"
```

Script menyiapkan runtime saja, tidak mengunduh dataset atau menjalankan analisis notebook. Tidak mengubah PATH sistem dan tidak membutuhkan instalasi Java global. Setup awal membutuhkan internet dan ruang disk untuk arsip Java, runtime, serta staging Spark; unduhan Java sekitar 187 MB, di luar dependensi pip. `.venv` tidak portabel; buat ulang dengan requirements.txt.

- Java: Microsoft OpenJDK 17.0.20.1, ZIP Windows x64 dari https://aka.ms/download-jdk/microsoft-jdk-17.0.20.1-windows-x64.zip. SHA-256: `3d9006956fc8af5601cd24ffc4f468bef48279c7ebd8171b9bdf90d0aabfbf1f`, dicocokkan dengan checksum penerbit. Sumber: https://learn.microsoft.com/en-us/java/openjdk/download.
- Helper Hadoop: versi 3.3.6, diunduh dari commit tetap `7386986d5d8a079b5cd4464f4599766dd27e7d13` pada repository cdarlint/winutils. Checksum di tabel bawah tetap berlaku.
- Spark: bin/jars disalin dari package PySpark 4.0.4 yang diinstal melalui requirements.txt; checksum setiap berkas diperiksa terhadap metadata RECORD package sebelum launcher diperbaiki. RECORD memeriksa konsistensi instalasi, bukan tanda tangan penerbit.
- Berkas runtime dicatat dengan SHA-256 dalam `.runtime/setup-manifest.json`, kemudian Java, versi Spark, dan tulis/baca lima baris Parquet diuji. Manifest memeriksa konsistensi lokal dan tidak menggantikan checksum sumber yang tersemat.

Jika setup diulang, runtime yang telah tercatat diperiksa dan diuji kembali tanpa mengunduh. Gunakan `setup_runtime.py --check` untuk pemeriksaan tanpa instalasi. Berkas runtime lama yang berbeda tidak ditimpa: script berhenti dan menunjukkan folder yang perlu dipindahkan/diubah namanya terlebih dahulu. Jika unduhan terputus, jalankan ulang; checksum gagal menghentikan instalasi. Jalankan setup ketika notebook/kernel Spark sedang tidak digunakan.

Notebook tetap perlu dijalankan berurutan 01, 02, 03 setelah sembilan CSV tersedia di datasets_raw. macOS/Linux/ARM64/Colab belum didukung oleh setup ini.

## Paket lampiran untuk dosen

Sertakan notebooks/ (tiga notebook dan README), README.md, requirements.txt, setup_runtime.py, run_local_notebooks.py, demo_assignment1.py, docs/runtime-prerequisites.md, datasets_raw/ (sembilan CSV dengan sumber/ketentuan dataset), serta laporan CSV/JSON kecil dari outputs_ml_graph. Jangan sertakan .venv, .runtime, .git, cache, backup atau hasil Parquet/fitur besar; hasil tersebut dibuat kembali. ZIP dan runtime tetap di-ignore dari Git.

Sumber helper yang dicatat pada mesin asal:

| Berkas | Sumber | SHA-256 |
|---|---|---|
| winutils.exe | https://raw.githubusercontent.com/cdarlint/winutils/master/hadoop-3.3.6/bin/winutils.exe | 496a591eb1e67df2a620f710d529ba6ddfe1c19149e6647cc4e320bb0efd8553 |
| hadoop.dll | https://raw.githubusercontent.com/cdarlint/winutils/master/hadoop-3.3.6/bin/hadoop.dll | d7ab36a68518748cef142be2da5069b4c763c2cd764c1d2e6ac48c7200405be3 |

Ini helper pihak ketiga; checksum merekam berkas yang diuji, bukan jaminan keamanan atau dukungan resmi Apache. Periksa checksum jika memulihkan berkas tersebut.

Spark lokal memakai launcher Spark 4.0.4 yang diperbaiki pada `bin/spark-class2.cmd` agar path launcher output dengan spasi dibaca dengan:

```bat
for /f "usebackq tokens=*" %%i in ("%LAUNCHER_OUTPUT%") do (
  set SPARK_CMD=%%i
)
del "%LAUNCHER_OUTPUT%"
```

Jangan menganggap clone siap menjalankan pipeline sebelum dataset dan runtime tersedia. Notebook mengatur JAVA_HOME, HADOOP_HOME, SPARK_HOME, lokasi temporary files dan interpreter Python pada proses kernel; tidak memerlukan pengubahan PATH sistem. Eksekusi pada OS lain atau cluster memerlukan adaptasi tersendiri.
