from PyQt5 import QtWidgets
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

#===================end=================
MainWindow.show()
sys.exit(app.exec_())


# def set_player(name,color):
#     print('ok')
#     Person.player_li.append(Person(name,color))
#     list_beads = Base.get_list(color,'out') 
#     list_beads = Bead.creat_beads(color)
#     print(Base.out_red)


