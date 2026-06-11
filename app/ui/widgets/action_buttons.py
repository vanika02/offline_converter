from PySide6.QtWidgets import QPushButton

class SelectButton(QPushButton):
    def __init__(self):
        super().__init__("Select Image")

        self.setMinimumHeight(50)
        self.setObjectName("SelectButton")


class ConvertButton(QPushButton):
    def __init__(self):
        super().__init__("Convert to PDF")

        self.setMinimumHeight(50)
        self.setObjectName("convertButton")