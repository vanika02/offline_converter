from pathlib import Path
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout, 
    QMessageBox, 
    QComboBox
)
from app.enums.conversion_type import ConversionType
from app.services.conversion_service import ConversionService
from app.ui.styles import (
    TITLE_LABEL, 
    FILE_LABEL, 
    SELECT_BUTTON, 
    CONVERT_BUTTON, 
    MAIN_CONTAINER
)
from app.ui.widgets.action_buttons import SelectButton, ConvertButton
from app.ui.widgets.file_label import FileLabel
from app.ui.widgets.title_label import TitleLabel
from app.utils.file_dialogs import (
    get_image_file, 
    get_output_directory, 
    get_pdf_file
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.input_file = None
        self.conversion_service = ConversionService()

        self.setWindowTitle("Offline Converter")
        self.resize(500, 350)

        # widgets
        self.title_label = TitleLabel()
        self.file_label = FileLabel()

        self.conversion_box = QComboBox()
        
        # Populate combo box from enum
        for conversion in ConversionType:
            self.conversion_box.addItem(conversion.value)

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
        container.setStyleSheet(MAIN_CONTAINER)

        self.setCentralWidget(container)

        # signals
        self.select_btn.clicked.connect(self.select_file)
        self.convert_btn.clicked.connect(self.convert)
        self.conversion_box.currentIndexChanged.connect(
            self.reset_selected_file
        )

    def current_conversion(self) -> ConversionType:
        """
        Returns the currently selected conversion type
        """
        return ConversionType(
            self.conversion_box.currentText()
        )

    def reset_selected_file(self):
        """
        Clears the previously selected file whenever the conversation type changes.
        """

        self.input_file = None
        self.file_label.setText("No file selected")


    def select_file(self):
        conversion = self.current_conversion()

        if conversion == ConversionType.IMG_TO_PDF:
            self.input_file = get_image_file()

        elif conversion == ConversionType.PDF_TO_IMAGE:
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

        output_dir = get_output_directory()

        if not output_dir:
            return 
        
        try:
            output_files = self.conversion_service.convert(
                self.input_file,
                output_dir,
                self.current_conversion()
            )

            if isinstance(output_files, list):
                message = "\n".join(output_files)
            else:
                message = output_files


            QMessageBox.information(
                self,
                "Success",
                f"Conversion completed successfully.\n\n{message}"
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Conversion Failed",
                str(e)
            )