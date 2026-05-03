import sqlite3
import os

class Database:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "buku.db")        
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS buku (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kode TEXT,
            judul TEXT,
            pengarang TEXT,
            tahun INTEGER,
            stok INTEGER,
            kategori TEXT
        )
        """)

    def insert(self, data):
        self.cursor.execute("""
        INSERT INTO buku (kode, judul, pengarang, tahun, stok, kategori)
        VALUES (?, ?, ?, ?, ?, ?)
        """, data)
        self.conn.commit()

    def get_all(self):
        return self.cursor.execute(
            "SELECT kode, judul, pengarang, tahun, stok, kategori FROM buku"
        ).fetchall()

    def delete(self, kode):
        self.cursor.execute("DELETE FROM buku WHERE kode=?", (kode,))
        self.conn.commit()