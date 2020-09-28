import random2
import sys
from PyQt5 import QtWidgets, QtTest, QtGui, QtCore as QC

fontTText = QtGui.QFont("Saira", 24)
fontLText = QtGui.QFont("Semi", 10)
fontBtn = QtGui.QFont("Kanit", 10)
fontQlabel = QtGui.QFont("Kanit", 10)
fontWait = QtGui.QFont("Kanit", 20)

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çekiliş V1.0")
        self.setWindowIcon(QtGui.QIcon("images/giveaway.png"))
        self.setGeometry(510, 100, 950, 850)

        self.setFixedSize(950, 850)

        self.titleImage = QtWidgets.QLabel()
        self.titleImage.setPixmap(QtGui.QPixmap("images/giveaway.png"))

        self.titleText = QtWidgets.QLabel("Çekiliş V1.0")
        self.titleText.setFont(fontTText)

        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setFont(fontLText)

        self.listTitle = QtWidgets.QLabel("Kişi Listesi")
        self.listTitle.setAlignment(QC.Qt.AlignCenter)
        self.listTitle.setFont(fontTText)

        self.textList = QtWidgets.QListWidget()
        self.textList.setFont(fontLText)

        self.textEditTitle = QtWidgets.QLabel("Kişi Giriş")
        self.textEditTitle.setFont(fontTText)
        self.textEditTitle.setAlignment(QC.Qt.AlignCenter)

        self.persono = QtWidgets.QSpinBox()
        self.persono.setValue(1)
        self.persono.valueChanged.connect(self.valueError)

        self.personumber = QtWidgets.QLabel("Kaç Kişi Çekilecek ?")
        self.personumber.setAlignment(QC.Qt.AlignCenter)
        self.personumber.setFont(fontQlabel)

        self.personTransferBtn = QtWidgets.QPushButton(
            QtGui.QIcon("images/user-add.svg"), "Kişi Ekle")
        self.personTransferBtn.clicked.connect(self.persontransfer)
        self.personTransferBtn.setFont(fontBtn)
        self.personAllClearBtn = QtWidgets.QPushButton(
            QtGui.QIcon("images/trash.svg"), "Tüm Kişileri Çıkar")
        self.personAllClearBtn.clicked.connect(self.personAllClear)
        self.personAllClearBtn.setFont(fontBtn)
        self.personRemoveBtn = QtWidgets.QPushButton(
            QtGui.QIcon("images/user-remove.svg"), "Kişi Çıkar")
        self.personRemoveBtn.clicked.connect(self.personremove)
        self.personRemoveBtn.setFont(fontBtn)
        self.start = QtWidgets.QPushButton(
            QtGui.QIcon("images/start.png"), "Başlat")
        self.start.clicked.connect(self.startGiveaway)
        self.start.setFont(fontBtn)
        self.wait = QtWidgets.QLabel("")
        self.wait.setFont(fontWait)
        self.wait.setAlignment(QC.Qt.AlignCenter)
        self.result = QtWidgets.QPushButton(
            QtGui.QIcon("images/giveaway.png"), "Sonuç")
        self.result.clicked.connect(self.openResult)
        self.result.setFont(fontBtn)
        self.result.setHidden(True)

        horizontal1 = QtWidgets.QHBoxLayout()
        vertical1 = QtWidgets.QVBoxLayout()

        horizontal2 = QtWidgets.QHBoxLayout()
        vertical2 = QtWidgets.QVBoxLayout()

        vertical3 = QtWidgets.QVBoxLayout()

        vertical1.addWidget(self.textEditTitle)
        vertical1.addWidget(self.textEdit)

        horizontal1.addLayout(vertical1)
        horizontal1.addStretch()
        horizontal1.addLayout(vertical3)
        horizontal1.addStretch()
        horizontal1.addLayout(horizontal2)

        vertical2.addWidget(self.listTitle)
        vertical2.addWidget(self.textList)

        horizontal2.addLayout(vertical2)

        vertical3.addStretch()
        vertical3.addWidget(self.personTransferBtn)
        vertical3.addWidget(self.personRemoveBtn)
        vertical3.addWidget(self.personAllClearBtn)
        vertical3.addStretch()
        vertical3.addWidget(self.personumber)
        vertical3.addWidget(self.persono)
        vertical3.addWidget(self.start)
        vertical3.addWidget(self.wait)
        vertical3.addWidget(self.result)
        vertical3.addStretch()

        window = QtWidgets.QWidget()
        window.setLayout(horizontal1)

        self.setCentralWidget(window)
        self.show()

    def valueError(self):
        if self.persono.value() <= 0:
            self.persono.setValue(1)
            QtWidgets.QMessageBox.critical(
                self, "Hata !", "Kişi sayısı 0 olamaz!", QtWidgets.QMessageBox.Ok)

    def persontransfer(self):
        persons = self.textEdit.toPlainText()
        personlist = persons.split()
        for person in personlist:
            self.textList.addItem(person)
        self.textEdit.clear()

    def personAllClear(self):
        self.textList.clear()

    def personremove(self):
        for item in self.textList.selectedItems():
            self.textList.takeItem(self.textList.row(item))

    def startGiveaway(self):
        try:
            persons = []
            for index in range(self.textList.count()):
                persons.append(self.textList.item(index).text())
            global winperson
            winperson = []
            while True:
                rndm = random2.choice(persons)
                winperson.append(rndm)
                if len(winperson) == int(self.persono.value()):
                    self.wait.setText("Kişi Çekiliyor...")
                    QtTest.QTest.qWait(4000)
                    self.wait.setText("Tebrikler! 🎊")
                    QtTest.QTest.qWait(2000)
                    self.wait.setHidden(True)
                    self.result.show()
                    break
                elif self.persono.value() == 0:
                    QtWidgets.QMessageBox.critical(
                        self, "Hata!", "Lütfen Bir Kişi Sayısı Belirtiniz!")
                    break
        except IndexError:
            QtWidgets.QMessageBox.critical(
                self, "Hata!", "Liste İçerisi Boş!\nLütfen liste içerisine kişi ekleyiniz!")

    def openResult(self):
        self.resultOpen = resulT()
        self.resultOpen.show()


class resulT(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kazananlar!")
        self.setGeometry(750, 150, 500, 500)
        self.setWindowIcon(QtGui.QIcon("images/giveaway.png"))

        fontTitle = QtGui.QFont("Aldrich", 28)
        fontText = QtGui.QFont("Cairo Semi-bold", 10)

        winlist = QtWidgets.QListWidget()
        winlist.setFont(fontText)
        winlist.setItemAlignment(QC.Qt.AlignCenter)

        for winper in winperson:
            winlist.addItem(winper)

        sonucTitle = QtWidgets.QLabel("🎉 Kazananlar 🎉")
        sonucTitle.setFont(fontTitle)
        sonucTitle.setAlignment(QC.Qt.AlignCenter)

        horizontal = QtWidgets.QHBoxLayout()
        vertical = QtWidgets.QVBoxLayout()

        horizontal.addStretch()
        horizontal.addWidget(winlist)
        horizontal.addStretch()

        vertical.addStretch()
        vertical.addWidget(sonucTitle)
        vertical.addStretch()
        vertical.addLayout(horizontal)
        vertical.addStretch()

        self.setLayout(vertical)
        self.show()


stylesheet = """
 QPushButton{
   border: 4px solid #E4E4E4;
   border-radius: 10px;
   width: 180px;
   height: 30px;
   color: #E4E4E4;
 }
 QPushButton:hover{
     color: black;
 }
 QTextEdit{
     color: white;
     font-size: 14px;
     border: 6px solid #E4E4E4;
     border-radius: 8px;
 }
 QListWidget{
     color: white;
     font-size: 14px;
     border: 6px solid #E4E4E4;
     border-radius: 8px;
 }
 QSpinBox{
     border: 4px solid #E4E4E4;
     border-radius: 6px;
     color: #E4E4E4;
 }
 QWidget{
     color: #E4E4E4;
     background-color: #7A7A7A;
 }
"""

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(stylesheet)
main = mainWindow()
sys.exit(app.exec_())
