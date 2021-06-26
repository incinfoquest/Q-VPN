import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)

web = QWebEngineView()

web.load(QUrl("https://www.tutorialspoint.com/How-can-I-make-one-Python-file-run-another"))

web.show()

sys.exit(app.exec_())