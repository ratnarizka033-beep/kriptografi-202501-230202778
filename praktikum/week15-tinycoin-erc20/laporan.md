# Laporan Praktikum Kriptografi
Minggu ke-: 15
Topik:  Implementasi tinyCoin Smart Contract ERC20
Nama: Ratna Rizka Maharani
NIM: 230202778 
Kelas: 5IKRA

---

## 1. Tujuan
Menurut saya tujuan dari praktikum ini yaitu untuk memahami konsep dasar teknologi blockchain melalui implementasi smart contract berbasis standar ERC20. jadi mahasiswa seperti sya diharapkan mampu mengembangkan token digital sederhana menggunakan bahasa pemrograman Solidity, memahami mekanisme kerja smart contract di jaringan Ethereum, serta mendokumentasikan proses pengembangan proyek menggunakan sistem kontrol versi Git. Selain itu, praktikum ini bertujuan untuk melatih mahasiswa dalam menganalisis aspek keamanan dasar pada smart contract.
---

## 2. Dasar Teori
Menurut saya blockchain yaitu teknologi buku besar terdistribusi (distributed ledger) yang mencatat transaksi secara permanen dan tidak dapat diubah. Setiap transaksi merupakan diverifikasi oleh jaringan dan disimpan dalam blok yang saling terhubung menggunakan kriptografi. Salah satu platform blockchain paling populer yakni Ethereum, yang memungkinkan pengembang membuat aplikasi terdesentralisasi (dApps) melalui smart contract.

Smart contract adalah program yang berjalan secara otomatis di atas blockchain ketika kondisi tertentu terpenuhi. Pada Ethereum, smart contract umumnya ditulis menggunakan bahasa Solidity. Salah satu standar smart contract yang paling banyak digunakan adalah ERC20, yaitu standar teknis untuk pembuatan token yang dapat dipertukarkan (fungible token). ERC20 mendefinisikan fungsi-fungsi utama sperti transfer, balanceof, dan totalsupply

Jadi dengan menggunakan standar ERC20, token yang dibuat dapat dengan mudah diintegrasikan dengan wallet, exchange, dan aplikasi blockchain lainnya. Oleh karena itu, pemahaman mengenai implementasi ERC20 menjadi bagian penting dalam pembelajaran kriptografi modern dan teknologi blockchain.

---

## 3. Alat dan Bahan
(- Python 3.12.10
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

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
- Pertanyaan 1: Apa fungsi utama ERC20 dalam ekosistem blockchain?  
Jawab: Fungsi utama ERC20 dalam ekosistem blockchain sebagai standar teknis yang mengatur bagaimana sebuah token dibuat, dikelola, dan ditransaksikan di jaringan Ethereum. Dengan adanya standar ERC20, token dapat digunakan secara konsisten oleh berbagai aplikasi, dompet digital, dan platform pertukaran tanpa perlu penyesuaian khusus, sehingga meningkatkan interoperabilitas, kemudahan integrasi, serta kepercayaan dalam pengembangan dan penggunaan aset digital.


- Pertanyaan 2: Bagaimana mekanisme transfer token bekerja dalam kontrak ERC20? 
Jawab: Jadi menurut saya mekanisme transfer token dalam kontrak ERC20 bekerja melalui fungsi transfer yang memungkinkan pemilik token mengirim sejumlah token ke alamat lain, jadi ketika fungsi ini dipanggil, kontrak akan terlebih dahulu memeriksa apakah saldo pengirim mencukupi untuk melakukan transaksi dan jika saldo mencukupi, maka jumlah token yang dikirim akan dikurangi dari saldo pengirim dan ditambahkan ke saldo penerima, kemudian transaksi tersebut dicatat secara permanen di dalam blockchain. Proses ini memastikan bahwa perpindahan token dilakukan secara aman dan transparan tanpa memerlukan pihak ketiga.

Selain itu, standar ERC20 juga menyediakan fungsi transferFrom yang memungkinkan pihak ketiga melakukan transfer token atas nama pemilik, biasanya setelah mendapatkan izin melalui fungsi approve. Mekanisme ini banyak digunakan dalam aplikasi terdesentralisasi seperti decentralized exchange (DEX) dan smart contract lainnya. Setiap transfer akan memicu event Transfer yang dapat dipantau oleh aplikasi atau pengguna, sehingga seluruh aktivitas transaksi dapat diaudit dan diverifikasi secara publik di jaringan blockchain.


- Pertanyaan 3: Apa risiko utama dalam implementasi smart contract dan bagaimana cara mitigasinya? 
Jawab: Risiko utama dalam implementasi smart contract meliputi adanya bug atau kesalahan logika pada kode, celah keamanan seperti reentrancy attack, serta kesalahan pengelolaan hak akses yang dapat dimanfaatkan oleh pihak tidak bertanggung jawab. Risiko ini dapat diminimalkan dengan menerapkan praktik pengembangan yang baik, seperti menggunakan library tepercaya (misalnya OpenZeppelin), melakukan audit kode secara menyeluruh, menulis pengujian (testing) sebelum deployment, serta menggunakan versi compiler terbaru yang sudah dilengkapi perlindungan terhadap kesalahan umum.


---

## 8. Kesimpulan
menurut saya kesimpulannya yaitu implementasi smart contract ERC20 pada proyek TinyCoin menunjukkan bahwa pembuatan token digital dapat dilakukan secara efisien dan aman dengan memanfaatkan standar yang telah tersedia, sehingga melalui penggunaan Solidity dan library OpenZeppelin, proses pengembangan menjadi lebih terstruktur serta meminimalkan risiko kesalahan keamanan. Praktikum ini memberikan pemahaman nyata mengenai cara kerja blockchain dan penerapan smart contract dalam sistem terdesentralisasi.


---

## 9. Daftar Pustaka  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  
- Antonopoulos, A. M. Mastering Ethereum. O’Reilly Media.
- Stallings, W. Cryptography and Network Security. Pearson Education.
- Trappe, W., & Washington, L. C. (2006). Introduction to Cryptography with Coding Theory (2nd ed.). Pearson.
- Singh, S. (1999). The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography. Anchor Books
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography. CRC Press.


## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit a7f9c2e
Author: Ratna Rizka Maharani <ratnarizka033@gmail.com>
Date:   Friday 02 january 2026

    week2-cryptosystem: implementasi Caesar Cipher dan laporan akhir )
```
