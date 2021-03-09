# ------------------  Main_frame.py -----------------------------

# Product : IQ Fast and secure
# developer : InfoQuest.inc
# created : March 2021

# imports
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import qdarkstyle
import requests


class WorkerThread(QThread):
    out_string = pyqtSignal(str)

    def run(self):

        try:
            ipaddress = requests.get("http://ipconfig.in/ip").text
            self.out_string.emit(ipaddress)
        except:
            print("Failed to obtain IP Address!")

class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(qdarkstyle.load_stylesheet())
        self.setGeometry(100, 100, 600, 400)
        self.button_show()

    # buttons used
    def button_show(self):
        button = QPushButton("CONNECT", self)
        button.resize(150, 150)
        button.setGeometry(200, 150, 200, 200)
        # button.setStyleSheet("background-color : green")
        # to circle the pushbutton
        button.setStyleSheet("border-radius : 100; border : 2px solid white")
        # button.move(400, 150)
        button.setFont(QFont('Times', 15))
        button.clicked.connect(self.on_click)
        button2 = QPushButton("Current IP", self)
        button2.resize(10, 50)
        button2.move(800, 60)
        button2.clicked.connect(self.on_ip)

        self.iptext = QPlainTextEdit(self)
        self.iptext.setFixedSize(150, 50)
        self.iptext.move(900, 60)
        self.iptext.setReadOnly(True)


        buttontor = QPushButton("TOR", self)
        buttontor.resize(100, 50)
        buttontor.setGeometry(700, 150, 200, 200)
        buttontor.setFont(QFont('Times', 15))
        buttontor.setStyleSheet("border-radius :100; border : 2px solid blue")
        buttontor.clicked.connect(self.on_tor)

        buttonsp = QPushButton("Internet speed", self)
        buttonsp.resize(80, 60)
        buttonsp.move(900, 550)
        buttonsp.clicked.connect(self.get_speed)
    def get_speed(self):
      print()

    def on_tor(self):
        print("TOR activated")

    def on_ip(self):
        self.ip_thread = WorkerThread()
        self.ip_thread.out_string.connect(self.printIP)
        self.ip_thread.start()

    def printIP(self, val):
        try:
            self.iptext.clear()
            #self.buffer = str(val)
            print(val)
            self.iptext.appendPlainText(val)
        except Exception as e:
            print(e)

    def on_click(self):
        print("Connected")


def main():
    app = QApplication(sys.argv)
    win = MainWidget()
    win.setFixedSize(1080, 900)
    win.setWindowTitle("vpn")
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
