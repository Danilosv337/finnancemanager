# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finnanceYBfPnh.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources.resource_rc

class Ui_Manager(object):
    def setupUi(self, Manager):
        if not Manager.objectName():
            Manager.setObjectName(u"Manager")
        Manager.resize(1019, 520)
        self.centralwidget = QWidget(Manager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"QFrame#main_frame,QWidget#main_page,QWidget#main_page2{\n"
"border-radius: 30px;\n"
"border: .5px solid black;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 132, 228, 255), stop:1 rgba(26, 95, 180, 255));\n"
"}\n"
"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.QStackedWidget = QStackedWidget(self.main_frame)
        self.QStackedWidget.setObjectName(u"QStackedWidget")
        self.QStackedWidget.setStyleSheet(u"")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_7 = QHBoxLayout(self.page_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_11 = QFrame(self.page_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tableWidget_2 = QTableWidget(self.frame_11)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_9.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.pushButton_10 = QPushButton(self.frame_12)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_8.addWidget(self.pushButton_10)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.pushButton_12 = QPushButton(self.frame_12)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_8.addWidget(self.pushButton_12)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.gridLayout_9.addWidget(self.frame_12, 1, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.frame_11)

        self.QStackedWidget.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.QStackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.QStackedWidget.addWidget(self.page_2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.QStackedWidget.addWidget(self.page)
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.main_page.setStyleSheet(u"border:none")
        self.gridLayout_2 = QGridLayout(self.main_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_8 = QFrame(self.main_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"border: none;")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_8)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_5 = QFrame(self.frame_9)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: green;\n"
"border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 25px;\n"
"font-weight: bold ;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 3)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setCursor(QCursor(Qt.CrossCursor))
        self.label_2.setStyleSheet(u"max-height: 40px;\n"
"max-width: 40px")
        self.label_2.setPixmap(QPixmap(u":/icons/carteira.png"))
        self.label_2.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size: 20px")

        self.gridLayout_4.addWidget(self.label_3, 2, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: green;\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"max-height: 40px;\n"
"max-width: 40px")
        self.label_5.setPixmap(QPixmap(u":/icons/aumentar.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size: 20px")

        self.gridLayout_6.addWidget(self.label_6, 3, 2, 1, 1)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size: 25px;\n"
"font-weight: bold;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_4, 2, 0, 1, 3)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: red;\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"max-height: 40px;\n"
"max-width: 40px")
        self.label_8.setPixmap(QPixmap(u":/icons/financas.png"))
        self.label_8.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-size: 20px")

        self.gridLayout_5.addWidget(self.label_9, 2, 2, 1, 1)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font-size: 25px;\n"
"font-weight: bold;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_7, 1, 0, 1, 3)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.gridLayout_3.addWidget(self.frame_9, 0, 0, 1, 3)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QPushButton{\n"
"background-color: white;\n"
"color: black;\n"
"text-transform: uppercase;\n"
"min-width: 100px;\n"
"min-height: 25px;\n"
"border: 1px solid black;\n"
"border-radius: 7px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pushButton_7 = QPushButton(self.frame_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.pushButton_8 = QPushButton(self.frame_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.pushButton_8)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.gridLayout_3.addWidget(self.frame_10, 1, 0, 1, 3)


        self.gridLayout_2.addWidget(self.frame_8, 0, 0, 1, 1)

        self.QStackedWidget.addWidget(self.main_page)
        self.main_page2 = QWidget()
        self.main_page2.setObjectName(u"main_page2")
        self.gridLayout_7 = QGridLayout(self.main_page2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame = QFrame(self.main_page2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_8.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.main_page2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"color: black;\n"
"background-color:white;\n"
"text-transform: uppercase;\n"
"min-width: 100px;\n"
"min-height: 30px;\n"
"border: 1px solid black;\n"
"border-radius: 8px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.pushButton_11 = QPushButton(self.frame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_6.addWidget(self.pushButton_11)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.gridLayout_7.addWidget(self.frame_2, 1, 0, 1, 1)

        self.QStackedWidget.addWidget(self.main_page2)

        self.gridLayout.addWidget(self.QStackedWidget, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.main_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"max-height:40px;\n"
"min-height: 40px;\n"
"\n"
"}\n"
"QPushButton{\n"
"min-height: 20px;\n"
"max-height: 20px;\n"
"background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"font-size:20px\n"
"}")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_minimize = QPushButton(self.frame_3)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_quit = QPushButton(self.frame_3)
        self.btn_quit.setObjectName(u"btn_quit")
        self.btn_quit.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_quit)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.main_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"min-height: 40px;\n"
"max-height: 40px;\n"
"}\n"
"QLabel{\n"
"font-size: 15px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.gridLayout.addWidget(self.frame_4, 2, 1, 1, 1)

        self.sidebar = QFrame(self.main_frame)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: rgb(25,25,25);\n"
"border-top-left-radius: 30px;\n"
"border-bottom-left-radius: 30px;\n"
"}\n"
"QPushButton{\n"
"border: none;\n"
"background-color: rgb(25,25,25);\n"
"min-width: 100%;\n"
"min-height: 60px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(53, 132, 228);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"\n"
"}")
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_9 = QPushButton(self.sidebar)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/botao-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_4 = QPushButton(self.sidebar)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/carteira.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.sidebar)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/aumentar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.sidebar)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/financas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.sidebar, 0, 0, 3, 1)


        self.horizontalLayout.addWidget(self.main_frame)

        Manager.setCentralWidget(self.centralwidget)

        self.retranslateUi(Manager)
        self.btn_quit.clicked.connect(Manager.close)
        self.btn_minimize.clicked.connect(Manager.showMinimized)

        self.QStackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Manager)
    # setupUi

    def retranslateUi(self, Manager):
        Manager.setWindowTitle(QCoreApplication.translate("Manager", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Manager", u"Desc Lucro", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Manager", u"Lucro", None));
        self.pushButton_10.setText(QCoreApplication.translate("Manager", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("Manager", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Manager", u"Sal\u00e1rio", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Manager", u"R$ 00,00", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("Manager", u"R$ 00,00", None))
        self.label_4.setText(QCoreApplication.translate("Manager", u"Lucros", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("Manager", u"R$ 00,00", None))
        self.label_7.setText(QCoreApplication.translate("Manager", u"Gastos", None))
        self.pushButton_7.setText(QCoreApplication.translate("Manager", u"Atualizar", None))
        self.pushButton_8.setText(QCoreApplication.translate("Manager", u"Sair", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Manager", u"Descri\u00e7\u00e3o Gasto", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Manager", u"Valor Gasto", None));
        self.pushButton_3.setText(QCoreApplication.translate("Manager", u"Adicionar", None))
        self.pushButton_11.setText(QCoreApplication.translate("Manager", u"Remover", None))
        self.pushButton.setText("")
        self.btn_minimize.setText(QCoreApplication.translate("Manager", u"-", None))
        self.btn_quit.setText(QCoreApplication.translate("Manager", u"x", None))
        self.label_10.setText(QCoreApplication.translate("Manager", u"Finnance Manager V2 \u00a9 Danilosv337 -  2023", None))
        self.pushButton_9.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
    # retranslateUi

