import sys

from PyQt6 import uic
from random import randint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.create)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw()
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = randint(0, 250)
        qp.drawEllipse(randint(0, 378 - r), randint(0, 474 - r), r, r)
        self.do_paint = False

    def create(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec())
