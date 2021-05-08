#  [MAIN FILE]
# ______________________________________________________________
# PRODUCT : Q VPN

# NAME    : main.py [UI STARTS]

# AUTHORS : ANANDAN , OMAR , SREERAG
# _______________________________________________________________


import sys
import platform
from PyQt5.QtCore import *
# from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from subprocess import *
import threading
import os
import requests
import speedtest

## SPLASH SCREEN
from ui_splash_screen import Ui_splashscreen

## MAIN WINDOW

from ui_main import Ui_MainWindow

counter = 0  # GLOBALS


# SPLASH SCREEN
class splashscreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.sp = Ui_splashscreen()
        self.sp.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setXOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.sp.dropshadowframe.setGraphicsEffect(self.shadow)

        # QTimer START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        # Timer in millisecond
        self.timer.start(35)

        # CHANGE DESCRIPTION OF SPLASH SCREEN

        # INITIAL TEXT
        self.sp.label_description.setText("FAST AND SECURE")

        # CHANGE TEXT
        QtCore.QTimer.singleShot(1500, lambda: self.sp.label_description.setText("<strong>LOADING</strong> SERVERS"))
        QtCore.QTimer.singleShot(3000,
                                 lambda: self.sp.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))

        # SHOW Main Window
        self.show()

    # AppFunctions
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.sp.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


# MAIN WINDOW [APPLICATION]
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Tor_Btn.setCheckable(True)
        self.ui.connect_Btn.clicked.connect(self.on_click)
        self.ui.Tor_Btn.clicked.connect(self.on_Tor)
        self.ui.speed_Test.clicked.connect(self.check_speed)

        # PAGE 2
        self.ui.btn_faq.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_about.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # FROM PAGE_2 to PAGE_1
        self.ui.btn_home_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # FROM PAGE_3 to PAGE_1
        self.ui.btn_home_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # DISPLAY IP ADDRESS WHEN MAIN WINDOW IS LOADED
        self.on_ip()

        # WG OFF BUTTON
        self.ui.off_btn.clicked.connect(self.wgDown)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # TOP PANEL
        self.ui.miniNew.clicked.connect(lambda: self.showMinimized())
        self.ui.closeNew.clicked.connect(lambda: self.close())

        # MOVE WINDOW
        def moveWindow(event):
            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.top_bar.mouseMoveEvent = moveWindow

    def on_click(self):
        # To disable the button
        self.ui.connect_Btn.setEnabled(False)
        self.ui.off_btn.show()
        self.ui.off_btn.setEnabled(True)

        # THREADING
        self.connectThread = threading.Thread(target=self.wgConnect)
        self.connectThread.start()

        # Wg UP
    def wgConnect(self):
        process = Popen(["C:\Program Files\WireGuard\wireguard.exe", '/installtunnelservice',
                         "C:\Program Files\WireGuard\Data\Configurations\wg1.conf.dpapi"], stdout=PIPE,
                        encoding='utf-8')
        print("CONNECTED")

        # TO PRINT IP AFTER WG IS CONNECTED
        self.on_ip()
        self.ui.connect_Btn.hide()

    # WG DOWN
    def wgDown(self):
        self.ui.off_btn.setEnabled(False)
        process = Popen(["C:\Program Files\WireGuard\wireguard.exe", '/uninstalltunnelservice', "wg1"], stdout=PIPE,
                        encoding='utf-8')
        print("SESSION ENDED")
        self.ui.off_btn.hide()
        self.ui.connect_Btn.setEnabled(True)
        self.ui.connect_Btn.show()

    # IP THREAD
    def on_ip(self):
        self.ip_Thread = threading.Thread(target=self.run)
        # self.ip_thread.out_string.connect(self.printIP)
        self.ip_Thread.start()

    # FETCH IP
    def run(self):
        self.ui.iptext.clear()
        try:
            ipaddress = requests.get("http://ipecho.net/plain?").text
            print(ipaddress)

            try:
                # self.ui.iptext.
                self.ui.iptext.appendPlainText(ipaddress)
                # Enabling the connect button
                #
            except:
                print("Please wait")
        except:
            print("Check your internet Connection")

    # TOR THREAD
    def on_Tor(self):
        if self.ui.Tor_Btn.isChecked():
            self.tor_Thread = threading.Thread(target=self.torConnect)
            self.tor_Thread.start()
        else:
            self.tor_Thread = threading.Thread(target=self.torDisconnect)
            self.tor_Thread.start()
    # TOR CONNECTION
    def torConnect(self):
        process = Popen(['sc', 'start', 'tor'])
        print("tor successfully connected")
        self.on_ip()

    def torDisconnect(self):
        process = Popen(['sc', 'stop', 'tor'])
        self.on_ip()
    # SPEED_TEST THREAD
    def check_speed(self):
        self.speedThread = threading.Thread(target=self.get_speedTest)
        self.speedThread.start()

    # GET INTERNET SPEED
    def get_speedTest(self):
        try:
            speed = speedtest.Speedtest()
            print("processing..........")
            # self.process.terminate()
            # print("processing..........")
            sp = speed.download() / 1024 / 1024
            print(sp)

        except:
            print('check your internet connection for speed test')

    # APP EVENTS [DRAG MAIN WINDOW]
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

# EXIT
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = splashscreen()
    sys.exit(app.exec_())
