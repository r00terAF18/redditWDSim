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
        sleep(0.04)
    sleep(0.09)


def writeC(word, color):
    if color == 'green':
        for i in range(len(word)):
            print(f'{bcolors.PASS}{word[i]}{bcolors.END}', sep='', end='', flush=True)
            sleep(0.05)
    elif color == 'red':
        for i in range(len(word)):
            print(f'{bcolors.FAIL}{word[i]}{bcolors.END}', sep='', end='', flush=True)
            sleep(0.05)
    elif color == 'blue':
        for i in range(len(word)):
            print(f'{bcolors.BLUE}{word[i]}{bcolors.END}', sep='', end='', flush=True)
            sleep(0.05)
    else:
        write(message)
    print()


def initSystem():
    write("Booting System...")
    writeC("OK", "green")
    write("Loading Modules...")
    writeC("OK", "green")
    write("Reading changes...")
    writeC("OK", "green")
    write("Applying updates...")
    writeC("OK", "green")
    write("Creating helper Threads...")
    writeC("OK", "green")
    write("Activating all Modules...")
    writeC("OK", "green")
    write("DONE")
    print()


def shutdownSys():
    write("Deactivating Modules...")
    writeC("Done", "red")
    write("Shuting down System...")
    writeC("Done", "red")
    cls()
    showLogo()


def showMenu():
    items = ['Scan', 'Hack Traffic Lights', 'Hack Car', 'Hack ATM', 'Hack Phone']
    i = 0
    for item in items:
        write(str(i) + "-" + item)
        i += 1
        print()

cls()
showLogo()

# initSystem()
# usrInput = input("Awaiting input...")
# cls()

showMenu()
