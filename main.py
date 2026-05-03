import sys
import os 
from PySide6.QtWidgets import QApplication
from ui import UI
from logic import Logic
from database import Database

if __name__ == "__main__":
    app = QApplication(sys.argv)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    qss_path = os.path.join(current_dir, "style.qss")
    
    with open(qss_path, "r") as f:
        style = f.read()
        app.setStyleSheet(style)

    ui = UI()
    db = Database()
    logic = Logic(ui, db)

    ui.show()
    sys.exit(app.exec())