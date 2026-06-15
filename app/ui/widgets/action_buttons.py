from PySide6.QtWidgets import QPushButton

class SelectButton(QPushButton):
    def __init__(self):
        super().__init__("Select File")

        self.setMinimumHeight(50)
        self.setObjectName("SelectButton")


class ConvertButton(QPushButton):
    def __init__(self):
        super().__init__("Convert")

        self.setMinimumHeight(50)
        self.setObjectName("convertButton")