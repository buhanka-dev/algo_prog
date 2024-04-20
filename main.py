from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
import sys


class ScreenMain(QWidget):
    def __init__(self):
        super().__init__()
        start_button = QPushButton(button_start_text)
        intrduction = QLabel(introduction_text)
        description = QLabel(description_text)

        description.setWordWrap(True)

        vertical_line1 = QVBoxLayout()
        vertical_line1.addWidget(intrduction)
        vertical_line1.addWidget(description)
        vertical_line1.addWidget(start_button, alignment=Qt.AlignCenter)

        self.setLayout(vertical_line1)


app = QApplication(sys.argv)
main_window = ScreenMain()
main_window.setFixedSize(400, 350)
main_window.show()
sys.exit(app.exec_())
