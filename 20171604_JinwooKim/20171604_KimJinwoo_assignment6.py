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
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

        addButton = QPushButton("Add", self)
        addButton.clicked.connect(self.add)
        delButton = QPushButton("Del", self)
        delButton.clicked.connect(self.delet)
        findButton = QPushButton("Find", self)
        findButton.clicked.connect(self.find)
        incButton = QPushButton("Inc", self)
        incButton.clicked.connect(self.inc)
        showButton = QPushButton("Show", self)
        showButton.clicked.connect(self.show_score)

        #############################################################

        firstLine = QHBoxLayout()
        firstLine.addStretch(1)
        name = QLabel("Name :")
        self.nameEdit = QLineEdit(self)
        age = QLabel("Age :")
        self.ageEdit = QLineEdit(self)
        score = QLabel("Score :")
        self.scoreEdit = QLineEdit(self)
        firstLine.addWidget(name)
        firstLine.addWidget(self.nameEdit)
        firstLine.addWidget(age)
        firstLine.addWidget(self.ageEdit)
        firstLine.addWidget(score)
        firstLine.addWidget(self.scoreEdit)

        secondLine = QHBoxLayout()
        secondLine.addStretch(1)
        secondLine.addStretch(1)
        amount = QLabel("Amount :")
        self.amountEdit = QLineEdit(self)
        key = QLabel("Key :")
        self.keyCombobox = QComboBox(self)
        self.keyCombobox.addItem("Name")
        self.keyCombobox.addItem("Age")
        self.keyCombobox.addItem("Score")
        secondLine.addWidget(amount)
        secondLine.addWidget(self.amountEdit)
        secondLine.addWidget(key)
        secondLine.addWidget(self.keyCombobox)

        thirdLine = QHBoxLayout()
        thirdLine.addStretch(1)
        thirdLine.addWidget(addButton)
        thirdLine.addWidget(delButton)
        thirdLine.addWidget(findButton)
        thirdLine.addWidget(incButton)
        thirdLine.addWidget(showButton)

        result = QLabel("Result :")
        fourthLine = QHBoxLayout()
        fourthLine.addWidget(result)

        fiveLine = QHBoxLayout()
        self.resultEdit = QTextEdit()
        fiveLine.addWidget(self.resultEdit)

        ####################################################
        vbox = QVBoxLayout()
        vbox.addLayout(firstLine)
        vbox.addLayout(secondLine)
        vbox.addLayout(thirdLine)
        vbox.addLayout(fourthLine)
        vbox.addLayout(fiveLine)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Assignment')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):

        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            print("New DB: ", self.dbfilename)
            return []
        try:
            scdb = pickle.load(fH)
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        fH.close()
        self.scoredb = scdb

    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, keyname = "Name"):
        msg = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                msg += attr + "=" + str(p[attr]) +" "
            msg += "\n"
        self.resultEdit.setPlainText(msg)

    def add(self):
        self.addnametext = self.nameEdit.text()
        self.addscoretext = int (self.scoreEdit.text())
        self.addagetext = int (self.ageEdit.text())
        try:
            record = {'Name': self.addnametext, 'Age': self.addagetext, 'Score': self.addscoretext}
            if (type(self.addagetext) != 'int') or (type(self.addscoretext) != 'int'):
                print("Value Error")
            self.scoredb += [record]
        except:
            print("Invalid command Error")

    def delet(self):
        self.addnametext = self.nameEdit.text()
        self.Co_scdb = self.scoredb[:]
        for l in range(len(self.scoredb)):
            for p in self.scoredb:
                if p['Name'] == self.addnametext:
                    self.scoredb.remove(p)

    def inc(self):
        self.intnametext = self.nameEdit.text()
        self.intamounttext = (int) (self.amountEdit.text())
        for j in self.scoredb:
            if j['Name'] == self.intnametext:
                j['Score'] = str(int(j['Score']) + self.intamounttext)

    def find(self):
        self.intnametext = self.nameEdit.text()
        empty_list = []
        result_string = ""
        for i in self.scoredb:
            if i['Name'] == self.intnametext:
                empty_list.append(i)
                for attr in i:
                    result_string += attr + "=" + str(i[attr]) + " "
                result_string += "\n"
        if len(empty_list) == 0:
            print("Not Found")
        self.resultEdit.setPlainText(result_string)

    def show_score(self):
        self.current_str = self.keyCombobox.currentText()
        self.showScoreDB(self.current_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
