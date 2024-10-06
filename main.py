import requests

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QLabel

API_Key = '9b28c7a3bcea595744fc43c16882304f'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Py Weather App")

        layout = QVBoxLayout()

        self.zip_input = QLineEdit(self)
        self.zip_input.setPlaceholderText("Enter city or zip code")
        self.button_send = QPushButton("Send")
        self.button_send.clicked.connect(self.get_wetter)
        self.button_clear = QPushButton("New city / zip")
        self.button_clear.clicked.connect(self.clear_zip)
        self.label_result = QLabel('Weather Data is shown here...')

        layout.addWidget(self.zip_input)
        layout.addWidget(self.button_send)
        layout.addWidget(self.button_clear)
        layout.addWidget(self.label_result)


        self.setFixedSize(QSize(250, 250))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def get_wetter(self):
        city = self.zip_input.text()
        if city:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_Key}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temperature = data['main']['temp']
                weather_description = data['weather'][0]['description']
                self.label_result.setText(f'Temperature: {temperature}°C\nDescription: {weather_description}')
            else:
                self.label_result.setText(f'City or zip code not found')

    def clear_zip(self):
        self.zip_input.setText('')
        self.label_result.setText('Weather Data is shown here...')


app = QApplication([])

window = MainWindow()
window.show()

app.exec()




