# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maindNbTZG.ui'
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
        MainWindow.setStyleSheet(u"background-color: rgb(23, 33, 59);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 30, 801, 571))
        self.label_2.setStyleSheet(u"")
        self.label_2.setLineWidth(1)
        self.label_2.setPixmap(QPixmap(u"../../Q-VPN-secondary/resources/vpnbg.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 111, 21))
        font = QFont()
        font.setFamily(u"AvenirNext LT Pro Bold")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgba(0,0,0,0%)")
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
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
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../../Q-VPN-secondary/resources/clipart2939527.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"../../Q-VPN-secondary/resources/powerbutton.png", QSize(), QIcon.Normal, QIcon.On)
        self.connect_Btn.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u"../../Q-VPN-secondary/resources/emojipng.com-2364600.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Tor_Btn.setIcon(icon1)
        self.Tor_Btn.setIconSize(QSize(35, 35))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(710, 70, 31, 21))
        self.label.setFont(font)
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
        icon2 = QIcon()
        icon2.addFile(u"../../Q-VPN-secondary/resources/PngItem_3774350.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(35, 35))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(650, 130, 91, 16))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel{\n"
"background: transparent\n"
"}")
        self.iptext = QPlainTextEdit(self.centralwidget)
        self.iptext.setObjectName(u"iptext")
        self.iptext.setGeometry(QRect(130, 60, 131, 31))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.iptext.setPalette(palette)
        self.iptext.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"background-color: rgba(0,0,0,0%);\n"
"border-radius: 0px;\n"
"}")
        self.iptext.setLineWidth(0)
        self.iptext.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.iptext.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.iptext.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.iptext.setReadOnly(True)
        self.iptext.setBackgroundVisible(True)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 801, 41))
        self.top_bar.setStyleSheet(u"background-color: rgb(34, 31, 14);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.Logo = QLabel(self.top_bar)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(360, 0, 81, 41))
        font1 = QFont()
        font1.setFamily(u"AvenirNext LT Pro Bold")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.Logo.setFont(font1)
        self.Logo.setStyleSheet(u"QLabel{\n"
"\n"
"background-color: rgba(0,0,0,0%)\n"
"\n"
"}")
        self.Logo.setAlignment(Qt.AlignCenter)
        self.F_B = QPushButton(self.top_bar)
        self.F_B.setObjectName(u"F_B")
        self.F_B.setGeometry(QRect(660, 10, 21, 23))
        self.F_B.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"resources/face.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.F_B.setIcon(icon3)
        self.F_B.setIconSize(QSize(20, 20))
        self.T_T = QPushButton(self.top_bar)
        self.T_T.setObjectName(u"T_T")
        self.T_T.setGeometry(QRect(690, 10, 21, 23))
        self.T_T.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"resources/tweet.png", QSize(), QIcon.Normal, QIcon.Off)
        self.T_T.setIcon(icon4)
        self.T_T.setIconSize(QSize(20, 20))
        self.Git = QPushButton(self.top_bar)
        self.Git.setObjectName(u"Git")
        self.Git.setGeometry(QRect(720, 10, 31, 21))
        self.Git.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"resources/GitHub-Mark-Light-64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Git.setIcon(icon5)
        self.Git.setIconSize(QSize(20, 20))
        self.Git_3 = QPushButton(self.top_bar)
        self.Git_3.setObjectName(u"Git_3")
        self.Git_3.setGeometry(QRect(740, 0, 61, 41))
        self.Git_3.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"resources/GitHub_Logo_White.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Git_3.setIcon(icon6)
        self.Git_3.setIconSize(QSize(55, 55))
        self.insta = QPushButton(self.top_bar)
        self.insta.setObjectName(u"insta")
        self.insta.setGeometry(QRect(630, 10, 21, 21))
        self.insta.setStyleSheet(u"QPushButton{\n"
"background: transparent\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"resources/icons8-instagram.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.insta.setIcon(icon7)
        self.insta.setIconSize(QSize(30, 30))
        self.closeNew = QPushButton(self.top_bar)
        self.closeNew.setObjectName(u"closeNew")
        self.closeNew.setGeometry(QRect(10, 10, 16, 16))
        self.closeNew.setStyleSheet(u"QPushButton {\n"
"    \n"
"    \n"
"	background-color: rgb(255, 96, 88);\n"
"    border-radius: 8px;\n"
"    \n"
"   }\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}")
        self.miniNew = QPushButton(self.top_bar)
        self.miniNew.setObjectName(u"miniNew")
        self.miniNew.setGeometry(QRect(40, 10, 16, 16))
        self.miniNew.setStyleSheet(u"\n"
"QPushButton {\n"
"    \n"
"    \n"
"	background-color: rgb(255, 190, 47);\n"
"    border-radius: 8px;\n"
"    \n"
"   }\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">CURRENT IP :</span></p></body></html>", None))
        self.connect_Btn.setText("")
        self.Tor_Btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">TOR</span></p></body></html>", None))
        self.pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">SPEED TEST</span></p></body></html>", None))
        self.Logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Q VPN</span></p></body></html>", None))
        self.F_B.setText("")
        self.T_T.setText("")
        self.Git.setText("")
        self.Git_3.setText("")
        self.insta.setText("")
#if QT_CONFIG(tooltip)
        self.closeNew.setToolTip(QCoreApplication.translate("MainWindow", u"close", None))
#endif // QT_CONFIG(tooltip)
        self.closeNew.setText("")
#if QT_CONFIG(tooltip)
        self.miniNew.setToolTip(QCoreApplication.translate("MainWindow", u"minimize", None))
#endif // QT_CONFIG(tooltip)
        self.miniNew.setText("")
    # retranslateUi

