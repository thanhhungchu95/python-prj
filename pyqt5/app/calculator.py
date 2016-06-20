import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt


class Calculator(QWidget):

    btnProcess = 0

    def __init__(self):
        super().__init__()

        self.createUI()

    def createUI(self):

        grid = QGridLayout()
        grid.setSpacing(1)

        result = QLineEdit('0.')
        result.setAlignment(Qt.AlignRight)
        result.setReadOnly(True)

        grid.addWidget(result, 0, 0, 1, 4)

        btnOne = QPushButton('1')
        grid.addWidget(btnOne, 3, 0)
        btnOne.clicked.connect(self.actionOne)

        btnTwo = QPushButton('2')
        grid.addWidget(btnTwo, 3, 1)
        btnTwo.clicked.connect(self.actionTwo)

        btnThree = QPushButton('3')
        grid.addWidget(btnThree, 3, 2)
        btnThree.clicked.connect(self.actionThree)

        btnFour = QPushButton('4')
        grid.addWidget(btnFour, 2, 0)
        btnFour.clicked.connect(self.actionFour)

        btnFive = QPushButton('5')
        grid.addWidget(btnFive, 2, 1)
        btnFive.clicked.connect(self.actionFive)

        btnSix = QPushButton('6')
        grid.addWidget(btnSix, 2, 2)
        btnSix.clicked.connect(self.actionSix)

        btnSeven = QPushButton('7')
        grid.addWidget(btnSeven, 1, 0)
        btnSeven.clicked.connect(self.actionSeven)

        btnEight = QPushButton('8')
        grid.addWidget(btnEight, 1, 1)
        btnEight.clicked.connect(self.actionEight)

        btnNine = QPushButton('9')
        grid.addWidget(btnNine, 1, 2)
        btnNine.clicked.connect(self.actionNine)

        btnZero = QPushButton('0')
        grid.addWidget(btnZero, 4, 0)
        btnZero.clicked.connect(self.actionZero)

        btnAdd = QPushButton('+')
        grid.addWidget(btnAdd, 4, 3)
        btnAdd.clicked.connect(self.actionAdd)

        btnSubtract = QPushButton('-')
        grid.addWidget(btnSubtract, 3, 3)
        btnSubtract.clicked.connect(self.actionSubtract)

        btnMultiple = QPushButton('*')
        grid.addWidget(btnMultiple, 2, 3)
        btnMultiple.clicked.connect(self.actionMultiple)

        btnDivide = QPushButton('/')
        grid.addWidget(btnDivide, 1, 3)
        btnDivide.clicked.connect(self.actionDivide)

        btnDot = QPushButton('.')
        grid.addWidget(btnDot, 4, 1)
        btnDot.clicked.connect(self.actionDot)

        btnEqual = QPushButton('=')
        grid.addWidget(btnEqual, 4, 2)
        btnEqual.clicked.connect(self.actionEqual)

        btnSign = QPushButton('+/-')
        grid.addWidget(btnSign, 1, 3)
        btnSign.clicked.connect(self.actionSign)

        btnAC = QPushButton('AC')
        grid.addWidget(btnAC, 1, 1)
        btnAC.clicked.connect(self.actionAC)

        btnDelete = QPushButton('DEL')
        grid.addWidget(btnDelete, 1, 2)
        btnDelete.clicked.connect(self.actionDelete)

        btnExit = QPushButton('EXIT')
        grid.addWidget(btnExit, 1, 0)
        btnExit.clicked.connect(self.actionExit)

        self.setLayout(grid)
        self.move(300, 300)
        self.setWindowTitle('Calculator')
        self.show()

    def actionOne(self):
        print('Button one clicked.')

    def actionTwo(self):
        print('Button two clicked.')

    def actionThree(self):
        print('Button three clicked.')

    def actionFour(self):
        print('Button four clicked.')

    def actionFive(self):
        print('Button five clicked.')

    def actionSix(self):
        print('Button six clicked.')

    def actionSeven(self):
        print('Button seven clicked.')

    def actionEight(self):
        print('Button eight clicked.')

    def actionNine(self):
        print('Button nine clicked.')

    def actionZero(self):
        print('Button zero clicked.')

    def actionAdd(self):
        print('Button add clicked.')

    def actionSubtract(self):
        print('Button subtract clicked.')

    def actionMultiple(self):
        print('Button multiple clicked.')

    def actionDivide(self):
        print('Button divide clicked.')

    def actionDot(self):
        print('Button dot clicked.')

    def actionEqual(self):
        print('Button equal clicked.')

    def actionSign(self):
        print('Button sign clicked.')

    def actionAC(self):
        print('Button AC clicked.')

    def actionDelete(self):
        print('Button delete clicked.')

    def actionExit(self):
        print('Button exit clicked.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cal = Calculator()
    sys.exit(app.exec_())
