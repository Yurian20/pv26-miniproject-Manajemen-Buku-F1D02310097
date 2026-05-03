from PySide6.QtWidgets import *
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mini project - Sistem Manajemen Perpustakaan")
        self.resize(700, 550)
        # ========== MENU BAR ==========
        menu = self.menuBar()

        menu_file = menu.addMenu("File")
        menu_help = menu.addMenu("Bantuan")

        self.act_keluar = QAction("Keluar", self)
        menu_file.addAction(self.act_keluar)
        self.act_tentang = QAction("Tentang Aplikasi", self)

        menu_help.addAction(self.act_tentang)
        central = QWidget()
        central.setObjectName("centralWidget")
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # ========== JUDUL ==========
        title_label = QLabel("Sistem Manajemen Perpustakaan Informatika")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            color: #2c3e50;
            padding: 10px;
            background-color: #f0f4f8;
            border-radius: 8px;
        """)
        layout.addWidget(title_label)

        # ========== NAMA & NIM ==========
        info_label = QLabel("Nama: Yurian Fathur Fajar | NIM: F1D02310097")
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setStyleSheet("""
            color: #7f8c8d;
            font-size: 12px;
            margin-bottom: 10px;
        """)

        layout.addWidget(info_label)

        # ========== TOMBOL DI TENGAH ==========
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(15)

        self.btn_tambah = QPushButton("➕ Tambah Data")
        self.btn_tambah.setObjectName("btn_tambah")
        self.btn_tambah.setMinimumSize(120, 36)  # ukuran lebih besar

        self.btn_hapus = QPushButton("🗑 Hapus")
        self.btn_hapus.setObjectName("btn_hapus")
        self.btn_hapus.setMinimumSize(120, 36)
        
        self.btn_refresh = QPushButton("🔄 Refresh")
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.setMinimumSize(120, 36)

        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_tambah)
        btn_layout.addWidget(self.btn_hapus)
        btn_layout.addWidget(self.btn_refresh)
        btn_layout.addStretch()

        # ========== TABEL ==========
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(
            ["Kode", "Judul", "Pengarang", "Tahun", "Stok", "Kategori"]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.setAlternatingRowColors(True)

        layout.addLayout(btn_layout)
        layout.addWidget(self.table)

        central.setLayout(layout)
        self.setCentralWidget(central)