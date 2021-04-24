####infoquestinc#####

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import(QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import threading
import os
import requests



## SPLASH SCREEN
from ui_splash_screen import Ui_splashscreen

## MAIN WINDOW

from ui_main import Ui_MainWindow


## GLOBALS
counter = 0

# SPLASH SCREEN
class splashscreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.sp = Ui_splashscreen()
        self.sp.setupUi(self)

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
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.sp.dropshadowframe.setGraphicsEffect(self.shadow)

        ## QTIMER START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # Timer in millisec
        self.timer.start(35)


    #CHANGE DESCRIPTION

        #INITIAL TEXT
        self.sp.label_description.setText("FAST AND SECURE")

        #CHANGE TEXT
        QtCore.QTimer.singleShot(1500, lambda: self.sp.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.sp.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))




        ## SHOW Main Window
        ###############################################################
        self.show()
        ## END#########
    ## AppFunctions
    #####################################################################
    def progress(self):


        global counter

        # SET VALUE TO PROGRESS BAR


        self.sp.progressBar.setValue(counter)


        # CLOSE SPLASH SCREEN AND OPEN APP

        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            #SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()


            #CLOSE SPLASH SCREEN
            self.close()


        # INCREASE COUNTER

        counter += 1




# APPLICATION
class MainWindow(QMainWindow):
        def __init__(self):
            QMainWindow.__init__(self)
            buffer = 0
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.connect_Btn.clicked.connect(self.on_click)
            self.ui.Tor_Btn.clicked.connect(self.on_Tor)
            # Display the ip address when the MainWindow loaded
            self.on_ip()

            ## REMOVE TITLE BAR
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            # TOP PANEL
            self.ui.miniNew.clicked.connect(lambda: self.showMinimized())
            self.ui.closeNew.clicked.connect(lambda: self.close())

            #MOVE WINDOW
            self.ui.top_bar.mouseMoveEvent = moveWindow

            def moveWindow(event):
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

            def mousePressEvent(self, event):
                self.dragPos = event.globalPos()






        def on_ip(self):
            self.ip_Thread = threading.Thread(target=self.run)
            #self.ip_thread.out_string.connect(self.printIP)
            self.ip_Thread.start()

        def run(self):
            self.ui.iptext.clear()
            try:
                ipaddress = requests.get("http://ipecho.net/plain?").text
                print(ipaddress)

                try:
                    #self.ui.iptext.
                    self.ui.iptext.appendPlainText(ipaddress)
                    # Enabling the connect button
                    self.ui.connect_Btn.setEnabled(True)
                except:
                    print("Please wait")
            except:
                print("Check your internet Connection")






        def on_Tor(self):
            self.tor_Thread = threading.Thread(target=self.torConnect)
            self.tor_Thread.start()

        def on_click(self):
            # To disable the button
            self.ui.connect_Btn.setEnabled(False)
            # threading
            self.connectThread =threading.Thread(target=self.wgConnect)
            self.connectThread.start()

        def on_speed(self):
            self.speedThread = threading.Thread(target=self.get_speedTest)
            self.speedThread.start()

        def torConnect(self):
            buffer = 1
            print("tor successfully connected ")


        def wgConnect(self):
            print("Connected")
            # to display the ip after wg connected
            self.on_ip()


        def get_speedTest(self):
           try:
            os.system('cmd /k ""')

           except:
               print('check')

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = splashscreen()
    sys.exit(app.exec_())

