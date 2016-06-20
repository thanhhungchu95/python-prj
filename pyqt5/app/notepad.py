import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, qApp,
                             QTextEdit, QMessageBox)
from PyQt5.QtGui import QIcon


class Notepad(QMainWindow):

    textEdit = 0
    textEditType = 0

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()

        self.textEditType = str(type(self.textEdit))
        self.textEditType = self.textEditType[8:len(self.textEditType) - 2]
        self.setCentralWidget(self.textEdit)

        exitAction = QAction(QIcon('image/exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)

        newAction = QAction(QIcon('image/new.png'), '&New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Create New File')
        newAction.triggered.connect(self.newFile)

        openAction = QAction(QIcon('image/open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open An Exist File')
        openAction.triggered.connect(self.openFile)

        saveAction = QAction(QIcon('image/save.png'), '&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save File To Disk')
        saveAction.triggered.connect(self.saveFile)

        self.statusBar()

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Notepad')
        self.show()

    def newFile(self):
        if self.textEditType == 'PyQt5.QtWidgets.QTextEdit':
            print()
        else:
            QMessageBox.warning(self, 'Warning', 'Can\'t create new file.')

    def openFile(self):
        if self.textEditType == 'PyQt5.QtWidgets.QTextEdit':
            print()
        else:
            QMessageBox.warning(self, 'Warning', 'Can\'t open file.')

    def saveFile(self):
        if self.textEditType == 'PyQt5.QtWidgets.QTextEdit':
            print()
        else:
            QMessageBox.warning(self, 'Warning', 'Can\'t save file.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    n = Notepad()
    sys.exit(app.exec_())
