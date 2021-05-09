# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAYJucc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(23, 33, 59);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 801, 41))
        self.top_bar.setStyleSheet(u"background-color: rgb(34, 31, 14);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.Logo = QLabel(self.top_bar)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(360, 0, 81, 41))
        font = QFont()
        font.setFamily(u"AvenirNext LT Pro Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(QFont.Bold)
        self.Logo.setFont(font)
        self.Logo.setStyleSheet(u"QLabel{\n"
"\n"
"background-color: rgba(0,0,0,0%)\n"
"\n"
"}")
        self.Logo.setAlignment(Qt.AlignCenter)
        self.closeNew = QPushButton(self.top_bar)
        self.closeNew.setObjectName(u"closeNew")
        self.closeNew.setGeometry(QRect(10, 10, 16, 16))
        self.closeNew.setStyleSheet(u"QPushButton {\n"
"    \n"
"    \n"
"	background-color: rgb(255, 96, 88);\n"
"    border-radius: 8px;\n"
"    \n"
"   }\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}")
        self.miniNew = QPushButton(self.top_bar)
        self.miniNew.setObjectName(u"miniNew")
        self.miniNew.setGeometry(QRect(40, 10, 16, 16))
        self.miniNew.setStyleSheet(u"\n"
"QPushButton {\n"
"    \n"
"    \n"
"	background-color: rgb(255, 190, 47);\n"
"    border-radius: 8px;\n"
"    \n"
"   }\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 255, 0);\n"
"\n"
"}")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 40, 801, 561))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.back_img_1 = QLabel(self.page_1)
        self.back_img_1.setObjectName(u"back_img_1")
        self.back_img_1.setGeometry(QRect(0, 0, 801, 561))
        self.back_img_1.setPixmap(QPixmap(u"resources/vpnbg.png"))
        self.back_img_1.setScaledContents(True)
        self.connect_Btn = QPushButton(self.page_1)
        self.connect_Btn.setObjectName(u"connect_Btn")
        self.connect_Btn.setGeometry(QRect(320, 190, 160, 160))
        self.connect_Btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 80px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(48, 154, 38);\n"
"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"resources/power.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connect_Btn.setIcon(icon)
        self.connect_Btn.setIconSize(QSize(150, 150))
        self.ip_label = QLabel(self.page_1)
        self.ip_label.setObjectName(u"ip_label")
        self.ip_label.setGeometry(QRect(10, 30, 111, 21))
        font1 = QFont()
        font1.setFamily(u"AvenirNext LT Pro Bold")
        font1.setBold(True)
        font1.setWeight(QFont.Bold)
        self.ip_label.setFont(font1)
        self.ip_label.setStyleSheet(u"background-color: rgba(0,0,0,0%)")
        self.ip_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.iptext = QPlainTextEdit(self.page_1)
        self.iptext.setObjectName(u"iptext")
        self.iptext.setGeometry(QRect(120, 30, 131, 21))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.iptext.setPalette(palette)
        font2 = QFont()
        font2.setFamily(u"CrashNumberingGothic")
        font2.setPointSize(12)
        self.iptext.setFont(font2)
        self.iptext.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"background-color: rgba(0,0,0,0%);\n"
"border-radius: 0px;\n"
"}")
        self.iptext.setLineWidth(0)
        self.iptext.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.iptext.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.iptext.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.iptext.setReadOnly(True)
        self.iptext.setBackgroundVisible(True)
        self.tor_label = QLabel(self.page_1)
        self.tor_label.setObjectName(u"tor_label")
        self.tor_label.setGeometry(QRect(710, 30, 31, 21))
        self.tor_label.setFont(font1)
        self.tor_label.setStyleSheet(u"QLabel{\n"
"background: transparent\n"
"}")
        self.Tor_Btn = QPushButton(self.page_1)
        self.Tor_Btn.setObjectName(u"Tor_Btn")
        self.Tor_Btn.setGeometry(QRect(750, 20, 41, 40))
        self.Tor_Btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"resources/emojipng.com-2364600.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Tor_Btn.setIcon(icon1)
        self.Tor_Btn.setIconSize(QSize(35, 35))
        self.speed_label = QLabel(self.page_1)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setGeometry(QRect(650, 90, 91, 16))
        self.speed_label.setFont(font1)
        self.speed_label.setStyleSheet(u"QLabel{\n"
"background: transparent\n"
"}")
        self.speed_Test = QPushButton(self.page_1)
        self.speed_Test.setObjectName(u"speed_Test")
        self.speed_Test.setGeometry(QRect(750, 80, 40, 40))
        self.speed_Test.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"resources/PngItem_3774350.png", QSize(), QIcon.Normal, QIcon.Off)
        self.speed_Test.setIcon(icon2)
        self.speed_Test.setIconSize(QSize(35, 35))
        self.off_btn = QPushButton(self.page_1)
        self.off_btn.setObjectName(u"off_btn")
        self.off_btn.setGeometry(QRect(320, 190, 160, 160))
        self.off_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 80px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"resources/powerbutton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.off_btn.setIcon(icon3)
        self.off_btn.setIconSize(QSize(150, 150))
        self.btn_about = QPushButton(self.page_1)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setGeometry(QRect(750, 510, 40, 40))
        self.btn_about.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"resources/icons8-about-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon4)
        self.btn_about.setIconSize(QSize(30, 30))
        self.stackedWidget.addWidget(self.page_1)
        self.back_img_1.raise_()
        self.ip_label.raise_()
        self.iptext.raise_()
        self.tor_label.raise_()
        self.Tor_Btn.raise_()
        self.speed_label.raise_()
        self.speed_Test.raise_()
        self.off_btn.raise_()
        self.connect_Btn.raise_()
        self.btn_about.raise_()
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.back_img_3 = QLabel(self.page_3)
        self.back_img_3.setObjectName(u"back_img_3")
        self.back_img_3.setGeometry(QRect(0, 0, 801, 561))
        self.back_img_3.setPixmap(QPixmap(u"resources/2028632.jpg"))
        self.btn_home_2 = QPushButton(self.page_3)
        self.btn_home_2.setObjectName(u"btn_home_2")
        self.btn_home_2.setGeometry(QRect(10, 30, 50, 50))
        self.btn_home_2.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"resources/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home_2.setIcon(icon5)
        self.btn_home_2.setIconSize(QSize(35, 35))
        self.textBrowser = QTextBrowser(self.page_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(40, 100, 741, 291))
        self.textBrowser.setStyleSheet(u"\n"
"QTextBrowser{\n"
"\n"
"\n"
"background:transparent;\n"
"border:0px\n"
"\n"
"\n"
"\n"
"}\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    \n"
"	background-color: rgb(3, 52, 110);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	\n"
"	background-color: rgb(2, 58, 119);\n"
"	height: 15px;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	\n"
"	background-color: rgb(80, 80, 122);"
                        "\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	\n"
"	background-color: rgb(2, 58, 119);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	\n"
"	background-color: rgb(78, 78, 119);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}")
        self.tweet = QLabel(self.page_3)
        self.tweet.setObjectName(u"tweet")
        self.tweet.setGeometry(QRect(640, 520, 21, 21))
        self.tweet.setStyleSheet(u"QLabel{\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.tweet.setPixmap(QPixmap(u"resources/twitter_round.svg"))
        self.tweet.setScaledContents(True)
        self.git = QLabel(self.page_3)
        self.git.setObjectName(u"git")
        self.git.setGeometry(QRect(690, 520, 21, 21))
        self.git.setStyleSheet(u"QLabel{\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.git.setPixmap(QPixmap(u"resources/GitHub-Mark-Light-64px.png"))
        self.git.setScaledContents(True)
        self.tele = QLabel(self.page_3)
        self.tele.setObjectName(u"tele")
        self.tele.setGeometry(QRect(740, 520, 21, 21))
        self.tele.setStyleSheet(u"QLabel{\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.tele.setPixmap(QPixmap(u"resources/telegram.svg"))
        self.tele.setScaledContents(True)
        self.fsf = QLabel(self.page_3)
        self.fsf.setObjectName(u"fsf")
        self.fsf.setGeometry(QRect(50, 500, 191, 41))
        self.fsf.setStyleSheet(u"QLabel{\n"
"background:transparent;\n"
"}")
        self.fsf.setPixmap(QPixmap(u"resources/fsf-free-software-foundation.svg"))
        self.fsf.setScaledContents(True)
        self.reddit = QLabel(self.page_3)
        self.reddit.setObjectName(u"reddit")
        self.reddit.setGeometry(QRect(590, 520, 21, 21))
        self.reddit.setStyleSheet(u"QLabel{\n"
"\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.reddit.setPixmap(QPixmap(u"resources/Reddit Logo/On White/PNG/Reddit_Mark_OnWhite.png"))
        self.reddit.setScaledContents(True)
        self.lgpl_3 = QLabel(self.page_3)
        self.lgpl_3.setObjectName(u"lgpl_3")
        self.lgpl_3.setGeometry(QRect(290, 490, 131, 51))
        self.lgpl_3.setStyleSheet(u"QLabel{\n"
"\n"
"\n"
"background:transparent;\n"
"\n"
"\n"
"}")
        self.lgpl_3.setPixmap(QPixmap(u"resources/LGPLv3_Logo.svg"))
        self.lgpl_3.setScaledContents(True)
        self.mail = QLabel(self.page_3)
        self.mail.setObjectName(u"mail")
        self.mail.setGeometry(QRect(580, 470, 191, 41))
        font3 = QFont()
        font3.setFamily(u"AvenirNext LT Pro Regular")
        font3.setBold(False)
        font3.setWeight(QFont.Bold)
        self.mail.setFont(font3)
        self.mail.setStyleSheet(u"QLabel{\n"
"\n"
"\n"
"background:transparent;\n"
"\n"
"\n"
"}")
        self.mail.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Q VPN</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.closeNew.setToolTip(QCoreApplication.translate("MainWindow", u"close", None))
#endif // QT_CONFIG(tooltip)
        self.closeNew.setText("")
#if QT_CONFIG(tooltip)
        self.miniNew.setToolTip(QCoreApplication.translate("MainWindow", u"minimize", None))
#endif // QT_CONFIG(tooltip)
        self.miniNew.setText("")
        self.back_img_1.setText("")
#if QT_CONFIG(tooltip)
        self.connect_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"CONNECT", None))
#endif // QT_CONFIG(tooltip)
        self.connect_Btn.setText("")
        self.ip_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">CURRENT IP :</span></p></body></html>", None))
        self.tor_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">TOR</span></p></body></html>", None))
        self.Tor_Btn.setText("")
        self.speed_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">SPEED TEST</span></p></body></html>", None))
        self.speed_Test.setText("")
#if QT_CONFIG(tooltip)
        self.off_btn.setToolTip(QCoreApplication.translate("MainWindow", u"DISCONNECT", None))
#endif // QT_CONFIG(tooltip)
        self.off_btn.setText("")
        self.btn_about.setText("")
        self.back_img_3.setText("")
        self.btn_home_2.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Here in this we are providing network level protection for all users that connect with our  Q VPN. it  is intended to generate user friendly VPN without interrupting their browsing with no compromise in the protection of data and privacy.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">		In this application we are using the Wireguard protocol to connect with the server. The WireGuard is an extremely fast VPN protocol with very little overhead. It has the potential to offer a simpler, more secure, more efficient, and easier to use VPN over existing technologies. The WireGuard protocol is 58% faster than the OpenVPN protocol and also the Wireguard is extremely stable and robust. It can easily switch the server while maintaining the connection. Clients can also change the networks without dropping the connection. Rather than other VPN protocols the WireGuard protocol has fewer codes to establish the connection. And also the WireGuard\u2019s performance improvement over OpenVPN is greater with low latency servers in comparison to high latency server locations. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; m"
                        "argin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">		</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">		The next main feature of our \u201c Q \u201c, is we are providing the TOR service along with the VPN service. The user can decide whether he/she wants to connect the internet using VPN or TOR. Default we are connecting with the VPN but if the user wants to switch to TOR service, they only want to click the TOR button. TOR is useful for anyone who wants to keep their internet activities out of the hands of advertisers, ISPs, and websites.</span></p></body></html>", None))
        self.tweet.setText("")
        self.git.setText("")
        self.tele.setText("")
        self.fsf.setText("")
        self.reddit.setText("")
        self.lgpl_3.setText("")
        self.mail.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">incinfoquest@gmail.com</span></p></body></html>", None))
    # retranslateUi

