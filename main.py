from second_window import *
from first_window import *
from third_window import *


app = QApplication(sys.argv)
main_window = FirstScreen()

sys.exit(app.exec_())
