import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Slot
from layout_colorwidget import Color
from utils.file_dialogs import get_image_file, OpenFileDialog, getSaveFileName


# this creates a func that logs message to the console - slot is a decorator that identifies func as a slot
@Slot()
def say_hello():
    print("Button clicked, wasssuppp")


def open_image():
    image_path = get_image_file()

    if image_path:
        print(image_path)

def save_image():
    pdf_path = SaveFileDialog()

    if pdf_path:
        print(pdf_path)


# creating a class main window to start the application
# this will create QApplication to run the pyside6 code
class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Offline Converter")

        btn = QPushButton(text="Click here")
        btn.setFixedSize(100, 60)

        open_btn = QPushButton(text="Open file")
        open_btn.setFixedSize(100, 60)


        layout = QVBoxLayout()
        layout.addWidget(Color("black"))
        layout.addWidget(btn)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.open_btn.clicked.connect(self.open_image)
        self.save_btn.clicked.connect(self.save_pdf)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
