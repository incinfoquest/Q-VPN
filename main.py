# ______________________________________________________________|
#                                                               |
# [MAIN FILE]                                                   |
# ______________________________________________________________|
# PRODUCT : Q VPN                                               |
#                                                               |
# NAME    : main.py [UI STARTS]                                 |
#                                                               |
# AUTHORS : ANANDAN , OMAR , SREERAG                            |
# ______________________________________________________________|

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from subprocess import Popen, PIPE
from playsound import playsound
import webbrowser
import threading
import os
import requests
import speedtest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from win10toast import ToastNotifier
import time
import win32event
import win32api
from winerror import *



## SPLASH SCREEN
from ui_splash_screen import Ui_splashscreen

## MAIN WINDOW

from ui_main import Ui_MainWindow

counter = 0  # GLOBALS

mutex = win32event.CreateMutex(None, False, 'clamguard')
last_error = win32api.GetLastError()
if last_error == ERROR_ALREADY_EXISTS:
   print("An instance of ClamGuard is already running! Exiting this instance.")
   ctypes.windll.user32.MessageBoxW(0, u"An instance of ClamGuard is already running!", u"Error", 0)
   sys.exit(1)

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
        self.ui.pop_btn.clicked.connect(self.popup)
        self.ui.reddit_Btn.clicked.connect(lambda: webbrowser.open('https://www.reddit.com/user/InQuest_inc'))
        self.ui.tweet_Btn.clicked.connect(lambda: webbrowser.open('https://twitter.com/Info43913522'))
        self.ui.git_Btn.clicked.connect(lambda: webbrowser.open('https://github.com/incinfoquest'))
        self.ui.insta_Btn.clicked.connect(lambda: webbrowser.open('https://www.instagram.com/inquest_inc/'))
        self.ui.mail_Btn.clicked.connect(lambda: webbrowser.open('https://mail.google.com/mail/u/0/#inbox?compose=new'))
        self.ui.site.clicked.connect(lambda: webbrowser.open('https://incinfoquest.godaddysites.com'))
        self.ui.ref.clicked.connect(self.refresh)
        self.ui.dwnld_label.hide()
        self.ui.C_label.setHidden(True)
        self.ui.upnld_label.hide()
        self.ui.pop_btn.setEnabled(False)
        self.ui.pop_btn.setHidden(True)
        self.ui.pop_label.hide()
        self.timer = QtCore.QTimer()
        self.t = ToastNotifier()
        # Checking the test.txt file is empty or not for status finding

        self.fi = "test.txt"
        if os.stat(self.fi).st_size != 0:
            self.st_thread()

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


# Status Checking Thread
    def st_thread(self):

        self.disconnectThread = threading.Thread(target=self.status)
        self.disconnectThread.start()

    # Changing the status of the Wg is up
    def status(self):
        self.ui.connect_Btn.setEnabled(False)
        self.ui.off_btn.show()
        self.ui.off_btn.setEnabled(True)
        self.ui.ext_btn.clear()
        self.ui.connect_Btn.hide()
        self.ui.pop_btn.setHidden(False)

        self.ui.pop_btn.setEnabled(True)
        self.ui.pop_label.show()

        self.ui.C_label.setHidden(True)



# To check the Network is on
    def checkInternetRequests(self, url='http://www.google.com/', timeout=3):
        try:
            self.ui.except_lbl.clear()
            r = requests.head(url, timeout=timeout)
            print(r)
            return True
        except:
            self.ui.except_lbl.setText("Check Your Network Connection")
            playsound('beep_beep.mp3')

# Refreshing the labels
    def refresh(self):
        self.ui.ext_btn.clear()
        self.ui.crnt_ip.clear()
        self.on_ip()
        self.ui.except_lbl.clear()
        self.ui.su_label.clear()
        self.ui.sp_label.clear()
        self.ui.dwnld_label.hide()
        self.ui.upnld_label.hide()
        self.ui.time_label.hide()
        self.ui.C_label.hide()


    def time_convert(self, sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))
        ti = "{0}:{1}:{2}".format(int(hours),int(mins),int(sec))
        self.ui.C_label.setHidden(False)
        self.ui.time_label.show()
        self.ui.time_label.setText("Connection Time " + ti)

    def on_click(self):
        # checking network connection

         if self.checkInternetRequests():

            self.ui.time_label.clear()
            playsound('message_dot.mp3')

            # THREADING
            self.connectThread = threading.Thread(target=self.wgConnect)
            self.connectThread.start()


        # Wg UP
    def wgConnect(self):
        self.st_thread()
        process = Popen(["C:\Program Files\Q VPN\WireGuard\wireguard.exe", '/installtunnelservice',
                         "C:\Program Files\Q VPN\WireGuard\Data\Configurations\wg1.conf.dpapi"], stdout=PIPE,
                        encoding='utf-8')

        print("CONNECTED")

        # TO PRINT IP AFTER WG IS CONNECTED
        self.on_ip()
        # windows notifying
        self.t.show_toast("Q VPN","VPN Connected Successfully", icon_path="icon-console.ico",duration=3)
        # Writing the starting ip to the test.txt
        f = open ("test.txt", 'w', encoding = 'utf-8')
        self.start_time = time.time()
        # to store the value as in Floating point
        f.write('%f'%self.start_time)


    def on_Down(self):
         self.ui.pop_btn.setHidden(True)
         self.ui.pop_btn.setEnabled(False)
         self.ui.pop_label.hide()
         playsound('off.mp3')
         # open the test.txt file in read mode
         with open ("test.txt", 'r', encoding = 'utf-8') as f:
             self.start_time  = f.read()
             print(self.start_time)
         self.end_time = time.time()
         self.time_lapsed = self.end_time - float(self.start_time)
         self.time_convert(self.time_lapsed)
         self.ui.pop_btn.setEnabled(False)
         self.disconnectThread = threading.Thread(target=self.wgDown)
         self.disconnectThread.start()


    # WG DOWN
    def wgDown(self):

        process = Popen(["C:\Program Files\Q VPN\WireGuard\wireguard.exe", '/uninstalltunnelservice', "wg1"], stdout=PIPE,
                        encoding='utf-8')
        print("SESSION ENDED")
        self.ui.off_btn.hide()
        self.ui.connect_Btn.setEnabled(True)
        self.ui.connect_Btn.show()
        self.on_ip()
        self.t.show_toast("Q VPN","VPN DisConnected Successfully", icon_path="icon-console.ico",duration=3)
        # To clear the test.txt contents
        with open("test.txt", 'r+') as f:
            f.truncate(0)


    # IP THREAD
    def on_ip(self):
        self.ip_Thread = threading.Thread(target=self.run)
        self.ip_Thread.start()

    # FETCH IP
    def run(self):
        self.ui.crnt_ip.setText("FETCHING IP")
        time.sleep(10)


        try:
            ipaddress = requests.get("http://ipecho.net/plain?").text
            print(ipaddress)
            self.ui.crnt_ip.clear()
            self.ui.crnt_ip.setText("CURRENT IP :")
            self.ui.ext_btn.clear()
            self.ui.ext_btn.setText(ipaddress)

        except:
            try:
                ipaddress = requests.get("http://ipconfig.in/ip").text
                print(ipaddress)
                self.ui.crnt_ip.clear()
                self.ui.crnt_ip.setText("CURRENT IP :")
                self.ui.ext_btn.clear()
                self.ui.ext_btn.setText(ipaddress)
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
####
        torexe = os.popen(r'C:\Program Files\Q VPN\Tor Browser\Browser\firefox.exe')
        self.showMinimized()

# pi hole Adblocking window
    def popup(self):
        self.pop_Thread = threading.Thread(target=self.pop)
        self.pop_Thread.start()


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



    # EXIT
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = splashscreen()
    sys.exit(app.exec_())
