from PySide6.QtWidgets import QPushButton

class SelectButton(QPushButton):
    def __init__(self):
        super().__init__("Select Image")

        self.setMinimumHeight(50)
        self.setObjectName("SelectButton")