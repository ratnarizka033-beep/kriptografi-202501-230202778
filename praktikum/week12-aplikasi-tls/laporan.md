# Laporan Praktikum Kriptografi
Minggu ke-: 12
Topik: aplikasi tls (Transport Layer Security)
Nama: Ratna Rizka Maharani  
NIM: 230202778
Kelas: 5ikra

---

## 1. Tujuan
Tujuan praktikum ini menurut saya yaitu untuk memahami konsep dasar komunikasi aman menggunakan protokol Transport Layer Security (TLS) dan bagaimana TLS digunakan pada aplikasi modern seperti HTTPS. Mahasiswa diharapkan mampu menganalisis proses handshake, pertukaran kunci, serta enkripsi dan autentikasi yang terjadi selama sesi TLS berlangsung. Selain itu, mahasiswa mampu melakukan simulasi koneksi TLS menggunakan Python, mengamati sertifikat digital, dan mengevaluasi manfaat TLS dalam melindungi data.
---

## 2. Dasar Teori
Transport Layer Security (TLS) merupakan protokol keamanan standar yang digunakan untuk mengamankan komunikasi di jaringan komputer. TLS bekerja dengan memastikan tiga aspek utama: confidentiality (kerahasiaan), integrity (integritas), dan authenticity (autentikasi). Dengan TLS, data yang dikirimkan antara client dan server akan dienkripsi sehingga tidak dapat dibaca oleh pihak yang tidak berwenang.

Pada prosesnya, TLS dimulai dengan TLS Handshake, yakni fase di mana client dan server saling bertukar informasi kriptografi. Handshake mencakup pertukaran versi TLS, cipher suites, sertifikat digital server, dan pembuatan session key melalui algoritma seperti RSA atau Diffie-Hellman. Setelah handshake berhasil, komunikasi aman menggunakan symmetric encryption seperti AES.

TLS sangat penting dalam layanan berbasis web, terutama HTTPS. Sertifikat digital digunakan untuk membuktikan identitas server dan mencegah serangan man-in-the-middle. Sertifikat ini dikeluarkan oleh CA (Certificate Authority) yang dipercaya secara  global. Dengan demikian, TLS menjadi pondasi utama keamanan pada transaksi online, e-commerce, login akun, email, API, dan hampir seluruh komunikasi berbasis internet.
---

## 3. Alat dan Bahan
(- Python 3.11
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `aplikasi_tls.py` di folder `praktikum/``week12-aplikasi-tls``/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python aplikasi_tls.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- 1. Mengapa TLS penting dalam komunikasi internet?
Jawab: Transport Layer Security (TLS) sangat penting dalam komunikasi internet karena protokol ini bertugas menjaga kerahasiaan, integritas, dan autentikasi data yang dikirimkan antar perangkat. Tanpa TLS, seluruh informasi yang dikirim melalui jaringan dapat dengan mudah disadap, diubah, atau dipalsukan oleh pihak tidak bertanggung jawab (misalnya attacker yang melakukan man-in-the-middle). TLS memastikan bahwa data dienkripsi sebelum dikirim, sehingga meskipun pihak lain mampu menangkap paket tersebut, mereka tidak akan dapat membaca isi informasinya. Selain itu, TLS menyediakan mekanisme verifikasi identitas server, sehingga pengguna dapat memastikan bahwa mereka terhubung ke pihak yang benar, bukan ke penyerang. Karena hampir semua aktivitas digital—mulai dari login, transaksi e-commerce, hingga pertukaran data penting—bergantung pada keamanan komunikasi, penggunaan TLS menjadi fondasi utama keamanan internet modern.

- 2. Apa fungsi sertifikat digital dalam TLS?
Jawab: Sertifikat digital berfungsi sebagai identitas resmi suatu server atau entitas dalam proses komunikasi TLS. Sertifikat ini diterbitkan oleh Certificate Authority (CA) terpercaya dan mengandung informasi penting seperti nama domain, kunci publik, serta tanda tangan digital dari CA. Dalam proses handshake TLS, browser atau client akan memeriksa sertifikat tersebut untuk memastikan bahwa server yang dihubungi benar-benar valid dan bukan server palsu yang dibuat oleh penyerang. Jika sertifikat tidak valid atau dipalsukan, TLS akan memberikan peringatan dan menghentikan koneksi. Selain memberikan autentikasi, sertifikat digital juga menjadi dasar pertukaran kunci rahasia yang digunakan dalam proses enkripsi selama sesi komunikasi. Dengan demikian, sertifikat digital adalah elemen inti yang memungkinkan TLS bekerja secara aman dan terpercaya.

- 3. Mengapa HTTPS lebih aman dibanding HTTP?
jawab: HTTPS lebih aman dibanding HTTP karena HTTPS menggunakan protokol TLS untuk melindungi data yang dikirim dan diterima melalui jaringan. Pada HTTP biasa, data dikirim dalam bentuk plaintext tanpa enkripsi, sehingga siapa pun yang berada di jalur komunikasi dapat membaca seluruh informasi seperti password, nomor kartu kredit, atau data pribadi lainnya. Namun pada HTTPS, seluruh data dienkripsi sehingga hanya pengirim dan penerima yang dapat memahaminya. Selain enkripsi, HTTPS juga menyediakan autentikasi melalui sertifikat digital, sehingga mencegah serangan seperti spoofing atau man-in-the-middle. HTTPS juga menjaga integritas data, memastikan bahwa pesan tidak dapat diubah tanpa diketahui selama proses pengiriman. Oleh karena itu, HTTPS digunakan sebagai standar keamanan dalam aplikasi web modern dan merupakan syarat utama untuk transaksi sensitif seperti perbankan, login akun, dan e-commerce.
)
---

## 8. Kesimpulan
Berdasarkan percobaan, dapat disimpulkan bahwa TLS merupakan protokol vital dalam pengamanan komunikasi internet modern. Program Python yang dijalankan berhasil menunjukkan proses koneksi aman, pengambilan sertifikat digital, serta penggunaan enkripsi TLS. Dengan demikian, mahasiswa memahami bagaimana TLS bekerja dalam sistem nyata seperti HTTPS dan mengapa protokol ini sangat penting dalam menjaga keamanan data.

Selain itu, praktikum ini juga memperlihatkan bagaimana proses verifikasi sertifikat dan negosiasi cipher suite dilakukan secara otomatis oleh protokol, sehingga pengguna dapat memastikan integritas dan autentikasi server tanpa perlu melakukan konfigurasi manual. Melalui simulasi dan analisis hasil eksekusi program, mahasiswa dapat memahami potensi ancaman seperti serangan man-in-the-middle ketika sertifikat tidak valid, serta menyadari pentingnya peran Certificate Authority (CA) dalam ekosistem TLS. Dengan pemahaman ini, mahasiswa lebih siap menerapkan konsep keamanan jaringan pada aplikasi nyata dan mampu mengevaluasi apakah suatu koneksi benar-benar aman atau tidak.
---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )
- Shamir, A. (1979). “How to Share a Secret.” Communications of the ACM.
- Trappe, W., & Washington, L. C. (2006). Introduction to Cryptography with Coding Theory (2nd ed.). Pearson.
- Singh, S. (1999). The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography. Anchor Books
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography. CRC Press.
---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 8ac93f1c2d9a12ab4d22faa11c8e9b331f20ae77
Author: Ratna Rizka Maharani <ratnarizka033gmail.com>
Date:   12 desember 2025

    week12-aplikasi-tls: implementasi aplikasi tls (Transport Layer Security) dan laporan )
```
