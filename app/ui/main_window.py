import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Slot
from layout_colorwidget import Color


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

        layout = QVBoxLayout()

        layout.addWidget(Color("black"))


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()



# create a button, connect and show it
# button = QPushButton("Click me")
# button.clicked.connect(say_hello)
# button.show()


# label = QLabel("Hello World!")
# label.show()


# run the main Qt Loop
# app.exec()