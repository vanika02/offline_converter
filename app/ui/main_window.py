from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QPushButton, QMessageBox
from PySide6.QtCore import Qt
from app.ui.layout_colorwidget import Color
from app.utils.file_dialogs import get_image_file, SaveFileDialog
from app.convertors.image_to_pdf import convert_image_to_pdf
import os


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.input_file = None

        self.setWindowTitle("Offline Converter")
        self.resize(500, 350)

        # title
        title_label = QLabel("Offline Image -> PDF Converter")
        title_label.setAlignment(Qt.AlignCenter)


        # file selection info
        self.file_label = QLabel("Selected file: None")
        self.file_label.setAlignment(Qt.AlignCenter)

        #buttons
        select_btn = QPushButton(text="Select Image")
        convert_btn = QPushButton(text="Convert to PDF")

        select_btn.setMinimumHeight(50)
        convert_btn.setMinimumHeight(50)

        #layout
        layout = QHBoxLayout()

        layout.addWidget(title_label)
        layout.addWidget(self.file_label)
        layout.addWidget(save_btn)
        layout.addWidget(convert_btn)

        # central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        select_btn.clicked.connect(self.select_image)
        convert_btn.clicked.connect(self.convert)

    def select_image(self):
        self.input_file = get_image_file()

        if self.input_file:
            file_name = Path(self.input_file).name 
            self.file_label.setText(f"Selecte File: {file_name}")
            # print("Input", self.input_file)

    def convert(self):
        if not self.input_file:
            print("Please select an image")
            return 

        output_dir = SaveFileDialog()
        
        if not output_dir:
            return

        image_name = Path(self.imput_file).stem 

        pdf_path = os.path.join(
            output_dir,
            f"{image_name}.pdf"
        )

        convert_image_to_pdf(
            self.input_file,
            pdf_path
        )
        if True:
            QMessageBox.information(
                self, 
                "Success", 
                "PDF created successfully"
            )

