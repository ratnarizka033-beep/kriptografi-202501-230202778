# Laporan Minggu 1 - Intro CIA

# Week 1 – Intro-CIA #Peran Kriptografi

## 1. Konsep Dasar Confidentiality, Integrity, Availability (CIA)

Dalam keamanan informasi, dikenal model CIA Triad yang menjadi pilar utama dalam merancang sistem yang aman.  
Ketiga aspek ini tidak dapat dipisahkan, karena keamanan tidak cukup hanya menjaga kerahasiaan saja, tetapi juga harus memastikan keaslian serta ketersediaan informasi.

### a. Confidentiality (Kerahasiaan)  
- Definisi menjaga informasi agar tidak diakses oleh pihak yang tidak berhak.  
- Tujuan melindungi privasi dan mencegah kebocoran data sensitif.  
- Mekanisme enkripsi data, manajemen akses, autentikasi multi-faktor.  
- contoh nyata yaitu data login pada aplikasi perbankan yang dilindungi dengan enkripsi sehingga meskipun jaringan disadap, isinya tidak dapat dibaca.

### b. Integrity (Integritas)  
- Definisi memastikan informasi tetap akurat, lengkap, dan tidak dimodifikasi tanpa izin.  
- Tujuan mencegah perubahan data baik akibat serangan maupun kesalahan sistem.  
- Mekanisme dalam penggunaan hash function, checksum, version control, serta tanda tangan digital.  
- Contoh nyata file update sistem operasi diverifikasi dengan digital signature sehingga pengguna yakin file tersebut asli dari pengembang, bukan hasil modifikasi penyerang.

### c. Availability (Ketersediaan)  
- Definisi: memastikan data dan layanan tetap dapat diakses oleh pengguna yang sah kapan pun dibutuhkan.  
- Tujuan dalam menjamin kontinuitas layanan meski terjadi serangan atau gangguan.  
- Mekanisme backup, load balancing, server redundan, firewall, mitigasi DDoS.  
- Contoh nyata yaitu layanan cloud seperti Google Drive menggunakan infrastruktur global yang redundan agar tetap tersedia walaupun salah satu server down.

> Kesimpulan CIA Triad 
> Jika hanya satu aspek yang terganggu (misalnya sistem terenkripsi tapi tidak tersedia), maka keamanan informasi dianggap gagal. Oleh karena itu, sistem yang baik harus menjaga keseimbangan ketiganya.


## 2. Peran Kriptografi dalam Kehidupan Sehari-hari

Kriptografi adalah ilmu dan seni menjaga kerahasiaan pesan dengan teknik matematika. Awalnya digunakan pada masa perang (contoh: mesin Enigma Jerman pada Perang Dunia II), tetapi kini perannya sudah meluas ke hampir semua aspek kehidupan digital.

Beberapa contoh penerapan nyata:

### a. Enkripsi pada WhatsApp  
WhatsApp menggunakan end-to-end encryption (protokol Signal) untuk menjamin bahwa hanya pengirim dan penerima yang dapat membaca isi pesan. Bahkan server WhatsApp tidak memiliki kunci untuk mendekripsi pesan.

### b. SSL/TLS pada Web  
Hampir semua situs modern menggunakan protokol HTTPS. SSL/TLS mengenkripsi komunikasi antara browser dan server. Dengan demikian, data login, nomor kartu kredit, atau dokumen sensitif tidak dapat diintip pihak ketiga.

### c. Tanda Tangan Digital  
Tanda tangan digital berbasis kriptografi asimetris digunakan untuk:  
- membuktikan keaslian dokumen,  
- memastikan integritas file,  
- serta memberikan non-repudiation (pengirim tidak bisa menyangkal).  

Contohnya: dokumen kontrak elektronik, sertifikat vaksin, hingga transaksi di blockchain.

### d. Kriptografi dalam Sistem Pembayaran  
ATM, kartu kredit, dan e-wallet menggunakan enkripsi untuk melindungi PIN serta transaksi dari upaya pencurian data.

### e. Kriptografi pada Blockchain dan Cryptocurrency  
Bitcoin dan Ethereum memanfaatkan algoritma kriptografi (hashing SHA-256, digital signature dengan ECDSA) untuk menjaga keamanan transaksi tanpa otoritas pusat.


## 3. Relevansi dengan Outcome-Based Education (OBE)

Dalam kurikulum berbasis OBE, pemahaman tentang CIA Triad dan peran kriptografi memberikan learning outcome yaitu berupa:  
1. Pengetahuan mahasiswa mampu menjelaskan konsep dasar keamanan informasi.  
2. Keterampilan mahasiswa dapat mengidentifikasi ancaman dan memilih mekanisme kriptografi yang sesuai.  
3. Sikap mahasiswa memiliki kesadaran etis terkait pentingnya privasi dan keamanan digital.

Hal ini selaras dengan kebutuhan industri dan masyarakat modern yang sangat bergantung pada sistem informasi yang aman.


## 4. Kesimpulan

Model CIA Triad adalah fondasi utama keamanan informasi: menjaga kerahasiaan, keaslian, dan ketersediaan data.  
Kriptografi menjadi alat yang sangat penting untuk mendukung ketiga aspek tersebut, dari komunikasi pribadi, transaksi keuangan, hingga teknologi blockchain.  

Pemahaman dasar ini menjadi bekal awal untuk mempelajari mata kuliah Kriptografi lebih dalam, serta mendukung capaian pembelajaran dalam kurikulum Outcome-Based Education (OBE).
