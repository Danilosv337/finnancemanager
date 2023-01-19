from PySide6.QtWidgets import QMainWindow,QApplication
from sys import argv
from interfaces.login_window import *


class Login_panel(Ui_login_window,QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setFixedSize(493,351)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(self.close)
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
        self.dragPos = event.globalPosition().toPoint()
        event.accept()





if __name__ == "__main__":
    qt = QApplication(argv)
    app = Login_panel()
    app.show()
    qt.exec_()