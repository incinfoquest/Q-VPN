# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainEpnZgc.ui'
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
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(23, 33, 59);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 30, 801, 571))
        self.label_2.setPixmap(QPixmap(u"resources/vpnbg.png"))
        self.label_2.setScaledContents(True)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(-1, 0, 801, 41))
        self.top_bar.setStyleSheet(u"background-color: rgb(34, 31, 14);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.Logo = QLabel(self.top_bar)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(10, 0, 91, 41))
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
        self.F_B.setGeometry(QRect(640, 10, 21, 23))
        self.F_B.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon = QIcon()
        icon.addFile(u"resources/face.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.F_B.setIcon(icon)
        self.F_B.setIconSize(QSize(20, 20))
        self.T_T = QPushButton(self.top_bar)
        self.T_T.setObjectName(u"T_T")
        self.T_T.setGeometry(QRect(680, 10, 21, 23))
        self.T_T.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"resources/tweet.png", QSize(), QIcon.Normal, QIcon.Off)
        self.T_T.setIcon(icon1)
        self.T_T.setIconSize(QSize(20, 20))
        self.Git = QPushButton(self.top_bar)
        self.Git.setObjectName(u"Git")
        self.Git.setGeometry(QRect(710, 10, 31, 21))
        self.Git.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"resources/GitHub-Mark-Light-64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Git.setIcon(icon2)
        self.Git.setIconSize(QSize(20, 20))
        self.pushButton_2 = QPushButton(self.top_bar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(740, 0, 61, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"resources/GitHub_Logo_White.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(55, 55))
        self.pushButton_3 = QPushButton(self.top_bar)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(600, 10, 21, 21))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"resources/icons8-instagram.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QSize(30, 30))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 111, 21))
        font1 = QFont()
        font1.setFamily(u"AvenirNext LT Pro Bold")
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
        self.connect_Btn.setGeometry(QRect(320, 220, 160, 160))
        self.connect_Btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 80px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(48, 154, 38);\n"
"\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"resources/clipart2939527.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connect_Btn.setIcon(icon5)
        self.connect_Btn.setIconSize(QSize(150, 150))
        self.Tor_Btn = QPushButton(self.centralwidget)
        self.Tor_Btn.setObjectName(u"Tor_Btn")
        self.Tor_Btn.setGeometry(QRect(750, 60, 40, 40))
        self.Tor_Btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"resources/emojipng.com-2364600.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Tor_Btn.setIcon(icon6)
        self.Tor_Btn.setIconSize(QSize(35, 35))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(710, 70, 31, 21))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
"background: transparent\n"
"}")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(750, 120, 40, 40))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"resources/PngItem_3774350.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(35, 35))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(650, 130, 91, 16))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel{\n"
"background: transparent\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.Logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Q VPN.</span></p></body></html>", None))
        self.F_B.setText("")
        self.T_T.setText("")
        self.Git.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">CURRENT IP :</span></p></body></html>", None))
        self.Crnt_Ip.setText("")
        self.connect_Btn.setText("")
        self.Tor_Btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">TOR</span></p></body></html>", None))
        self.pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">SPEED TEST</span></p></body></html>", None))
    # retranslateUi

