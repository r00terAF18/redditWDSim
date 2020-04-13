import bcolors
import os
from time import sleep
if os.name == 'nt':
    from colorama import init
    init()


def showLogo():
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
    print(logo)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def write(word):
    for i in range(len(word)):
        print(word[i], sep='', end='', flush=True)
        sleep(0.05)
    sleep(0.09)

def writeC(word, color):
    if color == 'green':
        for i in range(len(word)):
            print(f'{bcolors.OK}{word[i]}{bcolors.END}', sep='', end='', flush=True)
            sleep(0.05)
    elif color == 'red':
        for i in range(len(word)):
            print(f'{bcolors.WARNING}{word[i]}{bcolors.END}', sep='', end='', flush=True)
            sleep(0.05)
    elif color == 'blue':
        for i in range(len(word)):
            print(f'{bcolors.BLUE}{word[i]}{bcolors.END}', sep='', end='', flush=True)
            sleep(0.05)
    else:
        write(message)


def initSystem():
    write("Booting System...")
    writeC("OK", "green")

cls()
showLogo()

initSystem()

