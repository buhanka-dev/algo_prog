from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
import sys


class FirstScreen(QWidget):
    def __init__(self, next_window):
        super().__init__()
        self.next_window = next_window
        self.window_appearence()
        self.init_ui()
        self.connections()
        self.show()


    def window_appearence(self):
        self.setFixedSize(500, 500)

    def init_ui(self):
        self.start_button = QPushButton(button_start_text)
        self.intrduction_label = QLabel(introduction_text)
        self.description_label = QLabel(description_text)

        self.description_label.setWordWrap(True)

        self.vertical_line = QVBoxLayout()
        self.vertical_line.addWidget(self.intrduction_label)
        self.vertical_line.addWidget(self.description_label)

        self.vertical_line.addWidget(self.start_button, alignment=Qt.AlignCenter)

        self.setLayout(self.vertical_line)

    def connections(self):
        self.start_button.clicked.connect(self.next_window)

    def next_window(self):
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = FirstScreen()

    sys.exit(app.exec_())
