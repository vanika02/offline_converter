from PySide6.QtWidgets import QApplication, QWidget
from app.ui.main_window import MainWindow


# need this one for access to the command line arguments
import sys


# we need one and onl yone QApplication instance per application
# Pass in sys.argv to allow command line arguments for your app
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# this creates an instance of the main window
window = MainWindow()