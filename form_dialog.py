from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class FormDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tambah Buku")
        self.setFixedSize(350, 300)

        layout = QVBoxLayout()

        form = QFormLayout()

        self.kode = QLineEdit()
        self.judul = QLineEdit()
        self.pengarang = QLineEdit()

        self.tahun = QSpinBox()
        self.tahun.setRange(1900, 2100)

        self.stok = QSpinBox()
        self.stok.setRange(0, 1000)

        self.kategori = QComboBox()
        self.kategori.addItems(["Pemrograman", "Jaringan", "Desain"])

        form.addRow("Kode", self.kode)
        form.addRow("Judul", self.judul)
        form.addRow("Pengarang", self.pengarang)
        form.addRow("Tahun", self.tahun)
        form.addRow("Stok", self.stok)
        form.addRow("Kategori", self.kategori)

        layout.addLayout(form)

        btn_layout = QHBoxLayout()

        self.btn_simpan = QPushButton("💾 Simpan")
        self.btn_simpan.setStyleSheet("background-color: #27ae60; color: white;")
        self.btn_batal = QPushButton("❌ Batal")
        self.btn_batal.setStyleSheet("background-color: #e74c3c; color: white;")

        self.btn_simpan.setMinimumHeight(35)
        self.btn_batal.setMinimumHeight(35)

        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_simpan)
        btn_layout.addWidget(self.btn_batal)

        layout.addLayout(btn_layout)

        self.setLayout(layout)

        self.btn_simpan.clicked.connect(self.submit)
        self.btn_batal.clicked.connect(self.reject)

    def submit(self):
        if not self.kode.text() or not self.judul.text():
            QMessageBox.warning(self, "Error", "Kode & Judul wajib diisi")
            return
        
        self.accept()