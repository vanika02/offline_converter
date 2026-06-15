from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox, QComboBox
from PySide6.QtCore import Qt
from pathlib import Path
from app.ui.layout_colorwidget import Color
from app.utils.file_dialogs import get_image_file, SaveFileDialog
from app.convertors.image_to_pdf import convert_image_to_pdf
from app.ui.widgets.title_label import TitleLabel
from app.ui.widgets.file_label import FileLabel
from app.ui.widgets.action_buttons import SelectButton, ConvertButton
from app.ui.styles import TITLE_LABEL, FILE_LABEL, SELECT_BUTTON, CONVERT_BUTTON, MAIN_CONTAINER
import os


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.input_file = None

        self.setWindowTitle("Offline Converter")
        self.resize(500, 350)

        # title
        self.title_label = TitleLabel()

        # file selection info
        self.file_label = FileLabel()

        # comboBox
        self.conversion_box = QComboBox()
        self.conversion_box.addItems(["Image -> PDF", "PDF -> Image"])

        #buttons
        self.select_btn = SelectButton()
        self.convert_btn = ConvertButton()

        # styles
        self.title_label.setStyleSheet(TITLE_LABEL)
        self.file_label.setStyleSheet(FILE_LABEL)
        self.select_btn.setStyleSheet(SELECT_BUTTON)
        self.convert_btn.setStyleSheet(CONVERT_BUTTON)

        #layout
        layout = QVBoxLayout()

        layout.addWidget(self.title_label)
        layout.addWidget(self.file_label)
        layout.addWidget(self.conversion_box)
        layout.addWidget(self.select_btn)
        layout.addWidget(self.convert_btn)

        # central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        container.setStyleSheet(MAIN_CONTAINER)

        self.select_btn.clicked.connect(self.select_image)
        self.convert_btn.clicked.connect(self.convert)

    def select_image(self):
        self.input_file = get_image_file()

        if self.input_file:
            file_name = Path(self.input_file).name 
            self.file_label.setText(f"Selecte File: {file_name}")
            # print("Input", self.input_file)

    def convert(self):

        if not self.input_file:
            QMessageBox.warning(
                self, "Error", "Please select an image"
            )
            # print("Please select an image")
            return 

        output_dir = SaveFileDialog()
        
        if not output_dir:
            return

        image_name = Path(self.input_file).stem 

        pdf_path = os.path.join(
            output_dir,
            f"{image_name}.pdf"
        )
        try:
            convert_image_to_pdf(
                self.input_file,
                pdf_path
            )
            if True:
                QMessageBox.information(
                    self, 
                    "Success", 
                    f"PDF created successfully!\n\n{pdf_path}"
                )
        except Exception as e:
            QMessageBox.critical(
                self, "Conversion Failed", str(e)
            )
