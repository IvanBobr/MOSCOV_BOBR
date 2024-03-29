from random import choice
import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup
from PyQt5.QtWidgets import QLabel, QLineEdit, QLCDNumber, QCheckBox, QTextBrowser, QTextEdit
from PyQt5.Qt import QPainter, QPen, QColor
from PyQt5 import Qt, QtCore

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setGeometry(100, 100, 613, 613)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        s = choice(range(1, 600))
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(choice(range(1, 600)), choice(range(1, 600)), s, s)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
