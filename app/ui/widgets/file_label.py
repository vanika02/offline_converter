from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt 

class FileLsbel(QLabel):
    def __init__(self):
        super().__init__("Selected file: None")

        self.setAlignment(Qt.AlignCenter)
        self.setObjectName("fileLabel")