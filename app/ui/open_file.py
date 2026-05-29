import sys
from PySide6 import QtGui


def OpenFileDialog():
    """
    Opens a file dialog and sets the label to the chosen path 
    """

    path, _ = QtGui.QFileDialog.getOpenFileName(self, "Open File", os.getcwd())
    return path
