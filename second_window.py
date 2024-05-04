from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import instr
import sys

k = instr.description_text


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

        self.first_test_label = QLabel(instr.first_text)
        self.first_test_button = QPushButton('Начать первый тест')
        self.first_test_entry = QLineEdit()

        self.second_test_label = QLabel(instr.second_text)
        self.second_test_button = QPushButton('Начать делать приседания')

        self.third_test_label = QLabel(instr.third_text)
        self.third_test_button = QPushButton('Начать финальный тест')

        self.third_test_entry1 = QLineEdit()
        self.third_test_entry2 = QLineEdit()

        self.next_button = QPushButton('Отправить результаты')

        self.first_test_label.setWordWrap(True)
        self.second_test_label.setWordWrap(True)
        self.third_test_label.setWordWrap(True)

        self.timer_label = QLabel('<span style="font-size:40pt; "></span>')

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
        self.first_test_button.clicked.connect(self.timer_test)
        self.second_test_button.clicked.connect(self.timer_sits)
        self.third_test_button.clicked.connect(self.timer_final)

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.simple_timer)
        self.timer_label.setText('<span style="font-size:40pt; ">' + '00:15' + '</span>')
        self.timer.start(1000)

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.simple_timer)
        self.timer_label.setText('<span style="font-size:40pt; ">' + '00:30' + '</span>')
        self.timer.start(1000)

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.color_timer)
        self.timer_label.setText('<span style="color:rgb(20, 255, 20); font-size:40pt;> 1:00 </span>')
        self.timer.start(1000)

    def simple_timer(self):
        global time
        time = time.addSecs(-1)
        self.timer_label.setText('<span style="font-size:40pt; ">' + time.toString('mm:ss') + '</span>')
        if time.toString('mm:ss') == '00:00':
            self.timer.stop()
            self.timer_label.setText('<span style="font-size:40pt; "> </span>')

    def color_timer(self):
        global time
        time = time.addSecs(-1)
        if int(time.toString('mm:ss')[3::]) <= 45:
            self.timer_label.setText(
                '<span style="color:rgb(0, 0, 0); font-size:40pt; ">' + time.toString('mm:ss') + '</span>')
        if int(time.toString('mm:ss')[3::]) <= 15:
            self.timer_label.setText(
                '<span style="color:rgb(20, 255, 20); font-size:40pt; ">' + time.toString('mm:ss') + '</span>')
        if int(time.toString('mm:ss')[3::]) > 45:
            self.timer_label.setText(
                '<span style="color:rgb(20, 255, 20); font-size:40pt; ">' + time.toString('mm:ss') + '</span>')
        if time.toString('mm:ss') == '00:00':
            self.timer.stop()
            self.timer_label.setText('<span style="font-size:40pt; "> </span>')

    def next_window(self):
        self.hide()
        self.next_w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    second_window = SecondScreen('')
    second_window.show()

    sys.exit(app.exec_())
