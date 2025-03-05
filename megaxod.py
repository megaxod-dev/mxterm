import os
import subprocess
from rich.console import Console
from rich.align import Align

# Configuration
TOOLS_DIR = "tools"  # Dossier contenant les scripts Python
console = Console()

tools_mapping = {
    1: "ip-generator.py",
    2: "ip-lookup.py",
    3: "ip-pinger.py",
    4: "ip-port-scanner.py",
    5: "ip-scanner.py",
    6: "email-lookup.py",
    7: "email-tracker.py",
    8: "password-decrypted-attack.py",
    9: "password-encrypted.py",
    10: "phishing-attack.py",
    11: "phone-number-lookup.py",
    12: "username-tracker.py",
    13: "website-info-scanner.py",
    14: "website-url-scanner.py",
    15: "website-vulnerability-scanner.py"
}

def clear_screen():
    """Efface l'écran du terminal."""
    os.system("clear" if os.name == "posix" else "cls")

def display_banner():
    """Affiche une bannière stylée avec la liste des outils basée sur tools_mapping."""
    ascii_art = """
     [red] __  __                                _ 
     |  \/  | ___  __ _  __ ___  _____   __| |
     | |\/| |/ _ \/ _` |/ _` \ \/ / _ \ / _` |
     | |  | |  __/ (_| | (_| |>  < (_) | (_| |
     |_|  |_|\___|\__, |\__,_/_/\_\___/ \__,_|
                  |___/     Termux (Beta)    [/red]


╔═══════════════════════════════════════════════════╗
║                   MEGAXOD TOOLS                   ║
╠═══════════════════════════════════════════════════╣
╠ 01 : IP Generator                                 ║         
╠ 02 : IP Lookup                                    ║     
╠ 03 : IP Pinger                                    ║     
╠ 04 : IP Port Scanner                              ║           
╠ 05 : IP Scanner                                   ║                                                
╠ 06 : Email Lookup                                 ║                                                  
╠ 07 : Email Tracker                                ║                                                   
╠ 08 : Password Decrypted Attaque                   ║                                                                 
╠ 09 : Password Encrypted                           ║                                                        
╠ 10 : Phishing Attack                              ║                                                     
╠ 11 : Phone Number Lookup                          ║  
╠ 12 : Username Tracker                             ║
╠ 13 : Website Info Scanner                         ║
╠ 14 : Website URL Scanner                          ║
╠ 15 : Website Vulnerability Scanner                ║
╠ 00 : Quitter                                      ║
╚═══════════════════════════════════════════════════╝
"""  
    console.print(Align.center(ascii_art))

def run_tool(choice):
    """Exécute le script choisi basé sur le mapping des outils."""
    try:
        choice = int(choice)
        if 1 <= choice <= len(tools_mapping):
            script_path = os.path.join(TOOLS_DIR, tools_mapping[choice])
            console.print(f"[red]Exécution de {tools_mapping[choice]}...[/red]")
            subprocess.run(["python", script_path])
        else:
            console.print("[red]Choix invalide ![/red]")
    except ValueError:
        console.print("[red]Entrée invalide ! Veuillez entrer un numéro.[/red]")

if __name__ == "__main__":
    while True:
        clear_screen()
        display_banner()  # Affiche la bannière avec tools_mapping
        choice = input("\nFait ton choix: ")
        
        if choice.lower() == '0' or choice.lower() == '00':
            console.print("[red]Au revoir ![/red]")
            break
        
        run_tool(choice)
