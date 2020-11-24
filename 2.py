import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPolygon, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class Second(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('aaa.ui', self)
        self.setMouseTracking(True)
        self.coords = []
        self.qp = QPainter()
        self.flag = False
        self.pushButton.clicked.connect(self.run)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.setBrushColor()
            self.draw()
            self.qp.end()


    def run(self):
        self.coords = [random.randint(100, 500), random.randint(100, 500)]
        self.drawf()

    def mouseMoveEvent(self, event):
        self.coords = [event.x(), event.y()]


    def setBrushColor(self):
        self.qp.setBrush(QColor(255, 255, 0))

    def draw(self):
        self.size = random.randint(10, 100)
        self.qp.drawEllipse(*self.coords, self.size, self.size)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Second()
    ex.show()
    sys.exit(app.exec_())