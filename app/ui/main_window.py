from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Slot
from app.ui.layout_colorwidget import Color
from app.utils.file_dialogs import get_image_file, SaveFileDialog


# this creates a func that logs message to the console - slot is a decorator that identifies func as a slot
# @Slot()
# def say_hello():
#     print("Button clicked, wasssuppp")


def select_image(self):
    self.input_file = get_image_file()

    if self.input_file:
        print("Input", self.input_file)

def select_output(self):
    self.output_file = SaveFileDialog()

    if self.output_file:
        print("output:", self.output_file)


# creating a class main window to start the application
# this will create QApplication to run the pyside6 code
class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.input_file = None
        self.output_file = None

        self.setWindowTitle("Offline Converter")


        open_btn = QPushButton(text="Select Image")
        open_btn.setFixedSize(100, 60)

        save_btn = QPushButton(text="Select Output")
        save_btn.setFixedSize(100, 60)

        convert_btn = QPushButton(text="Convert")
        convert_btn.setFixedSize(100, 60)

        layout = QVBoxLayout()
        # layout.addWidget(Color("black"))
        layout.addWidget(btn)
        layout.addWidget(open_btn)
        layout.addWidget(save_btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        open_btn.clicked.connect(self.select_image)
        save_btn.clicked.connect(self.select_output)
        convert_btn.clicked.connect(self.convert)
