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

ui,_ = loadUiType('WDSkin.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_Handler()
        self.ButtonHandler()

    def UI_Handler(self):
        self.mainTab.tabBar().setVisible(False)

    ### Button Handler ####
    def ButtonHandler(self):
        pass


    def showHome(self):
        self.mainTab.setCurrentIndex(0)

    def showScript(self):
        self.mainTab.setCurrentIndex(1)

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainApp()
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(win)
    mw.show()
    app.exec_()

