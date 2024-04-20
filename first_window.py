from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
import sys


class ScreenMain(QWidget):
    def __init__(self):
        super().__init__()
        self.start_button = QPushButton(button_start_text)
        intrduction_label = QLabel(introduction_text)
        description_label = QLabel(description_text)

        description_label.setWordWrap(True)

        vertical_line = QVBoxLayout()
        vertical_line.addWidget(intrduction_label)
        vertical_line.addWidget(description_label)
        vertical_line.addWidget(self.start_button, alignment=Qt.AlignCenter)

        self.setLayout(vertical_line)


app = QApplication(sys.argv)
main_window = ScreenMain()
main_window.setFixedSize(400, 350)
main_window.show()

sys.exit(app.exec_())
