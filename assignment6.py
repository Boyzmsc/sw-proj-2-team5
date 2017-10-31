import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.dbfilename = 'assignment6.dat'
        self.scdb = []
        self.scdb = self.readScoreDB()
        self.initUI()

    def initUI(self):
        # 첫번째 열
        self.namelabel = QLabel("Name:")
        self.agelabel = QLabel("Age:")
        self.scorelabel = QLabel("Score:")
        self.namebox = QLineEdit(self)
        self.agebox = QLineEdit(self)
        self.scorebox = QLineEdit(self)
        self.h1layout = QHBoxLayout()
        self.h1layout.addWidget(self.namelabel)
        self.h1layout.addWidget(self.namebox)
        self.h1layout.addWidget(self.agelabel)
        self.h1layout.addWidget(self.agebox)
        self.h1layout.addWidget(self.scorelabel)
        self.h1layout.addWidget(self.scorebox)

        # 두번째 열
        self.amountlabel = QLabel("Amount:")
        self.amountbox = QLineEdit(self)
        self.keylabel = QLabel("Key:")
        self.keybox = QComboBox()
        self.keybox.addItem('Name')
        self.keybox.addItem('Age')
        self.keybox.addItem('Score')
        self.h2layout = QHBoxLayout()
        self.h2layout.addStretch(1)
        self.h2layout.addWidget(self.amountlabel)
        self.h2layout.addWidget(self.amountbox)
        self.h2layout.addWidget(self.keylabel)
        self.h2layout.addWidget(self.keybox)

        # 세번째 열
        self.addbutton = QPushButton("Add")
        self.delbutton = QPushButton("Del")
        self.findbutton = QPushButton("Find")
        self.incbutton = QPushButton("Inc")
        self.showbutton = QPushButton("Show")
        self.h3layout = QHBoxLayout()
        self.h3layout.addStretch(0.5)
        self.h3layout.addWidget(self.addbutton)
        self.h3layout.addWidget(self.delbutton)
        self.h3layout.addWidget(self.findbutton)
        self.h3layout.addWidget(self.incbutton)
        self.h3layout.addWidget(self.showbutton)
        self.showbutton.clicked.connect(self.showResult)
        self.addbutton.clicked.connect(self.addResult)
        self.delbutton.clicked.connect(self.delResult)
        self.findbutton.clicked.connect(self.findResult)
        self.incbutton.clicked.connect(self.incResult)

        # 네번째 열
        self.resultlabel = QLabel("Result:")
        self.h4layout = QHBoxLayout()
        self.h4layout.addWidget(self.resultlabel)

        # 다섯번째 열
        self.resultbox = QTextEdit()
        self.h5layout = QHBoxLayout()
        self.h5layout.addWidget(self.resultbox)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.h1layout)
        self.vbox.addLayout(self.h2layout)
        self.vbox.addLayout(self.h3layout)
        self.vbox.addLayout(self.h4layout)
        self.vbox.addLayout(self.h5layout)

        self.setLayout(self.vbox)

        self.setGeometry(400, 400, 600, 350)
        self.setWindowTitle('Assignment6')
        self.show()

    # result
    def showResult(self):

        keyname = self.keybox.currentText()
        self.showScoreDB(keyname)

    def addResult(self):

        self.addScoreDB()

    def delResult(self):

        self.delScoreDB()

    def findResult(self):

        self.findScoreDB()

    def incResult(self):

        self.incScoreDB()

    # ///
    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:

            self.scdb = []
            return
        self.scdb = []
        try:
            self.scdb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()
        return self.scdb

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scdb, fH)
        fH.close()


    # scoreDB
    def showScoreDB(self, keyname):
        result = ""
        for p in sorted(self.scdb, key = lambda person: person[keyname]):
            for attr in sorted(p):
                result += str(attr) + "=" + str(p[attr]) + "   "
            result += "\n"
        self.resultbox.setPlainText(result)

    def addScoreDB(self):
        try:
            intage = int(self.agebox.text())
            intscore = int(self.scorebox.text())
            record = {'Name': self.namebox.text(), 'Age': intage, 'Score': intscore}
            self.scdb += [record]
            self.showScoreDB("Name")
        except ValueError:
            self.resultbox.setPlainText("TypeError")

    def delScoreDB(self):
        self.check_scdb = self.scdb[:]
        for l in range(len(self.scdb)):
            k = self.scdb[len(self.scdb) - l - 1]
            if k['Name'] == self.namebox.text():
                self.scdb.remove(k)
        for j in range(len(self.scdb)):
            p = self.scdb[len(self.scdb) - j - 1]
            if p['Name'] == self.namebox.text():
                self.scdb.remove(p)
        self.showScoreDB("Name")
        if len(self.check_scdb) == len(self.scdb):
            self.resultbox.setPlainText("Not Found")

    def findScoreDB(self):
        temp=""
        rep = 0
        for k in self.scdb:
            if k['Name'] == self.namebox.text():
                rep += 1
                temp += "Age="+str(k['Age'])+"   "+"Name="+str(k['Name'])+"   "+"Score="+str(k['Score'])+"\n"
        self.resultbox.setPlainText(temp)
        if rep == 0:
            self.resultbox.setPlainText("Not Found")

    def incScoreDB(self):
        try:
            rep = 0
            intamount = int(self.amountbox.text())
            for j in self.scdb:
                if j['Name'] == self.namebox.text():
                    rep += 1
                    j['Score'] = int(j['Score']) + intamount
            self.showScoreDB("Name")
            if rep == 0:
                self.resultbox.setPlainText("Not Found")
        except ValueError:
            self.resultbox.setPlainText("TypeError")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())


