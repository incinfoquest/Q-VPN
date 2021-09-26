# ______________________________________________________________
# PRODUCT : Q VPN

# NAME    : pop.py [PyHole DASH BOARD]

# AUTHORS : ANANDAN , OMAR , SREERAG

# CHANGES TO THIS FILE ARE PROHIBITED
# _______________________________________________________________


import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import *
from PySide2 import QtGui
from PySide2 import QtCore

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
