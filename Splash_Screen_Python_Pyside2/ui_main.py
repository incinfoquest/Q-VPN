# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainEErzxk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 581)
        MainWindow.setStyleSheet(u"background-color: rgb(23, 33, 59);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 30, 801, 571))
        self.label_2.setPixmap(QPixmap(u"../../../Downloads/vpnbg.png"))
        self.label_2.setScaledContents(True)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(-1, 0, 801, 41))
        self.top_bar.setStyleSheet(u"background-color: rgb(34, 31, 14);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.Logo = QLabel(self.top_bar)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(40, 0, 81, 41))
        font = QFont()
        font.setFamily(u"Rockwell Std")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Logo.setFont(font)
        self.Logo.setStyleSheet(u"QLabel{\n"
"\n"
"background-color: rgba(0,0,0,0%)\n"
"\n"
"}")
        self.Logo.setAlignment(Qt.AlignCenter)
        self.F_B = QPushButton(self.top_bar)
        self.F_B.setObjectName(u"F_B")
        self.F_B.setGeometry(QRect(620, 10, 21, 23))
        self.F_B.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../face.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.F_B.setIcon(icon)
        self.F_B.setIconSize(QSize(25, 25))
        self.T_T = QPushButton(self.top_bar)
        self.T_T.setObjectName(u"T_T")
        self.T_T.setGeometry(QRect(660, 10, 21, 23))
        self.T_T.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../tweet.png", QSize(), QIcon.Normal, QIcon.Off)
        self.T_T.setIcon(icon1)
        self.T_T.setIconSize(QSize(25, 25))
        self.Git = QPushButton(self.top_bar)
        self.Git.setObjectName(u"Git")
        self.Git.setGeometry(QRect(700, 0, 31, 41))
        self.Git.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../GitHub-Mark/PNG/GitHub-Mark-Light-64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Git.setIcon(icon2)
        self.Git.setIconSize(QSize(25, 25))
        self.pushButton_2 = QPushButton(self.top_bar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(730, 10, 61, 23))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../../GitHub-Logos/GitHub_Logo_White.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(65, 65))
        self.pushButton_3 = QPushButton(self.top_bar)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(580, 2, 21, 41))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../../../Downloads/icons8-instagram.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QSize(30, 30))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 111, 21))
        font1 = QFont()
        font1.setFamily(u"Rockwell Std")
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: rgba(0,0,0,0%)")
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Crnt_Ip = QLabel(self.centralwidget)
        self.Crnt_Ip.setObjectName(u"Crnt_Ip")
        self.Crnt_Ip.setGeometry(QRect(130, 60, 221, 41))
        self.Crnt_Ip.setStyleSheet(u"background-color: rgba(0,0,0,0%)")
        self.connect_Btn = QPushButton(self.centralwidget)
        self.connect_Btn.setObjectName(u"connect_Btn")
        self.connect_Btn.setGeometry(QRect(300, 210, 201, 181))
        self.connect_Btn.setStyleSheet(u"QPushButton{background: transparent\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../../../Downloads/clipart2939527.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connect_Btn.setIcon(icon5)
        self.connect_Btn.setIconSize(QSize(150, 150))
        self.Tor_Btn = QPushButton(self.centralwidget)
        self.Tor_Btn.setObjectName(u"Tor_Btn")
        self.Tor_Btn.setGeometry(QRect(720, 60, 51, 51))
        self.Tor_Btn.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../../../Downloads/emojipng.com-2364600.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Tor_Btn.setIcon(icon6)
        self.Tor_Btn.setIconSize(QSize(40, 40))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(690, 80, 31, 21))
        self.label.setStyleSheet(u"QLabel{\n"
"background: transparent\n"
"}")
        self.speed_Test = QPushButton(self.centralwidget)
        self.speed_Test.setObjectName(u"speed_Test")
        self.speed_Test.setGeometry(QRect(670, 470, 121, 101))
        self.speed_Test.setStyleSheet(u"QPushButton{\n"
"\n"
"background:transparent;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../../../Downloads/icons8-ookla-speedtest.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.speed_Test.setIcon(icon7)
        self.speed_Test.setIconSize(QSize(100, 100))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.Logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Q VPN.</span></p></body></html>", None))
        self.F_B.setText("")
        self.T_T.setText("")
        self.Git.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">CURRENT IP :</span></p></body></html>", None))
        self.Crnt_Ip.setText("")
        self.connect_Btn.setText("")
        self.Tor_Btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">TOR</span></p></body></html>", None))
        self.speed_Test.setText("")
    # retranslateUi

