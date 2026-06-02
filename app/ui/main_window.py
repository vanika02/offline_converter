from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Slot
from app.ui.layout_colorwidget import Color
from app.utils.file_dialogs import get_image_file, SaveFileDialog
from app.convertors.image_to_pdf import convert_image_to_pdf

# this creates a func that logs message to the console - slot is a decorator that identifies func as a slot
# @Slot()
# def say_hello():
#     print("Button clicked, wasssuppp")



# creating a class main window to start the application
# this will create QApplication to run the pyside6 code
class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.input_file = None
        self.output_file = None

        self.setWindowTitle("Offline Converter")

        save_btn = QPushButton(text="Select Image")
        save_btn.setFixedSize(100, 60)

        convert_btn = QPushButton(text="Convert")
        convert_btn.setFixedSize(100, 60)


        print("Conversion successfull")
        layout = QVBoxLayout()
        # layout.addWidget(Color("black"))
        layout.addWidget(open_btn)
        layout.addWidget(save_btn)
        layout.addWidget(convert_btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        save_btn.clicked.connect(self.select_image)
        convert_btn.clicked.connect(self.convert)

    def select_image(self):
        self.input_file = get_image_file()

        if self.input_file:
            print("Input", self.input_file)

    def convert(self):
        if not self.input_file:
            print("Please select an image")

        pdf_path = save_pdf_file()
        
        if not pdf_path:
            return

        convert_image_to_pdf(
            self.input_file,
            pdf_path
        )
