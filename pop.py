import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.resize(600, 500)
        self.browser = QWebEngineView()
<<<<<<< HEAD
        self.browser.setUrl(QUrl('https://google.com/'))
=======
        self.browser.setUrl(QUrl('http://google.com'))
>>>>>>> c6bb463a0eda2a3015b9f52cd093440d610e2301
        self.setCentralWidget(self.browser)
        self.setWindowIcon(QtGui.QIcon('ad.png'))
        self.show()


app = QApplication(sys.argv)
QApplication.setApplicationName('AdBlock')
window = MainWindow()
app.exec_()
