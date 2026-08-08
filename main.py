from PySide6.QtWidgets import QApplication, QWidget
from app.logging_config import setup_logging
from app.ui.main_window import MainWindow
import sys

def main():

    setup_logging()

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
