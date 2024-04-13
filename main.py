from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import sys


class ScreenMain(QWidget):
    def __init__(self):
        super().__init__()
        start_button = QPushButton('Lorem ipsum.')
        intrduction = QLabel('Lorem ipsum dolor sit amet.')
        description = QLabel(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus luctus sit amet ipsum quis '
            'placerat. Donec malesuada ante sit amet arcu scelerisque fringilla. Quisque pretium non orci id '
            'aliquam. Duis bibendum nisi risus, eu vehicula orci dictum sit amet. Nullam lorem velit, '
            'laoreet non erat sed, tincidunt malesuada sem. Interdum et malesuada fames ac ante ipsum primis '
            'in faucibus. Duis aliquet a est tincidunt finibus. Sed mollis, dui sit amet dictum gravida, '
            'enim diam accumsan urna, in rhoncus elit purus id neque. Etiam sed purus mollis, commodo nisi '
            'eu, rhoncus dolor. Curabitur quis risus ante. Curabitur finibus tortor massa. Aenean.')

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
