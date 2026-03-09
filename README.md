# 🛒 Mini Market - Data Market App

Aplikasi manajemen barang sederhana berbasis CLI (Command Line Interface) yang menggunakan Python dan MySQL. Dibuat sebagai bahan belajar Python untuk pengelolaan data toko mini market.

---

## 📦 Fitur

- ✅ **Tambah Barang** — Menambahkan data barang baru ke database
- 📋 **Cek Barang** — Menampilkan semua barang yang tersedia beserta harga dan stok
- 🗑️ **Hapus Barang** — Menghapus data barang berdasarkan kode barang
- 🚪 **Keluar Program** — Menghentikan program dengan animasi countdown

---

## 🗂️ Struktur Proyek

```
data_market/
│
├── warung.py           # File utama, entry point aplikasi
└── services/
    ├── db.py           # Koneksi & operasi database MySQL
    └── libs.py         # Fungsi utilitas (welcome message, exit)
```

---

## ⚙️ Prasyarat

Pastikan kamu sudah menginstall:

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)
- Library `mysql-connector-python`

Install library dengan:

```bash
pip install mysql-connector-python
```

---

## 🗄️ Setup Database

1. Buka MySQL dan buat database baru:

```sql
CREATE DATABASE mini_market;
```

2. Buat tabel `tbl_barang`:

```sql
USE mini_market;

CREATE TABLE tbl_barang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kode_barang VARCHAR(50) NOT NULL,
    nama_barang VARCHAR(100) NOT NULL,
    harga_barang INT NOT NULL,
    stok_barang INT NOT NULL
);
```

3. Sesuaikan konfigurasi koneksi di `services/db.py` jika perlu:

```python
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',        # isi dengan password MySQL kamu
    database='mini_market'
)
```

---

## ▶️ Cara Menjalankan

```bash
python warung.py
```

---

## 📋 Menu Aplikasi

```
menu:

1. Tambah Barang
2. Check Barang
3. Kembali
4. Hapus Barang

silahkan pilih:
```

---

## 👤 Author

**Rafie** — Semester 6, belajar Python 🐍
