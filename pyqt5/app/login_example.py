import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFormLayout,
                             QPushButton, QLineEdit, QLabel,
                             QDesktopWidget, QHBoxLayout)
from PyQt5.QtCore import Qt


class Login(QWidget):

    lblUser = 0
    lblPass = 0
    fldUser = 0
    fldPass = 0
    btnLogin = 0
    btnReset = 0
    username = 0
    password = 0

    def __init__(self):
        super().__init__()

        self.init()

    def init(self):

        form = QFormLayout()
        hbox = QHBoxLayout()

        self.lblUser = QLabel("Username")
        self.lblPass = QLabel("Password")
        self.fldUser = QLineEdit()
        self.fldPass = QLineEdit()
        self.btnLogin = QPushButton("Login")
        self.btnReset = QPushButton("Reset")

        form.setHorizontalSpacing(20)

        hbox.setSpacing(20)
        hbox.addStretch()
        hbox.addWidget(self.btnLogin)
        hbox.addWidget(self.btnReset)
        hbox.addStretch()

        self.fldUser.setMaxLength(25)
        self.fldUser.setAlignment(Qt.AlignCenter)
        self.fldPass.setMaxLength(20)
        self.fldPass.setAlignment(Qt.AlignCenter)
        self.fldPass.setEchoMode(QLineEdit.Password)

        self.fldUser.textChanged.connect(self.changeUsername)
        self.fldPass.textChanged.connect(self.changePassword)
        self.btnLogin.clicked.connect(self.loginAction)
        self.btnReset.clicked.connect(self.resetAction)

        self.setLayout(form)

        form.addRow(self.lblUser, self.fldUser)
        form.addRow(self.lblPass, self.fldPass)
        form.addRow(QLabel())
        form.addRow(hbox)

        self.setWindowTitle("Login Example")

        self.resize(250, 100)
        self.moveToCenter()

        self.show()

    def moveToCenter(self):
        frame = self.frameGeometry()
        pos = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(pos)
        self.move(frame.topLeft())

    def loginAction(self):
        print('Login information: ')
        print('Username: {}, Password: {}'.format(self.username,
                                                  self.password))

    def resetAction(self):
        print('Click reset button.')
        self.fldUser.clear()
        self.fldPass.clear()

    def changeUsername(self, text):
        self.username = text

    def changePassword(self, text):
        self.password = text


if __name__ == '__main__':
    app = QApplication(sys.argv)
    le = Login()
    sys.exit(app.exec_())
