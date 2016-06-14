import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class StatusBar(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('The first status.')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = StatusBar()
    sys.exit(app.exec_())
