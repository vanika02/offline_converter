import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton
from PySide6.QtCore import Slot


# this creates a func that logs message to the console - slot is a decorator that identifies func as a slot
@Slot()
def say_hello():
    print("Button clicked, wasssuppp")

# this will create QApplication to run the pyside6 code
app = QApplication(sys.argv)


# create a button, connect and show it
button = QPushButton("Click me")
button.clicked.connect(say_hello)
button.show()


# label = QLabel("Hello World!")
# label.show()


# run the main Qt Loop
app.exec()