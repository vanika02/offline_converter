from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox, QComboBox
from PySide6.QtCore import Qt
from pathlib import Path
from app.ui.layout_colorwidget import Color
from app.utils.file_dialogs import get_image_file, save_file_dialog, get_pdf_file
from app.services.conversion_service import ConversionService
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

        self.select_btn.clicked.connect(self.select_file)
        self.convert_btn.clicked.connect(self.convert)

    def select_file(self):
        conversion = self.conversion_box.currentText()

        if conversion == "Image -> PDF":
            self.input_file = get_image_file()

        elif conversion == "PDF -> Image":
            self.input_file = get_pdf_file()
        
        if self.input_file:
            filename = Path(self.input_file).name
            self.file_label.setText(
                f"Selected File : {filename}"
            )

    def convert(self):
        if not self.input_file:
            QMessageBox.warning(
                self,
                "Error",
                "Please select a file"
            )
            return 

        output_dir = save_file_dialog()
        if not output_dir:
            return 
        
        conversion_type = self.conversion_box.currentText()

        service = ConversionService()
        try:
            output = service.convert(
                self.input_file,
                output_dir,
                conversion_type
            )
            QMessageBox.information(
                self,
                "Success",
                f"Conversion completed successfully.\n\n{output}"
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Conversion Failed",
                str(e)
            )