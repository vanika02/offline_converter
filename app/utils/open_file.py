import os
from PySide6.QtWidgets import QFileDialog


def OpenFileDialog():
    """
    Opens a file dialog and sets the label to the chosen path 
    """

    path, _ = QtGui.QFileDialog.getOpenFileName(None, "Open File", os.getcwd())
    return path
