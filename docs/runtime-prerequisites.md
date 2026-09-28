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

Pilihan yang paling sesuai environment teruji adalah menyalin direktori runtime di atas dari mesin proyek asal. Jangan salin tmp, spark-local, spark-warehouse atau log. Runtime `.venv` tidak portabel; buat ulang dengan requirements.txt. Belum ada bootstrap runtime otomatis di repository.

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
