import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

def dialog():
    mbox = QMessageBox()

    mbox.setText('You allegiance has been noted')
    mbox.setDetailedText('You are now a disciple and subject of the all-knowing Guru')
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    mbox.exec_()

def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300, 300)
    w.setWindowTitle('DAFE')

    label = QLabel(w)
    label.setText('Behold the Guru, DAFE')
    label.move(100, 130)
    label.show()

    btn = QPushButton(w)
    btn.setText('Beheld')
    btn.move(110, 150)
    btn.show()

    btn.clicked.connect(dialog) # widget.signal.connect(slot)

    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()