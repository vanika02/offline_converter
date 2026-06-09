from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

class TitleLabel(QLabel):
    def __init__(self):
        super().__init__("Offline Image -> PDF Converter")

        self.setAlignment(Qt.AlignCenter)
        self.setObjectName("titleLabel")