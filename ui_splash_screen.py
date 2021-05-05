# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenNlNRjp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_splashscreen(object):
    def setupUi(self, splashscreen):
        if not splashscreen.objectName():
            splashscreen.setObjectName(u"splashscreen")
        splashscreen.resize(689, 394)
        self.centralwidget = QWidget(splashscreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropshadowframe = QFrame(self.centralwidget)
        self.dropshadowframe.setObjectName(u"dropshadowframe")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.dropshadowframe.setFont(font)
        self.dropshadowframe.setStyleSheet(u"QFrame{\n"
"background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.dropshadowframe.setFrameShape(QFrame.StyledPanel)
        self.dropshadowframe.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropshadowframe)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 90, 661, 61))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(40)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropshadowframe)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 160, 661, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        self.label_description.setFont(font2)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropshadowframe)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(60, 260, 551, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(98, 114, 164);\n"
"    color:rgb(200, 200, 200);\n"
"	border-radius:10px;\n"
"	text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:1, y2:0.512, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropshadowframe)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(10, 290, 651, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.label_loading.setFont(font3)
        self.label_loading.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropshadowframe)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(20, 330, 631, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        self.label_credits.setFont(font4)
        self.label_credits.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropshadowframe)

        splashscreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(splashscreen)

        QMetaObject.connectSlotsByName(splashscreen)
    # setupUi

    def retranslateUi(self, splashscreen):
        splashscreen.setWindowTitle(QCoreApplication.translate("splashscreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("splashscreen", u"<strong>Q</strong> VPN", None))
        self.label_description.setText(QCoreApplication.translate("splashscreen", u"FAST AND SECURE", None))
        self.label_loading.setText(QCoreApplication.translate("splashscreen", u"loading...", None))
        self.label_credits.setText(QCoreApplication.translate("splashscreen", u"<strong>Infoquest</strong> inc", None))
    # retranslateUi
