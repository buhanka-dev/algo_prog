from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
import sys


class SecondScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.window_appearence()
        self.init_ui()
        self.show()

    def window_appearence(self):
        self.setFixedSize(500, 500)

    def init_ui(self):
        self.horizontal_line = QHBoxLayout()
        self.vertical_line_left = QVBoxLayout()
        self.vertical_line_right = QVBoxLayout()

        self.name_label = QLabel('Введите Ф.И.О.')
        self.name_entry = QLineEdit()

        self.year_label = QLabel('Полных лет')
        self.year_entry = QLineEdit()

        self.first_test_label = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер. Результат запишите в соответствующее поле.')
        self.first_test_button = QPushButton('Начать первый тест')
        self.first_test_entry = QLineEdit()

        self.second_test_label = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания", чтобы запустить счетчик приседаний.')
        self.second_test_button = QPushButton('Начать делать приседания')

        self.third_test_label = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд. Нажмите кнопку "Начать финальный тест", чтобы запустить таймер. Зеленым обозначены секунды, в течение которых необходимо проводить измерения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.')

        self.first_test_label.setWordWrap(True)
        self.second_test_label.setWordWrap(True)

        self.vertical_line_left.addWidget(self.name_label, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.name_entry, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.year_label, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.year_entry, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.first_test_label, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.first_test_button, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.first_test_entry, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.second_test_label, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.second_test_button, alignment=Qt.AlignLeft)

        self.horizontal_line.addLayout(self.vertical_line_left)
        self.horizontal_line.addLayout(self.vertical_line_right)

        self.setLayout(self.horizontal_line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    second_window = SecondScreen()
    second_window.show()

    sys.exit(app.exec_())
