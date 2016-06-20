import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout)


class BoxLayout(QWidget):

    def __init__(self):
        super().__init__()

        self.init()

    def init(self):

        btnOK = QPushButton('OK')
        btnCancel = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(5)
        hbox.addWidget(btnOK)
        hbox.addWidget(btnCancel)
        hbox.addStretch(5)

        vbox = QVBoxLayout()
        vbox.addStretch(5)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Box Layout')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    bl = BoxLayout()
    sys.exit(app.exec_())
