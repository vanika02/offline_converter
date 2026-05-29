import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Slot
from layout_colorwidget import Color
from open_file import OpenFileDialog


# this creates a func that logs message to the console - slot is a decorator that identifies func as a slot
@Slot()
def say_hello():
    print("Button clicked, wasssuppp")



# creating a class main window to start the application
# this will create QApplication to run the pyside6 code
class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Offline Converter")
        self.label = 
        btn = QPushButton(text="Click here")
        btn.setFixedSize(100, 60)

        layout = QVBoxLayout()
        layout.addWidget(Color("black"))
        layout.addWidget(btn)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        path = OpenFileDialog()
        self.label.setText(path)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
