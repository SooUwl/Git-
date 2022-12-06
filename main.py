import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.button.clicked.connect(self.paint)
        self.flag = False
        self.t = randint(60, 250)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush((QColor(randint(0, 255), randint(0, 255), randint(0, 255))))
        qp.drawEllipse(250, 250, self.t, self.t)

    def paint(self):
        self.t = randint(60, 250)
        self.flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
