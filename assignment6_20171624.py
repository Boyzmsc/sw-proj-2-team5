import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QTextEdit, QLineEdit, QStatusBar, QMenuBar, QAction, qApp)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        namelable = QLabel("Name : ")
        self.nameedit = QLineEdit()
        agelable = QLabel("Age : ")
        self.ageedit = QLineEdit()
        scorelable = QLabel("Score : ")
        self.scoreedit = QLineEdit()
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        hbox6 = QHBoxLayout()
        hbox7 = QHBoxLayout()

        amountlable = QLabel("Amount : ")
        self.amountedit = QLineEdit()
        keylable = QLabel("Key : ")
        self.selectedkey = QLabel("Age")

        funtionlabel = QLabel("Functions : ")
        addbutton = QPushButton("Add")
        addbutton.clicked.connect(self.addScoreDB)
        delbutton = QPushButton("Del")
        delbutton.clicked.connect(self.delScoreDB)
        findbutton = QPushButton("Find")
        findbutton.clicked.connect(self.findScoreDB)
        incbutton = QPushButton("Inc")
        incbutton.clicked.connect(self.incScoreDB)
        showbutton = QPushButton("Show")
        showbutton.clicked.connect(self.showScoreDB)

        keybuttonlabel = QLabel("Keys : ")
        agebutton = QPushButton("Age")
        agebutton.clicked.connect(self.SetKeyAsAge)
        scorebutton = QPushButton("Score")
        scorebutton.clicked.connect(self.SetKeyAsScore)
        namebutton = QPushButton("Name")
        namebutton.clicked.connect(self.SetKeyAsName)

        resultlable = QLabel("Result:")

        self.resultbox = QTextEdit()

        self.bar = QStatusBar()

        hbox1.addWidget(namelable)
        hbox1.addWidget(self.nameedit)
        hbox1.addWidget(agelable)
        hbox1.addWidget(self.ageedit)
        hbox1.addWidget(scorelable)
        hbox1.addWidget(self.scoreedit)

        hbox2.addStretch(1)
        hbox2.addWidget(amountlable)
        hbox2.addWidget(self.amountedit)
        hbox2.addWidget(keylable)
        hbox2.addWidget(self.selectedkey)

        hbox3.addStretch(1)
        hbox3.addWidget(funtionlabel)
        hbox3.addWidget(addbutton)
        hbox3.addWidget(delbutton)
        hbox3.addWidget(findbutton)
        hbox3.addWidget(incbutton)
        hbox3.addWidget(showbutton)

        hbox4.addStretch(1)
        hbox4.addWidget(keybuttonlabel)
        hbox4.addWidget(agebutton)
        hbox4.addWidget(scorebutton)
        hbox4.addWidget(namebutton)

        hbox5.addWidget(resultlable)
        hbox5.addStretch(1)

        hbox6.addWidget(self.resultbox)

        hbox7.addWidget(self.bar)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addLayout(hbox7)
        self.setLayout(vbox)
        self.show()


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
        self.resultbox.setText("")
        for p in sorted(self.scoredb, key=lambda person: person[self.selectedkey.text()]):
            for attr in sorted(p):
                self.resultbox.insertPlainText(attr + "=" + str(p[attr]) + "\t")
            self.resultbox.append("")
        pass

    def addScoreDB(self):
        self.bar.showMessage('')
        try:
            record = {'Name': self.nameedit.text(), 'Age': int(self.ageedit.text()), 'Score': int(self.scoreedit.text())}
        except ValueError:
            self.bar.showMessage('Value Error')
        else:
            self.scoredb += [record]
            self.showScoreDB()

    def delScoreDB(self):
        try:
            co_scdb = self.scoredb[:]
            for l in range(len(self.scoredb)):
                for p in self.scoredb:
                    if p['Name'] == self.nameedit.text():
                        self.scoredb.remove(p)
            if len(co_scdb) == len(self.scoredb):
                self.bar.showMessage('Name not found')
        except ValueError:
            self.bar.showMessage('Value Error')
        self.showScoreDB()

    def findScoreDB(self):
        try:
            findedDB = []
            for i in self.scoredb:
                if i['Name'] == self.nameedit.text():
                    findedDB += [i]
            if len(findedDB) > 0:
                self.resultbox.setText("")
                for p in sorted(findedDB, key=lambda person: person[self.selectedkey.text()]):
                    for attr in sorted(p):
                        self.resultbox.insertPlainText(attr + "=" + str(p[attr] ) + "\t")
                    self.resultbox.append("")
            else:
                self.bar.showMessage('Name not found')
        except ValueError:
            self.bar.showMessage('Value Error')

    def incScoreDB(self):
        try:
            for i in self.scoredb:
                if i['Name'] == self.nameedit.text():
                    i['Score'] += int(self.amountedit.text())
            self.showScoreDB()
        except ValueError:
            self.bar.showMessage('Value Error')

    def SetKeyAsAge(self):
        self.selectedkey.setText("Age")
    def SetKeyAsName(self):
        self.selectedkey.setText("Name")
    def SetKeyAsScore(self):
        self.selectedkey.setText("Score")

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
