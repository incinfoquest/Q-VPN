import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore

class PopWindow(QMainWindow):
    def __init__(self):
        super(PopWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.resize(600, 500)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://172.31.41.254/admin'))
        self.setCentralWidget(self.browser)
        self.setWindowIcon(QtGui.QIcon('ad.png'))
        self.show()

app = QApplication(sys.argv)
QApplication.setApplicationName('AdBlock')
p_window = PopWindow()
app.exec_()
