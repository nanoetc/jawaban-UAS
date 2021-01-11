# UAS Bahasa Pemrograman 

bagus tri handono

312010170

20.TI.B1

file yang dibutuhkan ![tampilan](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/gambar/tampilan.png)
[file main.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/main.py)
[file daftar_nilai.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/model/daftar_nilai.py)
[file input_nilai.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/view/input_nilai.py)
[file view_nilai.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/view/input_nilai.py)

![file main.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/gambar/main.png)
penjelasannya 
karena kita akan memanggil banyak module di beberapa folder maka kita gunakan perintah 
**from (nama folder.namafile) import (nama fungsi)** karena kita akan memanggil semua fungsi maka kita akan menggunakan 
tanda * untuk memanggil semua fungsi

![file daftar_nilai.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/gambar/daftar_nilai.png)
pada [file daftar_nilai.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/model/daftar_nilai.py)kita buat fungsi 
ubah hapus dan keluar,yang nantinya akan dipanggil pada [file main.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/main.py)

![file input_nilai.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/gambar/input_nilai.png)
pada [file input_nilai.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/view/input_nilai.py) kita tambahkan fungsi tambah
agar pada [file main.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/main.py) fungsi tambah dapat digunakan dan tidak error

![file view_nilai.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/gambar/view_nilai.png)
pada [file view_nilai.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/view/input_nilai.py) kita menambahkan fungsi lihat,dan cari
agar pada [file main.py](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/main.py) fungsi tambah dapat digunakan dan tidak error

untuk tampilan file setelah dieksekusi adalah seperti dibawah ini
![minta input user](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/gambar/tambah.png)
pada tampilan ini kita bisa liat jika program meminta masukkan dari user dan program ini tidak akan berhenti jika tidak kita hentikan dengan 
memberikan input huruf **K** dan ada beberapa input yang dapat kita berikan kepada program agar program tetap berjalan seperti T(tambah),L(lihat)
U(ubah),H(hapus),C(cari).K(keluar).untuk menu pertama kita gunakan T(tambah).

![menu ubah](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/gambar/ubah.png)
pada menu ini kita dapat mengubah isi data dari input yang telah kita berikan sebagai contoh saya telah mengubah nama dari **tri** ke **handono**

untuk menu L(lihat) tidak perlu saya jelaskan karena setiap kali ada perubahan data maka agar data tersebut berhasil terupdate maka kita gunakan menu L(lihat)

![menu cari](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/gambar/cari.png)
pada menu ini kita dapat menampilkan data yang kita cari pada data yeng tersimpan seperti contoh saya mencarikan nama maka muncul nama-nama yang telah kita inputkan
menu ini berguna saat kita lupa data apa saja yang telah kita input dan ingin kita ubah

![menu hapus](https://github.com/nanoetc/jawaban-UAS/blob/master/pythonProject/gambar/hapus.png)
pada  menu ini kita dapat menghapus data yang tidak kita ingin kan pada pada data atau kita salah input maka seperti contoh saya menghapus nim 312010171 maka data yang
dibelakang nim akan ikut terhapus karena pada blok program tadi telah kita buat jika kita menghapus salah satu perwakilan data seperti nim maka data yang dibelakangnya 
akan ikut tehapus.

jika ingin melihat file nya lebih jelas anda dapat menklik tulisan bercetak biru di setiap blok program 

sekian penjelasan dari saya.
