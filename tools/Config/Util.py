from .Config import *
try:
    import colorama
    import ctypes
    import subprocess
    import os
    import time
    import sys
    import datetime
    import requests
except Exception as e:
    print(f'Modules of the python library required are not installed. Make sure you have correctly installed python and have launched the "Setup.py" file to install necessary modules.')
    input(f'Error: {e}')

color_webhook = 0xa80505
username_webhook = name_tool
avatar_webhook = 'https://cdn.discordapp.com/attachments/1268900329605300234/1276010081665683497/RedTiger-Logo.png?ex=66cf38be&is=66cde73e&hm=696c53b4791044ca0495d87f92e6d603e8383315d2ebdd385aaccfc6dbf6aa77&'

color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
blue = color.BLUE
yellow = color.YELLOW

try: username_pc = os.getlogin()
except: username_pc = "username"

try:
    if sys.platform.startswith("win"):
        os_name = "Windows"
    elif 'termux' in sys.platform.lower():
        os_name = "Termux"
    elif sys.platform.startswith("linux"):
        os_name = "Linux"
    else:
        os_name = "Unknown"
except:
    os_name = "None"

tool_path = os.path.dirname(os.path.abspath(__file__)).split("Program\\")[0].strip()

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

BEFORE = f'{red}[{white}'
AFTER = f'{red}]'

BEFORE_GREEN = f'{green}[{white}'
AFTER_GREEN = f'{green}]'

INPUT = f'{BEFORE}>{AFTER} |'
INFO = f'{BEFORE}!{AFTER} |'
ERROR = f'{BEFORE}x{AFTER} |'
ADD = f'{BEFORE}+{AFTER} |'
WAIT = f'{BEFORE}~{AFTER} |'
NOTE = f'{BEFORE}NOTE{AFTER} |'

GEN_VALID = f'{BEFORE_GREEN}+{AFTER_GREEN} |'
GEN_INVALID = f'{BEFORE}x{AFTER} |'

INFO_ADD = f'{white}[{red}+{white}]{red}'

def Censored(text):
    censored = ["Matami", creator]
    for censored_text in censored:
        if text in censored:
            print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Unable to find "{white}{text}{red}".')
            Continue()
            Reset()
        elif censored_text in text:
            print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Unable to find "{white}{text}{red}".')
            Continue()
            Reset()
        else:
            pass

def Title(title):
    if os_name == "Windows":
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool} - {title}")
    elif os_name == "Linux" or os_name == "Termux":
        sys.stdout.write(f"\x1b]2;{name_tool} {version_tool} - {title}\x07")
        
def Clear():
    if os_name == "Windows":
        os.system("cls")
    elif os_name == "Linux" or os_name == "Termux":
        os.system("clear")

def Reset():
    if os_name == "Windows":
        file = ['python', os.path.join(tool_path, "RedTiger.py")]
        subprocess.run(file)
    elif os_name == "Linux" or os_name == "Termux":
        file = ['python3', os.path.join(tool_path, "RedTiger.py")]
        subprocess.run(file)

def StartProgram(program):
    if os_name == "Windows":
        file = ['python', os.path.join(tool_path, "Program", program)]
        subprocess.run(file)
    elif os_name == "Linux" or os_name == "Termux":
        file = ['python3', os.path.join(tool_path, "Program", program)]
        subprocess.run(file)

def Slow(text):
    delai = 0.03
    lignes = text.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)

def Continue():
    input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Press to continue -> " + reset)

def Error(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white}{e}", reset)
    Continue()
    Reset()

def ErrorChoiceStart():
    print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(1)

def ErrorChoice():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(3)
    Reset()

def ErrorId():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid ID !", reset)
    time.sleep(3)
    Reset()

def ErrorUrl():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid URL !", reset)
    time.sleep(3)
    Reset()

def ErrorResponse():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Response !", reset)
    time.sleep(3)
    Reset()

def ErrorEdge():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Edge not installed or driver not up to date !", reset)
    time.sleep(3)
    Reset()

def ErrorToken():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Token !", reset)
    time.sleep(3)
    Reset()
    
def ErrorNumber():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Number !", reset)
    time.sleep(3)
    Reset()

def ErrorWebhook():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Webhook !", reset)
    time.sleep(3)
    Reset()

def ErrorCookie():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Cookie !", reset)
    time.sleep(3)
    Reset()

def ErrorUsername():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Username !", reset)
    time.sleep(3)
    Reset()

def ErrorPlateform():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Unsupported Platform !", reset)
    time.sleep(3)
    Reset()

def ErrorModule(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error Module: {white}{e}", reset)
    Continue()
    Reset()

def OnlyWindows():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} This function is only available on Windows 10/11 !", reset)
    Continue()
    Reset()

def OnlyLinux():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} This function is only available on Linux !", reset)
    Continue()
    Reset()

# Ajout de la vérification et adaptation pour Termux
def InstallDependencies():
    if os_name == "Termux":
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Installing dependencies for Termux...")
        subprocess.run(['pkg', 'install', 'python', 'python-pip', '-y'])
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    elif os_name == "Windows":
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Installing dependencies for Windows...")
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

# Utilisation de la fonction InstallDependencies pour installer les dépendances
InstallDependencies()
