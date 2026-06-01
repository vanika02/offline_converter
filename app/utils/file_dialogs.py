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

def SaveFileDialog():
    """
    Opens a Save file dialog and return the selected PDF file path
    """
    file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "pdf files (*.pdf)")
    return file_path