from PySide6.QtWidgets import QMainWindow,QApplication,QStackedWidget
from sys import argv
from interfaces.login_window import *
from interfaces.manager import *
from main import  *

user = Usuario()

class Manager_app(Ui_Manager,QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(.95)
        self.sidebar.setFixedWidth(0)
        self.width_bar = 0
        self.QStackedWidget.setCurrentWidget(self.main_page)
        self.pushButton.clicked.connect(self.sidebar_size)

    def sidebar_size(self):
        if self.width_bar == 0:
            self.sidebar.setFixedWidth(100)
            self.width_bar = 1
        else:
            self.sidebar.setFixedWidth(0)
            self.width_bar = 0

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

class Login_panel(Ui_login_window,QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        #Config Window
        self.setFixedSize(493,351)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(.9)

        #Config Buttons
        self.btn_close.clicked.connect(self.close)
        self.btn_quit.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_login.clicked.connect(self.login)


    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
        self.dragPos = event.globalPosition().toPoint()
        event.accept()
    
    

    def login(self):

        user.login(self.Textinput_user.text(),self.Textinput_password.text())

        if user.ID_user != None and user.ID_user != '':
            self.interface = Manager_app()
            self.close()
            self.interface.show()
   
        else:
            self.Textinput_loginmessage.setText("Usuário Ou Senha Incorretos")
            self.Textinput_loginmessage.setStyleSheet("color: red;")
        


if __name__ == "__main__":
    qt = QApplication(argv)
    app = Login_panel()
    app.show()
    qt.exec()