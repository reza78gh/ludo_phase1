from move import check_move
import dice

from PyQt5 import QtCore, QtGui, QtWidgets


roll = None
permis_roll = True
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1144, 671)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(710, 510, 60, 60))
        self.pushButton_1.setStyleSheet("background-color: rgba(0, 0, 255, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 440, 60, 60))
        self.pushButton_2.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 370, 60, 60))
        self.pushButton_3.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 370, 60, 60))
        self.pushButton_4.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 370, 60, 60))
        self.pushButton_5.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(570, 300, 60, 60))
        self.pushButton_6.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 230, 60, 60))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 0, 0,120);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(640, 230, 60, 60))
        self.pushButton_8.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(710, 230, 60, 60))
        self.pushButton_9.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(710, 160, 60, 60))
        self.pushButton_10.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(710, 90, 60, 60))
        self.pushButton_11.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(785, 90, 60, 60))
        self.pushButton_12.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(860, 90, 60, 60))
        self.pushButton_13.setStyleSheet("background-color: rgb(0, 255, 0,100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(860, 160, 60, 60))
        self.pushButton_14.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(860, 230, 60, 60))
        self.pushButton_15.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(930, 230, 60, 60))
        self.pushButton_16.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(1000, 230, 60, 60))
        self.pushButton_17.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(1000, 300, 60, 60))
        self.pushButton_18.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(1000, 370, 60, 60))
        self.pushButton_19.setStyleSheet("background-color: rgb(255, 255, 0, 170);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(930, 370, 60, 60))
        self.pushButton_20.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(860, 370, 60, 60))
        self.pushButton_21.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(860, 440, 60, 60))
        self.pushButton_22.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(860, 510, 60, 60))
        self.pushButton_23.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(785, 510, 60, 60))
        self.pushButton_24.setStyleSheet("background-color: rgb(200, 255, 180, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(620, 510, 60, 60))
        self.pushButton_25.setStyleSheet("background-color: rgba(0, 0, 255, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_25.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/bluePlayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_25.setIcon(icon)
        self.pushButton_25.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(580, 150, 60, 60))
        self.pushButton_26.setStyleSheet("background-color: rgb(255, 0, 0,120);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_26.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/redPlayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_26.setIcon(icon1)
        self.pushButton_26.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(950, 90, 60, 60))
        self.pushButton_27.setStyleSheet("background-color: rgb(0, 255, 0,100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_27.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/greenPlayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_27.setIcon(icon2)
        self.pushButton_27.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(1000, 450, 60, 60))
        self.pushButton_28.setStyleSheet("background-color: rgb(255, 255, 0, 170);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_28.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/yellowPlayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_28.setIcon(icon3)
        self.pushButton_28.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(785, 440, 60, 60))
        self.pushButton_29.setStyleSheet("background-color: rgba(0, 0, 255, 100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_29.setText("")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(640, 300, 60, 60))
        self.pushButton_30.setStyleSheet("background-color: rgb(255, 0, 0,120);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_30.setText("")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(785, 160, 60, 60))
        self.pushButton_31.setStyleSheet("background-color: rgb(0, 255, 0,100);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_31.setText("")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(930, 300, 60, 60))
        self.pushButton_32.setStyleSheet("background-color: rgb(255, 255, 0, 170);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30;\n"
"border-color: black;\n"
"")
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 500, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1040, 440, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(990, 80, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 140, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(250, 0, 20, 621))
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 300, 251, 281))
        self.widget.setObjectName("widget")
        self.turn = QtWidgets.QLabel(self.widget)
        self.turn.setGeometry(QtCore.QRect(110, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.turn.setFont(font)
        self.turn.setObjectName("turn")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 35, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_33 = QtWidgets.QPushButton(self.widget)
        self.pushButton_33.setGeometry(QtCore.QRect(70, 90, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_33.setIcon(icon4)
        self.pushButton_33.setIconSize(QtCore.QSize(300, 30))
        self.pushButton_33.setObjectName("pushButton_33")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(10, 160, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 251, 271))
        self.widget_2.setObjectName("widget_2")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 231, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.player_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.player_1.setFont(font)
        self.player_1.setObjectName("player_1")
        self.verticalLayout.addWidget(self.player_1)
        self.player_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.player_2.setFont(font)
        self.player_2.setObjectName("player_2")
        self.verticalLayout.addWidget(self.player_2)
        self.player_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.player_3.setFont(font)
        self.player_3.setObjectName("player_3")
        self.verticalLayout.addWidget(self.player_3)
        self.player_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.player_4.setFont(font)
        self.player_4.setObjectName("player_4")
        self.verticalLayout.addWidget(self.player_4)
        self.back_grand = QtWidgets.QLabel(self.centralwidget)
        self.back_grand.setGeometry(QtCore.QRect(-130, 0, 1281, 621))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.back_grand.setFont(font)
        self.back_grand.setText("")
        self.back_grand.setPixmap(QtGui.QPixmap("./icon/bg.jpg"))
        self.back_grand.setObjectName("back_grand")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 280, 261, 16))
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.back_grand.raise_()
        self.pushButton_1.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.pushButton_16.raise_()
        self.pushButton_17.raise_()
        self.pushButton_18.raise_()
        self.pushButton_19.raise_()
        self.pushButton_20.raise_()
        self.pushButton_21.raise_()
        self.pushButton_22.raise_()
        self.pushButton_23.raise_()
        self.pushButton_24.raise_()
        self.pushButton_25.raise_()
        self.pushButton_26.raise_()
        self.pushButton_27.raise_()
        self.pushButton_28.raise_()
        self.pushButton_29.raise_()
        self.pushButton_30.raise_()
        self.pushButton_31.raise_()
        self.pushButton_32.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.line.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.line_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1144, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setFont(QtGui.QFont('Times', 15))
        self.statusbar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_1.clicked.connect(self.move)
        self.pushButton_2.clicked.connect(self.move)
        self.pushButton_3.clicked.connect(self.move)
        self.pushButton_4.clicked.connect(self.move)
        self.pushButton_5.clicked.connect(self.move)
        self.pushButton_6.clicked.connect(self.move)
        self.pushButton_7.clicked.connect(self.move)
        self.pushButton_8.clicked.connect(self.move)
        self.pushButton_9.clicked.connect(self.move)
        self.pushButton_10.clicked.connect(self.move)
        self.pushButton_11.clicked.connect(self.move)
        self.pushButton_12.clicked.connect(self.move)
        self.pushButton_13.clicked.connect(self.move)
        self.pushButton_14.clicked.connect(self.move)
        self.pushButton_15.clicked.connect(self.move)
        self.pushButton_16.clicked.connect(self.move)
        self.pushButton_17.clicked.connect(self.move)
        self.pushButton_18.clicked.connect(self.move)
        self.pushButton_19.clicked.connect(self.move)
        self.pushButton_20.clicked.connect(self.move)
        self.pushButton_21.clicked.connect(self.move)
        self.pushButton_22.clicked.connect(self.move)
        self.pushButton_23.clicked.connect(self.move)
        self.pushButton_24.clicked.connect(self.move)
        self.pushButton_25.clicked.connect(self.move)
        self.pushButton_33.clicked.connect(self.roll_dice)


    def move(self):
            global roll
            global permis_roll
            clicked_btn = MainWindow.sender()
            print(clicked_btn.objectName())
            print(roll)
            if roll:
                a = check_move(int(clicked_btn.objectName().split('_')[1]),roll).split()
                if a[0] == 'move':
                        print(roll,a)
                        roll = None
                        permis_roll = True
                        btn=MainWindow.findChild(QtWidgets.QPushButton,"pushButton_"+a[2])
                        btn.setIcon(QtGui.QIcon("icon/bluePlayer.png"))
                        clicked_btn.setIcon(QtGui.QIcon(""))
                        self.label_7.setText('done')
                        # QtCore.QTimer.singleShot(4500,self.clear)
                        if a[3]=='l':
                                self.label.setText(str(int(self.label.text())-1))
                if a[0]=='stop':
                        roll = None
                        permis_roll = True
                if a[0]=='move_win':
                        self.pushButton_29.setIcon(QtGui.QIcon("icon/bluePlayer.png"))
                        clicked_btn.setIcon(QtGui.QIcon(""))

            else:
                self.statusbar.showMessage('roll dick',3000)
                
    def roll_dice(self):
            global roll
            global permis_roll
            if permis_roll:
                roll = dice.roll_the_dice()
                self.label_8.setText(str(roll))
                permis_roll = False

    def clear(self):
            self.label_7.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "4"))
        self.label_2.setText(_translate("MainWindow", "4"))
        self.label_3.setText(_translate("MainWindow", "4"))
        self.label_4.setText(_translate("MainWindow", "4"))
        self.turn.setText(_translate("MainWindow", "Player1"))
        self.label_7.setText(_translate("MainWindow", "TURN:"))
        self.pushButton_33.setText(_translate("MainWindow", "Roll"))
        self.label_8.setText(_translate("MainWindow", "3"))
        self.label_6.setText(_translate("MainWindow", "Player"))
        self.player_1.setText(_translate("MainWindow", "Player"))
        self.player_2.setText(_translate("MainWindow", "Player"))
        self.player_3.setText(_translate("MainWindow", "Player"))
        self.player_4.setText(_translate("MainWindow", "Player"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

