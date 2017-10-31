import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.name=""
        self.age=""
        self.score=""
        self.amount=""
        self.tempkey='Name'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        Label1=QLabel("Name:")
        LineEdit1=QLineEdit("",self)
        Label2=QLabel("Age:")
        LineEdit2=QLineEdit("",self)
        Label3=QLabel("Score:")
        LineEdit3=QLineEdit("",self)
        LineEdit1.textChanged[str].connect(self.nameshift)
        LineEdit2.textChanged[str].connect(self.ageshift)
        LineEdit3.textChanged[str].connect(self.scoreshift)

        
        hbox = QHBoxLayout()        
        hbox.addWidget(Label1)
        hbox.addWidget(LineEdit1)
        hbox.addWidget(Label2)
        hbox.addWidget(LineEdit2)
        hbox.addWidget(Label3)
        hbox.addWidget(LineEdit3)

        Label4=QLabel("Amount:")
        LineEdit4=QLineEdit("",self)
        LineEdit4.textChanged[str].connect(self.amountshift)
        Label5=QLabel("Key:")
        combokey=QComboBox(self)
        combokey.addItem('Name')
        combokey.addItem('Age')
        combokey.addItem('Score')
        combokey.activated[str].connect(self.Clicked)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(Label4)
        hbox2.addWidget(LineEdit4)
        hbox2.addWidget(Label5)
        hbox2.addWidget(combokey)
        
        add = QPushButton("Add",self)
        show = QPushButton("Show",self)
        delete = QPushButton("Del",self)
        inc = QPushButton("Inc",self)
        find = QPushButton("Find",self)

        add.clicked.connect(self.addScoreDB)
        show.clicked.connect(self.showScoreDB)
        delete.clicked.connect(self.delScoreDB)
        inc.clicked.connect(self.incScoreDB)
        find.clicked.connect(self.findScoreDB)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(add)
        hbox3.addWidget(show)
        hbox3.addWidget(delete)
        hbox3.addWidget(inc)
        hbox3.addWidget(find)

        Label6 = QLabel("Result:")
        self.TextEdit = QTextEdit(self)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(Label6)
        hbox4.addWidget(self.TextEdit)
     

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)
        
                
        
        self.setGeometry(300, 300, 600, 340)
        self.setWindowTitle('Assignment6')    
        self.show()


    def Clicked(self , text):
        self.tempkey = text
    def nameshift(self,text):
        self.name = text
    def ageshift(self,text):
        self.age = text
    def scoreshift(self,text):
        self.score = text
    def amountshift(self,text):
        self.amount = text

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        string =''
        for p in sorted(self.scoredb, key = lambda person : person[self.tempkey]):
            for x in sorted(p):
                string += x+'='+str(p[x])+"     "
            string +='\n'
        self.TextEdit.setText(string)
    def addScoreDB(self):
        name = self.name
        score = self.score
        age = self.age

        record = {'Name' : name, 'Age' : int(age), 'Score' : int(score)}
        self.scoredb +=[record]
        self.showScoreDB()

    def findScoreDB(self):
        string=''
        name = self.name
        for k in self.scoredb:
            if k['Name'] == name:
                string += k['Name'] + 'Age:'+str(k['Age'])+'Score:'+str(k['Score']) + '\n'
        self.TextEdit.setText(string)

    def delScoreDB(self):
        d=0
        while d<len(self.scoredb):
            if self.scoredb[d]['Name'] == self.name:
                self.scoredb.remove(self.scoredb[d])
            else:
                d += 1
        self.showScoreDB()

    def incScoreDB(self):
        amount = self.amount
        a=0
        while a<len(self.scoredb):
            if self.scoredb[a]['Name'] == self.name:
                self.scoredb[a]['Score'] += int(amount)
                a += 1
            else:
                a += 1
        self.showScoreDB()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





