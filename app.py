from PySide6.QtWidgets import QApplication
from sys import argv
from modules.login_panel import *


qt = QApplication(argv)
app = Login_panel()
app.show()
qt.exec()