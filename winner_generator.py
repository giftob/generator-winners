#подключение библиотек

#создание элементов интерфейса

#привязка элементов к вертикальной линии

#обработка событий

#запуск приложения

from random import randint
from PyQt5. QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
def show_winner():
    num = randint(0, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    number.setText(str(num))
app = QApplication([])
window = QWidget()
v_line = QVBoxLayout()

q = QLabel('Нажми чтобы узнать победителя')
number = QLabel('?')
button = QPushButton('Сгенерировать')
button.clicked.connect(show_winner)

v_line.addWidget(q)
v_line.addWidget(number)
v_line.addWidget(button)

window.setLayout(v_line)
window.show()
app.exec()
