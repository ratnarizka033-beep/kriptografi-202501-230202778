# Laporan Praktikum Kriptografi
Minggu ke-: 13  
Topik: TinyChain – Proof of Work (PoW)
Nama: RATNA RIZKA MAHARANI 
NIM: 230202778  
Kelas: 5IKRA

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
Tujuan dari praktikum ini menurut saya agar memberikan pemahaman yang komprehensif mengenai konsep dasar blockchain dengan fokus pada peran fungsi hash dan mekanisme Proof of Work (PoW). Melalui praktikum ini, mahasiswa diharapkan mampu mengimplementasikan blockchain sederhana menggunakan bahasa pemrograman Python, memahami proses mining blok, serta menganalisis bagaimana PoW berkontribusi terhadap keamanan dan keandalan sistem cryptocurrency. Selain itu, praktikum ini juga bertujuan melatih kemampuan analisis mahasiswa terhadap kelebihan dan keterbatasan PoW dalam penerapan nyata.
---

## 2. Dasar Teori
Blockchain merupakan sebuah teknologi buku besar terdistribusi (distributed ledger) yang menyimpan data dalam bentuk blok-blok yang saling terhubung satu sama lain. Setiap blok berisi data transaksi, timestamp, hash dari blok sebelumnya, dan hash milik blok itu sendiri. Keterkaitan antarblok ini membentuk sebuah rantai (chain) yang bersifat immutable, artinya data yang telah tersimpan tidak dapat diubah tanpa memodifikasi seluruh blok setelahnya.

Fungsi hash kriptografis adalah komponen utama dalam blockchain. Fungsi hash seperti SHA-256 memiliki sifat one-way, collision resistant, dan avalanche effect, di mana perubahan kecil pada input akan menghasilkan perubahan besar pada output hash. Sifat-sifat ini menjadikan fungsi hash sangat efektif dalam menjaga integritas data dan mendeteksi adanya manipulasi pada isi blok.

Proof of Work (PoW) yaitu mekanisme konsensus yang digunakan untuk memvalidasi transaksi dan menambahkan blok baru ke dalam blockchain. Dalam PoW, penambang harus mencari nilai nonce yang menghasilkan hash dengan pola tertentu (misalnya diawali dengan sejumlah nol). Proses ini membutuhkan daya komputasi yang besar sehingga menyulitkan pihak tidak bertanggung jawab untuk memalsukan transaksi. Semakin tinggi tingkat kesulitan (difficulty), semakin aman blockchain, namun dengan konsekuensi meningkatnya konsumsi energi.

Selain itu, mekanisme Proof of Work juga berperan penting dalam menjaga konsistensi dan kepercayaan pada jaringan blockchain yang bersifat terdesentralisasi. Karena tidak ada otoritas pusat yang mengatur validasi transaksi, PoW memastikan bahwa setiap blok baru hanya dapat ditambahkan setelah melalui proses komputasi yang dapat diverifikasi oleh seluruh node dalam jaringan. Hal ini membuat konsensus tercapai secara kolektif, di mana mayoritas node sepakat terhadap rantai blok yang valid. Dengan demikian, PoW tidak hanya berfungsi sebagai alat validasi teknis, tetapi juga sebagai mekanisme ekonomi dan keamanan yang mencegah serangan seperti manipulasi data dan double spending.


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
1. Membuat file `tinychain.py` di folder `praktikum/week13-tinychain/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python tinychain.py`.)

---

## 5. Source Code
Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")
```

---

### Langkah 2 — Membuat Blockchain
```python
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Uji coba blockchain
my_chain = Blockchain()
print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))
```


---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/tinychain.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- 1: Mengapa fungsi hash sangat penting dalam blockchain?  
Jawab: Fungsi hash sangat penting dalam blockchain karena berperan utama dalam menjaga integritas dan keutuhan data pada setiap blok. Setiap blok memiliki nilai hash unik yang dihasilkan dari data transaksi, timestamp, hash blok sebelumnya, dan nonce. Jika terjadi perubahan sekecil apa pun pada isi blok, nilai hash akan berubah secara signifikan, sehingga ketidaksesuaian tersebut dapat langsung terdeteksi oleh node lain di jaringan. Mekanisme ini membuat data dalam blockchain sulit dimanipulasi tanpa diketahui.

Oleh karena itu, fungsi hash juga menjadi penghubung antarblok yang membentuk rantai blockchain. Hash dari blok sebelumnya disimpan di dalam blok berikutnya, sehingga menciptakan keterkaitan yang kuat antarblok. Struktur ini memastikan bahwa untuk mengubah satu blok, penyerang harus mengubah seluruh blok setelahnya, yang membutuhkan daya komputasi sangat besar. Dengan sifat one-way dan collision resistant, fungsi hash mendukung keamanan transparansi, dan keandalan blockchain dalam lingkungan terdesentralisasi.


- 2: Bagaimana Proof of Work mencegah double spending?  
Jawab: Proof of Work mencegah double spending dengan cara-> mewajibkan setiap transaksi untuk divalidasi melalui proses komputasi yang kompleks sebelum dapat dimasukkan ke dalam sebuah blok. Setelah transaksi dikonfirmasi dan blok berhasil ditambang, transaksi tersebut menjadi bagian dari blockchain yang bersifat permanen dan tidak dapat diubah. Jika seseorang mencoba menggunakan koin yang sama untuk dua transaksi berbeda, jaringan akan menolak transaksi kedua karena catatan transaksi sebelumnya sudah tercatat dan diverifikasi oleh mayoritas node dalam jaringan.

Selain itu, untuk mengubah atau membatalkan transaksi yang sudah tercatat, penyerang harus menambang ulang blok tersebut beserta seluruh blok setelahnya dengan kecepatan yang melebihi jaringan secara keseluruhan. Hal ini berarti penyerang harus menguasai sebagian besar kekuatan komputasi (51% attack), yang secara praktis sangat sulit dan membutuhkan biaya yang sangat besar. Dengan demikian, Proof of Work menciptakan hambatan teknis dan ekonomi yang efektif dalam mencegah terjadinya double spending pada sistem blockchain.


- 3: Apa kelemahan dari PoW dalam hal efisiensi energi?
Jawab: Kelemahan utama Proof of Work dalam hal efisiensi energi adalah tingginya konsumsi daya listrik yang dibutuhkan untuk melakukan proses mining. Penambang harus menjalankan perhitungan kriptografis secara terus-menerus untuk menemukan nilai nonce yang sesuai dengan tingkat kesulitan tertentu, sehingga membutuhkan perangkat keras berdaya tinggi dan energi yang besar. Pada jaringan blockchain berskala besar, aktivitas ini dapat menyebabkan pemborosan energi yang signifikan, meningkatkan biaya operasional, serta menimbulkan dampak lingkungan seperti emisi karbon. Selain itu adanya kebutuhan energi yang tinggi juga dapat memicu sentralisasi mining, karena hanya pihak dengan sumber daya besar yang mampu berpartisipasi secara efektif.

)
---

## 8. Kesimpulan
Menurut saya dari praktikum ini dapat disimpulkan bahwa fungsi hash dan Proof of Work merupakan komponen penting dalam keamanan blockchain. Implementasi TinyChain menunjukkan PoW dalam menjaga integritas data, meskipun memiliki kelemahan dari sisi efisiensi energi.

Selain itu, praktikum ini memberikan pemahaman nyata mengenai bagaimana proses mining bekerja dan mengapa blockchain sulit untuk dimanipulasi. Melalui simulasi sederhana TinyChain, dapat dilihat bahwa perubahan kecil pada data akan memengaruhi seluruh rantai blok sehingga membutuhkan usaha komputasi yang sangat besar untuk melakukan pemalsuan. Hal ini menegaskan bahwa meskipun Proof of Work memiliki keterbatasan dalam konsumsi energi, mekanisme ini tetap efektif dalam menjamin keamanan, keandalan, dan kepercayaan pada sistem blockchain.

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
commit abcdef123456
Author: Ratna Rizka Maharani <ratnarizka033@gmail.com>
Date: saturday, 13 desember 2025 pukul 14.57

    week13-tinychain: implementasi tinychain dan laporan )
```
