from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
import sys


class SecondScreen(QWidget):
    def __init__(self, next_window):
        super().__init__()
        self.next_w = next_window
        self.window_appearence()
        self.init_ui()
        self.connections()

    def window_appearence(self):
        self.setFixedSize(800, 500)

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
        self.third_test_button = QPushButton('Начать финальный тест')

        self.third_test_entry1 = QLineEdit()
        self.third_test_entry2 = QLineEdit()

        self.next_button = QPushButton('Отправить результаты')

        self.first_test_label.setWordWrap(True)
        self.second_test_label.setWordWrap(True)
        self.third_test_label.setWordWrap(True)

        self.timer_label = QLabel('<span style="font-size:40pt; ">99:99:99</span>')

        self.vertical_line_left.addWidget(self.name_label, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.name_entry, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.year_label, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.year_entry, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.first_test_label, alignment=Qt.AlignLeft, stretch=Qt.AlignCenter)
        self.vertical_line_left.addWidget(self.first_test_button, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.first_test_entry, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.second_test_label, alignment=Qt.AlignLeft, stretch=Qt.AlignCenter)
        self.vertical_line_left.addWidget(self.second_test_button, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.third_test_label, alignment=Qt.AlignLeft, stretch=Qt.AlignCenter)
        self.vertical_line_left.addWidget(self.third_test_button, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.third_test_entry1, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.third_test_entry2, alignment=Qt.AlignLeft)
        self.vertical_line_left.addWidget(self.next_button, alignment=Qt.AlignRight)

        self.vertical_line_right.addWidget(self.timer_label, alignment=Qt.AlignRight)

        self.horizontal_line.addLayout(self.vertical_line_left)
        self.horizontal_line.addLayout(self.vertical_line_right)

        self.setLayout(self.horizontal_line)

    def connections(self):
        self.next_button.clicked.connect(self.next_window)

    def next_window(self):
        self.hide()
        self.next_w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    second_window = SecondScreen('')
    second_window.show()

    sys.exit(app.exec_())
