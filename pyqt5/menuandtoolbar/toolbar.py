import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon


class ToolBar(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('image/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Hover exit button on toolbar')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tb = ToolBar()
    sys.exit(app.exec_())
