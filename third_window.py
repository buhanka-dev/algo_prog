from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import instr
import sys


class ThirdScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.window_appearence()
        self.init_ui()

    def window_appearence(self):
        self.setFixedSize(800, 500)

    def init_ui(self):
        self.result_label = QLabel(instr.result_text)
        self.heart_label = QLabel(instr.heart_text)

        self.vertical_line = QVBoxLayout()

        self.vertical_line.addWidget(self.result_label, alignment=Qt.AlignCenter)
        self.vertical_line.addWidget(self.heart_label, alignment=Qt.AlignCenter)

        self.setLayout(self.vertical_line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    final_window = ThirdScreen()

    sys.exit(app.exec_())
