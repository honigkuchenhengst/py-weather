from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Push mich!")

        self.setFixedSize(QSize(800, 500))

        self.setCentralWidget(button)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()




