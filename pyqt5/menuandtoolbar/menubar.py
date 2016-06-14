import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MenuBar(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('image/exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MenuBar()
    sys.exit(app.exec_())
