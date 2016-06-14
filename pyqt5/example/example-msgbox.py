import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox


class ExampleMessageBox(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Warning', 
                'Are you want to quit?', QMessageBox.Yes | 
                QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    et = ExampleMessageBox()
    sys.exit(app.exec_())
