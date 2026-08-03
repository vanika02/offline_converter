from PySide6.QtWidgets import QApplication, QWidget
from app.ui.main_window import MainWindow
import sys

def main():
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()

if __name__ == "__main__":
    main()
    