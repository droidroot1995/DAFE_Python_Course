import sys

from PyQt5.QtWidgets import *

def main():
    app = QApplication([])
    w = QWidget()
    w.setWindowTitle('Musketeers')

    btn1 = QPushButton('Athos')
    btn2 = QPushButton('Porthos')
    btn3 = QPushButton('Aramis')

    vbox = QVBoxLayout(w)

    vbox.addWidget(btn1)
    vbox.addWidget(btn2)
    vbox.addWidget(btn3)

    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()