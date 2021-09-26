# ______________________________________________________________
# PRODUCT : Q VPN

# NAME    : ui_main.py [MAIN UI]

# AUTHORS : ANANDAN , OMAR , SREERAG

# CHANGES TO THIS FILE ARE PROHIBITED
# _______________________________________________________________
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


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
        self.top_bar.setStyleSheet(u"background-color: rgb(43, 5, 83);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.Logo = QLabel(self.top_bar)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(360, 0, 81, 41))
        font = QFont()
        font.setFamily(u"AvenirNext LT Pro Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
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
        self.ref = QPushButton(self.top_bar)
        self.ref.setObjectName(u"ref")
        self.ref.setGeometry(QRect(760, 10, 20, 20))
        self.ref.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
" background-color : transparent; \n"
"border-radius: 10px;\n"
"\n"
" }\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(201, 230, 247);\n"
"};\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"resources/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ref.setIcon(icon)
        self.ref.setIconSize(QSize(24, 16))
        self.ref.setAutoExclusive(False)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 40, 801, 561))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.back_img_1 = QLabel(self.page_1)
        self.back_img_1.setObjectName(u"back_img_1")
        self.back_img_1.setGeometry(QRect(0, 0, 801, 561))
        font1 = QFont()
        font1.setFamily(u"AvenirNext LT Pro Regular")
        self.back_img_1.setFont(font1)
        self.back_img_1.setPixmap(QPixmap(u"resources/mainui1.png"))
        self.back_img_1.setScaledContents(True)
        self.back_img_1.setAlignment(Qt.AlignCenter)
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
"QPushButton:pressed{\n"
"\n"
"	background-color: rgb(0, 170, 0);\n"
"\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"resources/power.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connect_Btn.setIcon(icon1)
        self.connect_Btn.setIconSize(QSize(150, 150))
        self.crnt_ip = QLabel(self.page_1)
        self.crnt_ip.setObjectName(u"crnt_ip")
        self.crnt_ip.setGeometry(QRect(10, 30, 111, 31))
        font2 = QFont()
        font2.setFamily(u"AvenirNext LT Pro Bold")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.crnt_ip.setFont(font2)
        self.crnt_ip.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
" background-color : transparent; \n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
" };")
        self.crnt_ip.setAlignment(Qt.AlignCenter)
        self.tor_label = QLabel(self.page_1)
        self.tor_label.setObjectName(u"tor_label")
        self.tor_label.setGeometry(QRect(740, 40, 31, 21))
        font3 = QFont()
        font3.setFamily(u"AvenirNext LT Pro Bold")
        font3.setBold(True)
        font3.setWeight(75)
        self.tor_label.setFont(font3)
        self.tor_label.setStyleSheet(u"QLabel{\n"
"background: transparent\n"
"}")
        self.Tor_Btn = QPushButton(self.page_1)
        self.Tor_Btn.setObjectName(u"Tor_Btn")
        self.Tor_Btn.setGeometry(QRect(690, 30, 41, 40))
        self.Tor_Btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(125, 70, 152);\n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"	background-color: rgb(168, 132, 186);\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"resources/tor_br.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Tor_Btn.setIcon(icon2)
        self.Tor_Btn.setIconSize(QSize(35, 35))
        self.speed_label = QLabel(self.page_1)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setGeometry(QRect(700, 490, 91, 16))
        self.speed_label.setFont(font3)
        self.speed_label.setStyleSheet(u"QLabel{\n"
"background: transparent\n"
"}")
        self.speed_Test = QPushButton(self.page_1)
        self.speed_Test.setObjectName(u"speed_Test")
        self.speed_Test.setGeometry(QRect(650, 480, 40, 40))
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
"	\n"
"	background-color: rgb(53, 79, 79);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 85, 0);\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"resources/speed (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.speed_Test.setIcon(icon3)
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
"QPushButton:pressed{\n"
"\n"
"	background-color: rgb(85, 0, 0);\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"resources/powerbutton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.off_btn.setIcon(icon4)
        self.off_btn.setIconSize(QSize(150, 150))
        self.sp_label = QLabel(self.page_1)
        self.sp_label.setObjectName(u"sp_label")
        self.sp_label.setGeometry(QRect(430, 450, 171, 41))
        font4 = QFont()
        font4.setFamily(u"AvenirNext LT Pro Bold")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.sp_label.setFont(font4)
        self.sp_label.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
" background-color : transparent; \n"
"\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	color: rgb(120, 205, 212);\n"
" };\n"
"")
        self.sp_label.setAlignment(Qt.AlignCenter)
        self.time_label = QLabel(self.page_1)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(270, 150, 251, 31))
        self.time_label.setFont(font4)
        self.time_label.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
" background-color : transparent; \n"
"\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	color: rgb(50, 215, 54);\n"
" };\n"
"")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.btn_about = QPushButton(self.page_1)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setEnabled(True)
        self.btn_about.setGeometry(QRect(70, 480, 40, 40))
        self.btn_about.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(201, 230, 247);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(102, 204, 255);\n"
"\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"resources/information.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon5)
        self.btn_about.setIconSize(QSize(25, 25))
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 480, 61, 31))
        self.label.setFont(font3)
        self.label.setStyleSheet(u"QLabel{\n"
"\n"
"\n"
"background:transparent;\n"
"\n"
"\n"
"\n"
"}\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.except_lbl = QLabel(self.page_1)
        self.except_lbl.setObjectName(u"except_lbl")
        self.except_lbl.setGeometry(QRect(240, 10, 301, 51))
        self.except_lbl.setFont(font2)
        self.except_lbl.setStyleSheet(u"QLabel{\n"
"\n"
"background:transparent;\n"
"	\n"
"	color: rgb(255, 0, 0);\n"
"\n"
"}")
        self.except_lbl.setAlignment(Qt.AlignCenter)
        self.dwnld_label = QLabel(self.page_1)
        self.dwnld_label.setObjectName(u"dwnld_label")
        self.dwnld_label.setGeometry(QRect(610, 460, 31, 31))
        self.dwnld_label.setStyleSheet(u"QLabel{\n"
"\n"
"\n"
"background:transparent;\n"
"\n"
"\n"
"}")
        self.dwnld_label.setPixmap(QPixmap(u"resources/dwnld.png"))
        self.dwnld_label.setScaledContents(True)
        self.upnld_label = QLabel(self.page_1)
        self.upnld_label.setObjectName(u"upnld_label")
        self.upnld_label.setGeometry(QRect(610, 510, 31, 31))
        self.upnld_label.setStyleSheet(u"QLabel{\n"
"\n"
"\n"
"background:transparent;\n"
"\n"
"\n"
"}")
        self.upnld_label.setPixmap(QPixmap(u"resources/upnld.png"))
        self.upnld_label.setScaledContents(True)
        self.upnld_label.setAlignment(Qt.AlignCenter)
        self.su_label = QLabel(self.page_1)
        self.su_label.setObjectName(u"su_label")
        self.su_label.setGeometry(QRect(430, 500, 171, 41))
        self.su_label.setFont(font4)
        self.su_label.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
" background-color : transparent; \n"
"\n"
"	\n"
"	\n"
"	\n"
"	color: rgb(246, 146, 114);\n"
"	\n"
"	\n"
" };\n"
"")
        self.su_label.setAlignment(Qt.AlignCenter)
        self.C_label = QLabel(self.page_1)
        self.C_label.setObjectName(u"C_label")
        self.C_label.setGeometry(QRect(380, 110, 31, 31))
        self.C_label.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
" background-color : transparent; \n"
" };\n"
"")
        self.C_label.setPixmap(QPixmap(u"resources/stopwatch.png"))
        self.C_label.setScaledContents(True)
        self.pop_btn = QPushButton(self.page_1)
        self.pop_btn.setObjectName(u"pop_btn")
        self.pop_btn.setGeometry(QRect(330, 350, 41, 40))
        self.pop_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(169, 0, 51);\n"
"\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"	\n"
"	background-color: rgb(252, 66, 66);\n"
"\n"
"\n"
"}\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"resources/ad-blocker.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pop_btn.setIcon(icon6)
        self.pop_btn.setIconSize(QSize(35, 35))
        self.pop_label = QLabel(self.page_1)
        self.pop_label.setObjectName(u"pop_label")
        self.pop_label.setGeometry(QRect(380, 350, 101, 41))
        font5 = QFont()
        font5.setFamily(u"AvenirNext LT Pro Bold")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.pop_label.setFont(font5)
        self.pop_label.setStyleSheet(u"QLabel{\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.pop_label.setAlignment(Qt.AlignCenter)
        self.ext_btn = QLabel(self.page_1)
        self.ext_btn.setObjectName(u"ext_btn")
        self.ext_btn.setGeometry(QRect(130, 30, 141, 31))
        font6 = QFont()
        font6.setFamily(u"Avenir Next LT Pro")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.ext_btn.setFont(font6)
        self.ext_btn.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
" background-color : transparent; \n"
"	\n"
"	\n"
"	\n"
"	\n"
"	color: rgb(50, 215, 54);\n"
" };")
        self.ext_btn.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ext_btn.setWordWrap(False)
        self.ext_btn.setOpenExternalLinks(True)
        self.stackedWidget.addWidget(self.page_1)
        self.back_img_1.raise_()
        self.crnt_ip.raise_()
        self.tor_label.raise_()
        self.Tor_Btn.raise_()
        self.speed_label.raise_()
        self.speed_Test.raise_()
        self.off_btn.raise_()
        self.connect_Btn.raise_()
        self.sp_label.raise_()
        self.time_label.raise_()
        self.btn_about.raise_()
        self.label.raise_()
        self.except_lbl.raise_()
        self.dwnld_label.raise_()
        self.upnld_label.raise_()
        self.su_label.raise_()
        self.C_label.raise_()
        self.pop_btn.raise_()
        self.pop_label.raise_()
        self.ext_btn.raise_()
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.back_img_3 = QLabel(self.page_3)
        self.back_img_3.setObjectName(u"back_img_3")
        self.back_img_3.setGeometry(QRect(0, 0, 801, 561))
        self.back_img_3.setPixmap(QPixmap(u"resources/Aboutui1.png"))
        self.btn_home_2 = QPushButton(self.page_3)
        self.btn_home_2.setObjectName(u"btn_home_2")
        self.btn_home_2.setGeometry(QRect(20, 20, 40, 40))
        self.btn_home_2.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"resources/home_new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home_2.setIcon(icon7)
        self.btn_home_2.setIconSize(QSize(35, 35))
        self.textBrowser = QTextBrowser(self.page_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(50, 250, 711, 171))
        self.textBrowser.setFont(font3)
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
        self.fsf = QLabel(self.page_3)
        self.fsf.setObjectName(u"fsf")
        self.fsf.setGeometry(QRect(50, 430, 221, 51))
        self.fsf.setStyleSheet(u"QLabel{\n"
"background:transparent;\n"
"}")
        self.fsf.setPixmap(QPixmap(u"resources/fsf-free-software-foundation.png"))
        self.fsf.setScaledContents(True)
        self.lgpl_3 = QLabel(self.page_3)
        self.lgpl_3.setObjectName(u"lgpl_3")
        self.lgpl_3.setGeometry(QRect(320, 420, 161, 61))
        self.lgpl_3.setStyleSheet(u"QLabel{\n"
"\n"
"\n"
"background:transparent;\n"
"\n"
"\n"
"}")
        self.lgpl_3.setPixmap(QPixmap(u"resources/LGPLv3_Logo.png"))
        self.lgpl_3.setScaledContents(True)
        self.reddit_Btn = QPushButton(self.page_3)
        self.reddit_Btn.setObjectName(u"reddit_Btn")
        self.reddit_Btn.setGeometry(QRect(590, 510, 30, 30))
        self.reddit_Btn.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"background:transparent;\n"
"border-radius:15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(255, 69, 0);\n"
"\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 150, 112);\n"
"\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"resources/Reddit_Mark_OnWhite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reddit_Btn.setIcon(icon8)
        self.reddit_Btn.setIconSize(QSize(20, 20))
        self.tweet_Btn = QPushButton(self.page_3)
        self.tweet_Btn.setObjectName(u"tweet_Btn")
        self.tweet_Btn.setGeometry(QRect(640, 510, 30, 30))
        self.tweet_Btn.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"background:transparent;\n"
"border-radius:15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(28, 183, 235);\n"
"\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(215, 242, 251);\n"
"\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"resources/twitter_round.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tweet_Btn.setIcon(icon9)
        self.tweet_Btn.setIconSize(QSize(20, 20))
        self.insta_Btn = QPushButton(self.page_3)
        self.insta_Btn.setObjectName(u"insta_Btn")
        self.insta_Btn.setGeometry(QRect(740, 510, 30, 30))
        self.insta_Btn.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"background:transparent;\n"
"border-radius:15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(219, 125, 75);\n"
"\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(245, 168, 20);\n"
"\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"resources/insta_round.png", QSize(), QIcon.Normal, QIcon.Off)
        self.insta_Btn.setIcon(icon10)
        self.insta_Btn.setIconSize(QSize(20, 20))
        self.git_Btn = QPushButton(self.page_3)
        self.git_Btn.setObjectName(u"git_Btn")
        self.git_Btn.setGeometry(QRect(690, 510, 30, 30))
        self.git_Btn.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"background:transparent;\n"
"border-radius:15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(124, 149, 180);\n"
"\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"resources/GitHub-Mark-Light-64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.git_Btn.setIcon(icon11)
        self.git_Btn.setIconSize(QSize(20, 20))
        self.mail_Btn = QPushButton(self.page_3)
        self.mail_Btn.setObjectName(u"mail_Btn")
        self.mail_Btn.setGeometry(QRect(550, 460, 201, 23))
        font7 = QFont()
        font7.setFamily(u"AvenirNext LT Pro Regular")
        font7.setPointSize(11)
        self.mail_Btn.setFont(font7)
        self.mail_Btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background:transparent;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.site = QPushButton(self.page_3)
        self.site.setObjectName(u"site")
        self.site.setGeometry(QRect(540, 510, 30, 30))
        self.site.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"background:transparent;\n"
"border-radius:15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(255, 170, 32);\n"
"\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"resources/www.png", QSize(), QIcon.Normal, QIcon.Off)
        self.site.setIcon(icon12)
        self.site.setIconSize(QSize(25, 25))
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 100, 131, 31))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 150, 301, 31))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"QLabel{\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.mail_Btn_2 = QPushButton(self.page_3)
        self.mail_Btn_2.setObjectName(u"mail_Btn_2")
        self.mail_Btn_2.setGeometry(QRect(70, 510, 381, 23))
        self.mail_Btn_2.setFont(font7)
        self.mail_Btn_2.setStyleSheet(u"QPushButton{\n"
"\n"
"background:transparent;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 180, 351, 91))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"QLabel{\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
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
        self.ref.setText("")
        self.back_img_1.setText("")
#if QT_CONFIG(tooltip)
        self.connect_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"CONNECT", None))
#endif // QT_CONFIG(tooltip)
        self.connect_Btn.setText("")
        self.crnt_ip.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.tor_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">TOR</span></p></body></html>", None))
        self.Tor_Btn.setText("")
        self.speed_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">SPEED TEST</span></p></body></html>", None))
        self.speed_Test.setText("")
#if QT_CONFIG(tooltip)
        self.off_btn.setToolTip(QCoreApplication.translate("MainWindow", u"DISCONNECT", None))
#endif // QT_CONFIG(tooltip)
        self.off_btn.setText("")
        self.sp_label.setText("")
        self.time_label.setText("")
        self.btn_about.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">About</span></p></body></html>", None))
        self.except_lbl.setText("")
        self.dwnld_label.setText("")
        self.upnld_label.setText("")
        self.su_label.setText("")
        self.C_label.setText("")
        self.pop_btn.setText("")
        self.pop_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#cf0040;\">ACTIVATED</span></p></body></html>", None))
        self.ext_btn.setText("")
        self.back_img_3.setText("")
        self.btn_home_2.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'AvenirNext LT Pro Bold'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-weight:400;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-s"
                        "ize:12pt; font-weight:400; color:#ffffff;\">Q VPN is a vpn that uses WireGuard protocol. It is intended to generate user friendly VPN without interrupting your browsing with no compromise in the protection of your data and privacy.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; color:#ffffff;\">Developed using PySide2 and Python3.</span></p></body></html>", None))
        self.fsf.setText("")
        self.lgpl_3.setText("")
        self.reddit_Btn.setText("")
        self.tweet_Btn.setText("")
        self.insta_Btn.setText("")
        self.git_Btn.setText("")
        self.mail_Btn.setText(QCoreApplication.translate("MainWindow", u"incinfoquest@gmail.com", None))
        self.site.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Q VPN Project</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; color:#ffffff;\">A VPN that uses WireGuard protocol</span></p></body></html>", None))
        self.mail_Btn_2.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9 2021 incinfoquest - All Rights Reserved.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; color:#ffffff;\">Developed by:</span></p><p align=\"justify\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; color:#ffffff;\">Anandan S, Omar Fayadh D, Sreerag S.</span></p></body></html>", None))
    # retranslateUi
