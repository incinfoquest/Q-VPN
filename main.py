# ______________________________________________________________|
#                                                               |
# [MAIN FILE]                                                   |                                               |
# ______________________________________________________________|
# PRODUCT : Q VPN                                               |
#                                                               |
# NAME    : main.py [UI STARTS]                                 |
#                                                               |
# AUTHORS : ANANDAN , OMAR , SREERAG                            |
# ______________________________________________________________|


import sys
import platform
# from PyQt5.QtCore import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
# from PyQt5.QtWidgets import QApplication
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from subprocess import Popen, PIPE
from playsound import playsound
import webbrowser
import threading
import os
import requests
import speedtest
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

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
        #self.ui.connect_Btn.setCheckable(True)
        self.ui.connect_Btn.clicked.connect(self.on_click)
        self.ui.Tor_Btn.clicked.connect(self.on_Tor)
        self.ui.speed_Test.clicked.connect(self.check_speed)
        self.ui.pop_btn.clicked.connect(self.pop)
        self.ui.reddit_Btn.clicked.connect(lambda: webbrowser.open('https://www.reddit.com/user/InQuest_inc'))
        self.ui.tweet_Btn.clicked.connect(lambda: webbrowser.open('https://twitter.com/Info43913522'))
        self.ui.git_Btn.clicked.connect(lambda: webbrowser.open('https://github.com/incinfoquest'))
        self.ui.insta_Btn.clicked.connect(lambda: webbrowser.open('https://www.instagram.com/inquest_inc/'))
        self.ui.dwnld_label.hide()
        self.ui.C_label.setHidden(True)
        self.ui.upnld_label.hide()
        self.ui.pop_btn.setEnabled(False)
        self.ui.pop_label.hide()
        self.timer = QtCore.QTimer()
        # STACK

        # PAGE 3
        self.ui.btn_about.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # FROM PAGE_3 to PAGE_1
        self.ui.btn_home_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # DISPLAY IP ADDRESS WHEN MAIN WINDOW IS LOADED
        self.on_ip()

        # WG OFF BUTTON
        self.ui.off_btn.clicked.connect(self.on_Down)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # TOP PANEL
        self.ui.miniNew.clicked.connect(lambda: self.showMinimized())
        self.ui.closeNew.clicked.connect(lambda: self.close())

        # SET TITLE BAR
        self.ui.top_bar.mouseMoveEvent = self.moveWindow

    def checkInternetRequests(self, url='http://www.google.com/', timeout=3):
        try:
            self.ui.except_lbl.clear()
            r = requests.head(url, timeout=timeout)
            print(r)
            return True
        except:
            self.ui.except_lbl.setText("Check Your Network Connection")
            playsound('beep_beep.mp3')


        # MOVE WINDOW
    def moveWindow(self, event):
        # IF LEFT CLICK MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    # APP EVENTS [DRAG MAIN WINDOW]
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def time_convert(self, sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))
        ti = "{0}:{1}:{2}".format(int(hours),int(mins),int(sec))
        self.ui.C_label.setHidden(False)
        self.ui.time_label.setText("Connection Time " + ti)

    def on_click(self):
        # checking network connection

        if self.checkInternetRequests():

            self.ui.pop_btn.setEnabled(True)

            self.ui.pop_label.show()

            self.ui.C_label.setHidden(True)

            playsound('message_dot.mp3')


    # To disable the button
            self.ui.connect_Btn.setEnabled(False)
            self.ui.off_btn.show()
            self.ui.off_btn.setEnabled(True)
            self.ui.time_label.clear()
            self.start_time = time.time()
            # THREADING
            self.connectThread = threading.Thread(target=self.wgConnect)
            self.connectThread.start()


    def on_Down(self):
         self.ui.pop_btn.setEnabled(False)
         self.ui.pop_label.hide()
         playsound('off.mp3')
         self.end_time = time.time()
         self.time_lapsed = self.end_time - self.start_time
         self.time_convert(self.time_lapsed)
         self.ui.pop_btn.setEnabled(False)
         self.disconnectThread = threading.Thread(target=self.wgDown)
         self.disconnectThread.start()


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

        process = Popen(["C:\Program Files\WireGuard\wireguard.exe", '/uninstalltunnelservice', "wg1"], stdout=PIPE,
                        encoding='utf-8')
        print("SESSION ENDED")
        self.ui.off_btn.hide()
        self.ui.connect_Btn.setEnabled(True)
        self.ui.connect_Btn.show()
        self.on_ip()



    # IP THREAD
    def on_ip(self):
        self.ip_Thread = threading.Thread(target=self.run)
        self.ip_Thread.start()

    # FETCH IP
    def run(self):
        self.ui.iptext.setText("Fetching IP")
        time.sleep(10)
        self.ui.iptext.clear()
        self.ui.iptext.setText("Fetching IP")


        try:
            ipaddress = requests.get("http://ipecho.net/plain?").text
            print(ipaddress)
            self.ui.iptext.setText(ipaddress)

        except:
            try:
                ipaddress = requests.get("http://ipconfig.in/ip").text
                print(ipaddress)
                self.ui.iptext.setText(ipaddress)
            except:
                print("Check your internet Connection")
                playsound('beep_beep.mp3')
                self.ui.except_lbl.setText("Check Your Network Connection")

    # TOR THREAD
    def on_Tor(self):
            self.tor_Thread = threading.Thread(target=self.torConnect)
            self.tor_Thread.start()

    # TOR CONNECTION
    def torConnect(self):

        torexe = os.popen(r'C:\Program Files\Tor Browser\Browser\firefox.exe')
        self.showMinimized()

    def pop(self):

        os.system('python pop.py')


    # SPEED_TEST THREAD
    def check_speed(self):
        self.speedThread = threading.Thread(target=self.get_speedTest)
        self.speedThread.start()



    # GET INTERNET SPEED
    def get_speedTest(self):
        try:

            speed = speedtest.Speedtest()
            self.ui.except_lbl.clear()
            self.ui.su_label.clear()
            print("processing..........")

            # Download Speed
            self.ui.dwnld_label.show()
            self.ui.sp_label.setText("Retrieving Download")
            sp = "{:.2f}".format(speed.download()/ 1024/ 1024)
            print(sp + " mb/s")
            self.ui.sp_label.setText(sp + " Mbps ")

            # Upload Speed
            self.ui.upnld_label.show()
            self.ui.su_label.clear()
            self.ui.su_label.setText("Retrieving Upload")
            su = "{:.2f}".format(speed.upload()/ 1024/ 1024)
            print(su + "mb/s")
            self.ui.su_label.setText(su + " Mbps ")

        except:
            print("check your internet connection for speed test")
            playsound('beep_beep.mp3')
            self.ui.except_lbl.setText("Check Your Network Connection")


    # EXIT
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = splashscreen()
    sys.exit(app.exec_())
