####infoquestinc#####

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import(QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


## SPLASH SCREEN
from ui_splash_screen import Ui_splashscreen

## MAIN WINDOW

from ui_main import Ui_MainWindow

## GLOBALS
counter = 0

# APPLICATION
class MainWIndow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # MAIN WINDOW LABEL
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>LOL</strong>"))
        QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))

# SPLASH SCREEN
class splashscreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_splashscreen()
        self.ui.setupUi(self)

        ########## UI INTERFACE CODES
        ##########################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setXOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        self.ui.dropshadowframe.setGraphicsEffect(self.shadow)

        ## QTIMER START
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # Timer in millisec
        self.timer.start(35)


    #CHANGE DESCRIPTION

        #INITIAL TEXT
        self.ui.label_description.setText("FAST AND SECURE")

        #CHANGE TEXT
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))




        ## SHOW Main Window
        ###############################################################
        self.show()
        ## END#########
    ## AppFunctions
    #####################################################################
    def progress(self):


        global counter

        # SET VALUE TO PROGRESS BAR


        self.ui.progressBar.setValue(counter)


        # CLOSE SPLASH SCREEN AND OPEN APP

        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            #SHOW MAIN WINDOW
            self.main = MainWIndow()
            self.main.show()


            #CLOSE SPLASH SCREEN
            self.close()


        # INCREASE COUNTER

        counter += 1

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = splashscreen()
    sys.exit(app.exec_())

