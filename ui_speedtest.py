# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'speedtestCiVnow.ui'
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
        MainWindow.resize(584, 515)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setGeometry(QRect(0, 30, 591, 491))
        self.body.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 591, 31))
        self.frame_2.setStyleSheet(u"background-color: rgb(34, 31, 14);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.closeNew = QPushButton(self.frame_2)
        self.closeNew.setObjectName(u"closeNew")
        self.closeNew.setGeometry(QRect(10, 10, 10, 10))
        self.closeNew.setStyleSheet(u"QPushButton {\n"
"    \n"
"    \n"
"	background-color: rgb(255, 96, 88);\n"
"    border-radius: 5px;\n"
"    \n"
"   }\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.closeNew.setToolTip(QCoreApplication.translate("MainWindow", u"close", None))
#endif // QT_CONFIG(tooltip)
        self.closeNew.setText("")
    # retranslateUi

