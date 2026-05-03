# Sistem Manajemen Perpustakaan Informatika

Aplikasi **Sistem Manajemen Perpustakaan Informatika** merupakan mini project untuk mata kuliah Pemrograman Visual yang bertujuan untuk mengelola data buku secara efisien. Aplikasi ini dibangun dengan antarmuka pengguna (GUI) yang sederhana dan menerapkan konsep *Separation of Concerns* untuk memisahkan tampilan, logika, dan database.

---

## Deskripsi Proyek
Aplikasi ini digunakan untuk mengelola data buku seperti kode buku, judul, pengarang, tahun, stok, dan kategori. Data disimpan secara lokal menggunakan SQLite sehingga tetap tersimpan meskipun aplikasi ditutup.

**Fitur Utama:**
* **Tambah Data:** Menambahkan data buku melalui dialog form terpisah.
* **Tampil Data:** Menampilkan seluruh data buku dalam tabel.
* **Hapus Data:** Menghapus data buku dengan konfirmasi.
* **Refresh Data:** Memuat ulang data dari database.
* **Validasi Input:** Memastikan data tidak kosong sebelum disimpan.
* **Styling Modern:** Menggunakan file QSS untuk tampilan yang lebih menarik.

---

## Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python 3.x
* **Framework GUI:** PySide6 (Qt for Python)
* **Basis Data:** SQLite3
* **Styling:** Qt Style Sheets (QSS)

---

## Struktur Proyek
Proyek ini dibagi menjadi beberapa file untuk memudahkan pengelolaan:

* `main.py`  
  Sebagai entry point aplikasi dan menjalankan program.

* `database.py`  
  Mengelola koneksi database dan operasi CRUD (Create, Read, Delete).

* `ui.py`  
  Mengatur tampilan utama aplikasi seperti tabel, tombol, dan menu.

* `form_dialog.py`  
  Mengatur form input data dalam dialog terpisah.

* `logic.py`  
  Mengatur alur program dan menghubungkan UI dengan database.

* `style.qss`  
  Mengatur tampilan visual aplikasi.

---
## Cara Menjalankan
1.  **Pastikan Python Terinstal:**
    Unduh dan instal Python dari [python.org](https://www.python.org/).

2.  **Instal Library PySide6:**
    Buka terminal atau command prompt, lalu jalankan perintah berikut:
    ```bash
    pip install PySide6
    ```

3.  **Jalankan Aplikasi:**
    Navigasikan terminal ke folder project, lalu jalankan:
    ```bash
    python main.py
    ```

## Identitas Pengembang
* **Nama:** YURIAN FATHUUR FAJAR
* **NIM:** F1D02310097
* **Program Studi:** Teknik Informatika
* **Universitas:** Universitas Mataram