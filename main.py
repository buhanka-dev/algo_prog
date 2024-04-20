from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
import sys


class ScreenFinal(QWidget):
    def __init__(self):
        super().__init__()
        result_label = QLabel(result_text)
        heart_label = QLabel(heart_text)

        vertical_line = QVBoxLayout()

        vertical_line.addWidget(result_label, alignment=Qt.AlignCenter)
        vertical_line.addWidget(heart_label, alignment=Qt.AlignCenter)

        self.setLayout(vertical_line)


class ScreenMain(QWidget):
    def __init__(self):
        super().__init__()
        start_button_label = QPushButton(button_start_text)
        intrduction_label = QLabel(introduction_text)
        description_label = QLabel(description_text)

        description_label.setWordWrap(True)

        vertical_line = QVBoxLayout()
        vertical_line.addWidget(intrduction_label)
        vertical_line.addWidget(description_label)
        vertical_line.addWidget(start_button_label, alignment=Qt.AlignCenter)

        self.setLayout(vertical_line)


app = QApplication(sys.argv)
main_window = ScreenMain()
main_window.setFixedSize(400, 350)
main_window.show()

final_window = ScreenFinal()
final_window.setFixedSize(400, 350)
final_window.show()

sys.exit(app.exec_())
