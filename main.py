import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from random import randint
from ui_class import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            r, g, b = [randint(0, 255) for _ in range(3)]
            qp.setBrush(QColor(r, g, b))
            x, y = randint(50, 700), randint(100, 700)
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
