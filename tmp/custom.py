from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon
import sys


class Custom(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Hello World')
        self.setWindowIcon(QIcon('image/icon.png'))

    def showWnd(self):
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Custom()
    c.showWnd()
    sys.exit(app.exec_())
