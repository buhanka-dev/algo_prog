from second_window import *
from first_window import *
from third_window import *


app = QApplication(sys.argv)
third_window = ThirdScreen()
second_window = SecondScreen(third_window)
main_window = FirstScreen(second_window)

sys.exit(app.exec_())
