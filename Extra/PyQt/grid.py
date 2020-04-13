import sys

from PyQt5.QtWidgets import *

def main():
    app = QApplication([])
    w = QWidget()
    w.setWindowTitle('Musketeers')

    grid = QGridLayout(w)

    for i in range(3):
        for j in range(3):
            grid.addWidget(QPushButton('Button'), i, j)

    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()