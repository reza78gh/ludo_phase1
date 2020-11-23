from PyQt5 import QtWidgets,QtGui
import gui ,add_player
from logic import Person, Base,Bead,set_player
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = gui.Ui_MainWindow()
ui.setupUi(MainWindow)
#=================add player============
MainWindow2 = QtWidgets.QMainWindow()
ui2 = add_player.Ui_MainWindow2()
ui2.setupUi(MainWindow2)
ui.actionAdd_Player.triggered.connect(lambda : MainWindow2.show())
ui2.pushButton.clicked.connect(lambda : add_user())
def add_user():
    user = ui2.lineEdit.text()
    password = ui2.lineEdit_2.text()
    color = ui2.comboBox.currentText()
    for player in Person.player_li:
        if player.name == user:
            ui2.statusbar.showMessage('user exist',3000)
            return -1
        if player.color == color:
            ui2.statusbar.showMessage('color exist',3000)
            return -1
    with open('login.txt','r') as f:
        for line in f:
            if line.split()[0] == user:
                if line.split()[1] == password:
                    i = len(Person.player_li)+1
                    lable_player = MainWindow.findChild(QtWidgets.QLabel, "player_"+str(i))
                    lable_player.setText(f"{user}")
                    lable_player.setStyleSheet(f'color:{color};')
                    set_player(user,color)
    ui2.lineEdit.clear()
    ui2.lineEdit_2.clear()
    MainWindow2.close()

#===================start and new game=================
ui.actionStart_Game.triggered.connect(lambda : start_game())
ui.actionNew_Game.triggered.connect(lambda : new_game())
    
def start_game():
    if len(Person.player_li) >= 2:
        ui.pushButton_33.setDisabled(False)

def new_game():
    Base.creat_base()
    for i in range(1,25):
        MainWindow.findChild(QtWidgets.QPushButton,"pushButton_"+str(i)).setIcon(QtGui.QIcon())
    for i in range(1,4):
        MainWindow.findChild(QtWidgets.QLabel,'label_'+str(i)).setText('4')
    Base.in_home_blue = []
    Base.in_home_red = []
    Base.in_home_green = []
    Base.in_home_yellow = []
    Base.out_blue = []
    Base.out_red = []
    Base.out_green = []
    Base.out_yellow = []
#===================exit=================
ui.actionExit.triggered.connect(lambda : exit_game())
def exit_game():
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    msgBox.setText(f"are you sure?\nthis game lost!")
    msgBox.setWindowTitle("exit")
    msgBox.setStandardButtons(QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
    if msgBox.exec_() == QtWidgets.QMessageBox.Yes:
        MainWindow.close()

#===================end=================
MainWindow.show()
sys.exit(app.exec_())



