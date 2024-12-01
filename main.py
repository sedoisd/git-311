import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.button_paint.clicked.connect(self.paint)

    def initUI(self):
        self.setFixedSize(900, 700)
        self.setWindowTitle('Sh')
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('Yellow'))
            x, y = randint(100, 700), randint(100, 700)
            r = randint(10, 300)
            qp.drawEllipse(x, y, r, r)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook  # Удалить при релизе
    ex = Example()
    ex.show()
    sys.exit(app.exec())
