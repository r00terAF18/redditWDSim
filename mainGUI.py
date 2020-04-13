import os
import sys


from PyQt5 import QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType


import qtmodern.styles
import qtmodern.windows

#import resources_rc.py

#ui,_ = loadUiType('Library System UI v4.ui')


class MainApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.setupUi(self)
        #self.UI_Handler()
        #self.ButtonHandler()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainApp()
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(win)
    mw.show()
    app.exec_()

