import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QVBoxLayout,
                             QLineEdit, QPushButton, QApplication)


class GridLayout(QWidget):

    def __init__(self):
        super().__init__()

        self.init()

    def init(self):

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        text = QLineEdit('0.')
        text.setReadOnly(True)
        vbox.addWidget(text)

        grid = QGridLayout()
        vbox.addLayout(grid)

        names = ['Exit', 'AC', 'DEL', '+/-',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            btn = QPushButton(name)
            grid.addWidget(btn, *position)

        self.move(300, 200)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gl = GridLayout()
    sys.exit(app.exec_())
