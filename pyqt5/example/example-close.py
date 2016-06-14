import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import QCoreApplication


class ExampleClose(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn = QPushButton('Button', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(80, 30)
        btn.move(110, 85)

        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    et = ExampleClose()
    sys.exit(app.exec_())
