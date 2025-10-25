# 04 Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)

## Tujuan Pembelajaran
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menyelesaikan perhitungan sederhana terkait entropi kunci.  
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.  
3. Menghitung **unicity distance** untuk ciphertext tertentu.  
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.  
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.  

---

## Capaian Kegiatan
Pada akhir sesi ini mahasiswa menghasilkan:  
- Perhitungan manual/komputasi entropi dan unicity distance.  
- Analisis sederhana model brute force attack.  
- Laporan singkat tentang evaluasi kekuatan kunci.  
- Commit ke GitHub dengan format `week4-entropy-unicity`.  

---

## Persiapan Lingkungan
1. Buat folder berikut:  
   ```
   praktikum/week4-entropy-unicity/
   ├─ src/
   ├─ screenshots/
   └─ laporan.md
   ```
2. Gunakan Python 3.11 atau lebih baru.  
3. Materi rujukan: Stallings (2017), Bab 3.  

---

## Panduan Langkah demi Langkah

### Langkah 1 — Perhitungan Entropi
Gunakan rumus:  
\[
H(K) = \log_2 |K|
\]  
dengan \(|K|\) adalah ukuran ruang kunci.  

Contoh implementasi Python:  
```python
ic

---

## Pertanyaan Diskusi
1. Apa arti dari nilai **entropy** dalam konteks kekuatan kunci?  
2. Mengapa unicity distance penting dalam menentukan keamanan suatu cipher?  
3. Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat?  

---

## Tugas yang Dikumpulkan
1. Program Python (`src/`) berisi perhitungan:  
   - Entropi kunci.  
   - Unicity distance.  
   - Estimasi brute force attack.  
2. Screenshot hasil eksekusi program.  
3. Laporan `laporan.md` berisi:  
   - Ringkasan teori entropi & unicity distance.  
   - Hasil analisis brute force.  
   - Jawaban pertanyaan diskusi.  

Struktur akhir folder:
```
praktikum/week4-entropy-unicity/
 ├─ src/entropy_unicity.py
 ├─ screenshots/
 │   └─ hasil.png
 └─ laporan.md
```

Commit dengan pesan:  
```
week4-entropy-unicity
```

---

## Rubrik Penilaian
Mengacu pada RPS Minggu 4: **Total bobot 5% (Analisis Entropi/Unicity 3%, Laporan singkat 2%)**  

| Aspek Penilaian                | Bobot | Kriteria                                                                 |
|--------------------------------|-------|--------------------------------------------------------------------------|
| Analisis entropi & unicity     | 3%    | Perhitungan tepat, implementasi Python berjalan benar, analisis sesuai teori |
| Laporan singkat                | 2%    | Penjelasan ringkas, ada screenshot, jawaban diskusi sesuai pertanyaan     |
| Evidence Git & repo            | -     | Commit sesuai format, struktur folder rapi, laporan jelas                 |

---
