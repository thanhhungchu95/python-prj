import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class ExampleIcon(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Window with icon')
        self.setWindowIcon(QIcon('image/icon.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ei = ExampleIcon()
    sys.exit(app.exec_())
