import bcolors
import os
from time import sleep
from termcolor import colored

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

def write(word, message, color='green'):
    for i in range(len(word)):
        print(word[i], sep='', end='', flush=True)
        sleep(0.05)
    
    if color == 'green':
        print(colored(message, color))
        print(f'{bcolors.OK}{message}{bcolors.END}', end='')
    elif color == 'warning':
        print(f'{bcolors.WARNING}{message}{bcolors.END}', end='')
    
def initSystem():
    write("Booting System...", "OK", "green")

cls()
showLogo()

initSystem()

