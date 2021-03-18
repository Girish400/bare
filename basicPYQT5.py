
from os import system
system("python -m PyQt5.uic.pyuic -x tabtrading.ui -o Mainwindowtab.py")

from Mainwindowtab import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
import sys



class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


app = QApplication(sys.argv)
w = MainWindow()
app.exec_()
