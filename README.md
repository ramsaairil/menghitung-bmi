# ⚖️ BMI Calculator

Aplikasi web sederhana dan elegan untuk menghitung **Indeks Massa Tubuh (BMI)** secara instan, dilengkapi dengan visualisasi skala BMI dan rekomendasi kesehatan yang personal.

Dibangun menggunakan **Python** + **Streamlit** dengan desain dark-mode yang modern.

---

## ✨ Fitur

- 🧮 **Kalkulasi BMI real-time** — Hitung BMI hanya dengan memasukkan berat dan tinggi badan
- 🎨 **Kategori berwarna** — Hasil tampil dalam kartu berwarna sesuai kategori (kurus, normal, gemuk, obesitas)
- 📊 **Visualisasi skala BMI** — Posisi BMI Anda ditampilkan di atas track berwarna gradient
- ⚖️ **Rentang berat ideal** — Dihitung otomatis berdasarkan tinggi badan Anda
- 💡 **Rekomendasi personal** — 4 saran kesehatan spesifik per kategori BMI
- 🎈 **Animasi** — Balon muncul jika berat badan Anda ideal!
- 🌙 **Dark mode** — Desain gelap elegan, nyaman di mata

---

## 📸 Tangkapan Layar

> Buka `http://localhost:8501` setelah menjalankan aplikasi.

| Tampilan Awal | Hasil BMI Normal | Hasil BMI Obesitas |
|---|---|---|
| Input berat & tinggi | Kartu hijau + rekomendasi | Kartu merah + peringatan |

---

## 🚀 Cara Menjalankan

### 1. Prasyarat

Pastikan **Python 3.8+** telah terinstall di sistem Anda.

```bash
python --version
```

### 2. Clone Repositori

```bash
git clone https://github.com/username/menghitung-bmi.git
cd menghitung-bmi
```

### 3. Install Dependensi

```bash
pip install streamlit pillow
```

atau menggunakan `python -m pip`:

```bash
python -m pip install streamlit pillow
```

### 4. Jalankan Aplikasi

```bash
streamlit run "main..py"
```

atau:

```bash
python -m streamlit run "main..py"
```

### 5. Buka di Browser

Akses aplikasi di: **http://localhost:8501**

---

## 📂 Struktur Proyek

```
menghitung-bmi/
├── main..py       # File utama aplikasi Streamlit
├── bmi.png        # Aset gambar (legacy)
└── README.md      # Dokumentasi ini
```

---

## 🧮 Rumus BMI

$$BMI = \frac{\text{Berat Badan (kg)}}{\text{Tinggi Badan (m)}^2}$$

### Kategori BMI (WHO)

| Nilai BMI       | Kategori                  |
|-----------------|---------------------------|
| < 18.5          | Kekurangan Berat Badan    |
| 18.5 – 24.9     | Berat Badan Ideal ✅       |
| 25.0 – 29.9     | Kelebihan Berat Badan     |
| ≥ 30.0          | Obesitas                  |

> ⚠️ BMI adalah indikator awal. Konsultasikan dengan tenaga medis untuk penilaian kesehatan yang komprehensif.

---

## 🛠️ Teknologi

| Teknologi | Versi | Keterangan |
|---|---|---|
| [Python](https://python.org) | 3.8+ | Bahasa pemrograman utama |
| [Streamlit](https://streamlit.io) | 1.x | Framework web app Python |
| [Pillow](https://python-pillow.org) | 10.x+ | Pemrosesan gambar |
| CSS (custom) | — | Styling dark-mode & glassmorphism |
| Google Fonts (Inter) | — | Tipografi modern |

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah **MIT License** — bebas digunakan, dimodifikasi, dan didistribusikan.

---

<div align="center">
  Dibuat dengan ❤️ menggunakan <a href="https://streamlit.io">Streamlit</a>
</div>