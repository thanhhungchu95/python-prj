import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class ExampleCenter(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(300, 200)
        self.center()

        self.setWindowTitle('Center on Screen')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExampleCenter()
    sys.exit(app.exec_())
