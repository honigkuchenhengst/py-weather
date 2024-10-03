from PyQt5.QtCore import QSize, QTextStream
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout, QGridLayout, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Py Weather App")

        layout = QGridLayout()

        zip_input = QLineEdit()
        zip_input.setMaxLength(6)
        zip_input.setPlaceholderText("Enter Zip Code")
        button_send = QPushButton("Send")
        button_clear = QPushButton("New Zip")

        layout.addWidget(zip_input, 0, 0)
        layout.addWidget(button_send, 0, 1)
        layout.addWidget(button_clear, 3, 3)


        self.setFixedSize(QSize(800, 500))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()




