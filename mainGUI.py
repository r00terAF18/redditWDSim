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

#import resources_rc.py

ui,_ = loadUiType('WDSkin.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_Handler()
        self.ButtonHandler()
        self.TIME = 0.035



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
        

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        showLogo()
    

    def UI_Handler(self):
        self.mainTab.tabBar().setVisible(False)

    ### Button Handler ####
    def ButtonHandler(self):
        self.btnCar.clicked.connect(self.hackCar)


    def showHome(self):
        self.mainTab.setCurrentIndex(0)

    def showScript(self):
        self.mainTab.setCurrentIndex(1)

    

    def write(self, word, time):
        for i in range(len(word)):
            print(word[i], sep='', end='', flush=True)
            sleep(time)
        sleep(time + 0.02)
        print()


    def writeC(self, word, color, time):
        if color == 'green':
            for i in range(len(word)):
                print(f'{bcolors.PASS}{word[i]}{bcolors.END}', sep='', end='', flush=True)
                sleep(time)
        elif color == 'red':
            for i in range(len(word)):
                print(f'{bcolors.FAIL}{word[i]}{bcolors.END}', sep='', end='', flush=True)
                sleep(time)
        elif color == 'blue':
            for i in range(len(word)):
                print(f'{bcolors.BLUE}{word[i]}{bcolors.END}', sep='', end='', flush=True)
                sleep(time)
        elif color == 'yellow':
            for i in range(len(word)):
                print(f'{bcolors.WARN}{word[i]}{bcolors.END}', sep='', end='', flush=True)
                sleep(time)
        else:
            write(message)
        print()


    def hackCar(self):
        self.showScript()
        writeC("[*] L00king for nearest C4R...", "green", 0.02)
        write("[*] Sending Start request...", TIME)
        write("[*] Aquiring response...", TIME)
        write("[*] Preparing exploit...", TIME)
        write("[*] Running exploit....", TIME)
        writeC("[*] DONE", "green", TIME)
        print()
        input("Awaiting input...")
        print()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainApp()
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(win)
    mw.show()
    app.exec_()

