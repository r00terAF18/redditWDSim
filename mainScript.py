import bcolors
import os
from time import sleep
if os.name == 'nt':
    from colorama import init
    init()

TIME = 0.04
INAPP = True

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
    showLogo()

def write(word, time):
    for i in range(len(word)):
        print(word[i], sep='', end='', flush=True)
        sleep(time)
    sleep(time + 0.02)
    print()


def writeC(word, color, time):
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


def initSystem():
    write("Booting System...", TIME)
    writeC("OK", "green", TIME)
    write("Loading Modules...", TIME)
    writeC("OK", "green", TIME)
    write("Reading changes...", TIME)
    writeC("OK", "green", TIME)
    write("Applying updates...", TIME)
    writeC("OK", "green", TIME)
    write("Creating helper Threads...", TIME)
    writeC("OK", "green", TIME)
    write("Activating all Modules...", TIME)
    writeC("OK", "green", TIME)
    write("DONE", TIME)
    print()


def shutdownSys():
    write("Deactivating Modules...", TIME)
    writeC("Done", "red", TIME)
    write("Shuting down System...", TIME)
    writeC("Done", "red", TIME)
    


def showMenu():
    items = ['Scan', 'Hack Traffic Lights', 'Hack Car', 'Hack ATM', 'Hack Phone', "Exit"]
    i = 0
    for item in items:
        msg = bcolors.WARN + '[' + str(i) + ']' + bcolors.END
        print(msg, sep='', end='')
        write("-" + item, TIME)
        i += 1

def scanArea():
    writeC("[*] Starting Scan...", "green", TIME)
    write("####################################################################################################", TIME)
    writeC("DONE", "green", 0)
    print()
    input("Awaiting input...")
    print()

def hackTL():
    writeC("[*] Looking for nearest Traffic Light...", "green", 0.02)
    write("[*] Aquiring data...", TIME)
    write("[*] Infultraiting security...", TIME)
    write("[*] Running exploit....", TIME)
    writeC("[*] DONE", "green", TIME)
    print()
    input("Awaiting input...")
    print()


# initSystem()
# input("Awaiting input...")
cls()



while INAPP:
    showMenu()
    usrInput = input("Select Hack >>> ")
    cls()

    if usrInput == "0":
        cls()
        scanArea()
    elif usrInput == "1":
        cls()
        hackTL()
    
    elif usrInput == "5":
        cls()
        INAPP = False


shutdownSys()
input("Press any key to exit...")
cls()