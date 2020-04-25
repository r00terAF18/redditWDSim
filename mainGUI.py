import os
import sys

from PyQt5 import QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import qtmodern.styles
import qtmodern.windows

import bcolors
from time import sleep
if os.name == 'nt':
    from colorama import init
    init()


ui,_ = loadUiType('WDSkin.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_Handler()
        self.ButtonHandler()
        self.TIME = 0.035
        self.showLogo()



    def showLogo(self):
        logo = '''                                                                
    ,-.----.                                                        
    \    /  \                ___                   ___              
    |   :    \             ,--.'|_               ,--.'|_            
    |   |  .\ :   ,---.    |  | :,'              |  | :,'   ,---.   
    .   :  |: |  '   ,'\   :  : ' :              :  : ' :  '   ,'\  
    |   |   \ : /   /   |.;__,'  /    ,--.--.  .;__,'  /  /   /   | 
    |   : .   /.   ; ,. :|  |   |    /       \ |  |   |  .   ; ,. : 
    ;   | |`-' '   | |: ::__,'| :   .--.  .-. |:__,'| :  '   | |: : 
    |   | ;    '   | .; :  '  : |__  \__\/: . .  '  : |__'   | .; : 
    :   ' |    |   :    |  |  | '.'| ," .--.; |  |  | '.'|   :    | 
    :   : :     \   \  /   ;  :    ;/  /  ,.  |  ;  :    ;\   \  /  
    |   | :      `----'    |  ,   /;  :   .'   \ |  ,   /  `----'   
    `---'.|                 ---`-' |  ,     .-./  ---`-'            
    `---`                         `--`---'                        
                                                                    '''
        self.logoarea.setText(logo)

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        showLogo()
    

    def UI_Handler(self):
        self.mainTab.tabBar().setVisible(False)


    def ButtonHandler(self):
        self.btnCar.clicked.connect(self.hackCar)
        self.btnBack.clicked.connect(self.showHome)


    def showHome(self):
        self.mainTab.setCurrentIndex(0)

    def showScript(self):
        self.mainTab.setCurrentIndex(1)
    

    def write(self, word, time):
        for i in range(len(word)):
            self.mainText.append(word[i])
            sleep(time)
        sleep(time + 0.02)


    def writeC(self, word, color, time):
        if color == 'green':  # #00FF00
            text = "<span style=\" font-size:8pt; font-weight:600; color:#00FF00;\" >"
            text += word
            text += "</span>"
            self.mainText.append(text)
            sleep(time)
        elif color == 'red':  # #FF3333
            text = "<span style=\" font-size:8pt; font-weight:600; color:#FF3333;\" >"
            text += word
            text += "</span>"
            self.mainText.append(text)
            sleep(time)
        elif color == 'blue':  # #10B1FE
            text = "<span style=\" font-size:8pt; font-weight:600; color:#10B1FE;\" >"
            text += word
            text += "</span>"
            self.mainText.append(text)
            sleep(time)
        elif color == 'yellow':  # #F9C859
            text = "<span style=\" font-size:8pt; font-weight:600; color:#F9C859;\" >"
            text += word
            text += "</span>"
            self.mainText.append(text)
            sleep(time)
        else:
            write(message)
        print()


    def hackCar(self):
        self.showScript()
        self.writeC("[*] L00king for nearest C4R...", "red", 0.02)
        self.write("[*] Sending Start request...", self.TIME)
        self.write("[*] Aquiring response...", self.TIME)
        self.write("[*] Preparing exploit...", self.TIME)
        self.write("[*] Running exploit....", self.TIME)
        #self.writeC("[*] DONE", "green", self.TIME)
        #self.mainText.setText("\n")
        #input("Awaiting input...")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainApp()
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(win)
    mw.show()
    app.exec_()

