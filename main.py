import sys

from PyQt5.QtWidgets import QApplication

from gui import Gui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())