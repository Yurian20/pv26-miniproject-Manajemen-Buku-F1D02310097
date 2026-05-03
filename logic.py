from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from form_dialog import FormDialog

class Logic:
    def __init__(self, ui, db):
        self.ui = ui
        self.db = db

        self.connect_event()
        self.load_data()

    def connect_event(self):
        self.ui.btn_tambah.clicked.connect(self.tambah)
        self.ui.btn_hapus.clicked.connect(self.hapus)
        self.ui.btn_refresh.clicked.connect(self.clear)
        self.ui.table.cellClicked.connect(self.pilih)

        self.ui.act_keluar.triggered.connect(self.ui.close)
        self.ui.act_tentang.triggered.connect(self.show_about)

    def tambah(self):
        dialog = FormDialog()

        if dialog.exec():
            data = (
                dialog.kode.text(),
                dialog.judul.text(),
                dialog.pengarang.text(),
                dialog.tahun.value(),
                dialog.stok.value(),
                dialog.kategori.currentText()
            )

            self.db.insert(data)
            self.load_data()

    def load_data(self):
        self.ui.table.setRowCount(0)

        for row_data in self.db.get_all():
            row = self.ui.table.rowCount()
            self.ui.table.insertRow(row)

            for col, val in enumerate(row_data):
                self.ui.table.setItem(row, col, QTableWidgetItem(str(val)))

    def hapus(self):
        row = self.ui.table.currentRow()

        if row == -1:
            QMessageBox.warning(self.ui, "Peringatan", "Pilih data yang akan dihapus")
            return

        kode = self.ui.table.item(row, 0).text()

        msg = QMessageBox(self.ui)
        msg.setWindowTitle("Konfirmasi Hapus")
        msg.setText(f"Yakin ingin menghapus buku dengan kode '{kode}'?")
        
        msg.setIcon(QMessageBox.Question)

        # tombol
        btn_yes = msg.addButton("Ya", QMessageBox.YesRole)
        
        btn_no = msg.addButton("Tidak", QMessageBox.NoRole)

        msg.setDefaultButton(btn_no)

        msg.exec()

        if msg.clickedButton() == btn_yes:
            self.db.delete(kode)
            self.load_data()
            self.clear()

    def pilih(self, row):
        self.ui.kode.setText(self.ui.table.item(row, 0).text())
        self.ui.judul.setText(self.ui.table.item(row, 1).text())
        self.ui.pengarang.setText(self.ui.table.item(row, 2).text())
        self.ui.tahun.setValue(int(self.ui.table.item(row, 3).text()))
        self.ui.stok.setValue(int(self.ui.table.item(row, 4).text()))
        kategori = self.ui.table.item(row, 5).text()
        index = self.ui.kategori.findText(kategori)
        if index >= 0:
            self.ui.kategori.setCurrentIndex(index)

    def clear(self):
        self.ui.kode.clear()
        self.ui.judul.clear()
        self.ui.pengarang.clear()
        self.ui.tahun.setValue(1900)
        self.ui.stok.setValue(0)
        self.ui.kategori.setCurrentIndex(0)

    def show_about(self):
        QMessageBox.information(
            self.ui,
            "Tentang Aplikasi",
            "Sistem Manajemen Perpustakaan Informatika\n\n"
            "Nama: Yurian Fathur Fajar\n"
            "NIM: F1D02310097"
        )