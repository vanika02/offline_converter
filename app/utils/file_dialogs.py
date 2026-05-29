import os
from PySide6.QtWidgets import QFileDialog


def  get_image_file():
    """
    Selects an image file using a file dialog and returns its path
    """
    file_path, _ = QFileDialog.getOpenFileName(
        None,
        "Select Image",
        "", 
        "Images (*.png *.jpg *.jpeg *.bmp)"
    )

    return file_path

def OpenFileDialog():
    """
    Opens a file dialog and sets the label to the chosen path 
    """

    path, _ = QFileDialog.getOpenFileName(None, "Open File", os.getcwd())
    return path
