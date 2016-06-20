import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout,
                             QHBoxLayout, QVBoxLayout, QPushButton,
                             QLineEdit, QLabel)


class Login(QWidget):

    lblUser = 0
    lblPass = 0
    fldUser = 0
    fldPass = 0
    btnLogin = 0
    btnReset = 0

    def __init__(self):
        super().__init__()

        self.init()

    def init(self):

        grid = QGridLayout()
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        self.lblUser = QLabel("Username")
        self.lblPass = QLabel("Password")
        self.fldUser = QLineEdit()
        self.fldPass = QLineEdit()
        self.btnLogin = QPushButton("Login")
        self.btnReset = QPushButton("Reset")

        self.btnLogin.clicked.connect(self.loginAction)
        self.btnReset.clicked.connect(self.resetAction)

        self.setLayout(vbox)
        vbox.addLayout(grid)
        vbox.addLayout(hbox)

        grid.setSpacing(5)
        hbox.setSpacing(20)

        grid.addWidget(self.lblUser, 0, 0)
        grid.addWidget(self.fldUser, 0, 1)
        grid.addWidget(self.lblPass, 1, 0)
        grid.addWidget(self.fldPass, 1, 1)

        hbox.addStretch(1)
        hbox.addWidget(self.btnLogin)
        hbox.addWidget(self.btnReset)
        hbox.addStretch(1)

        self.setGeometry(300, 300, 320, 240)
        self.setWindowTitle("Login Example")
        self.show()

    def loginAction(self):
        print('Click login button.')
        print(self.fldUser.text)

    def resetAction(self):
        print('Click reset button.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    le = Login()
    sys.exit(app.exec_())
