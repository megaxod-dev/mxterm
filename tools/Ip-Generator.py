import os
import sys
import requests
import json
import random
import threading
import time
import subprocess
import concurrent.futures

# Variables de configuration
username_webhook = "IP Generator Bot"
avatar_webhook = "https://example.com/avatar.png"
color_webhook = 0x00FF00  # Couleur pour l'embed du webhook
max_ips = 100  # Limite de génération d'IP
generated_ips = 0
BEFORE = "["
AFTER = "]"
GEN_VALID = "[VALID]"
GEN_INVALID = "[INVALID]"
INPUT = ">"
reset = "\033[0m"
white = "\033[97m"
green = "\033[92m"
red = "\033[91m"
BEFORE_GREEN = "\033[92m"
BEFORE_RED = "\033[91m"
AFTER_GREEN = "\033[92m"  # Ajout de la couleur après l'élément vert
AFTER_RED = "\033[91m"  # Ajout de la couleur après l'élément rouge
BACKGROUND_RED = "\033[41m"  # Fond rouge

# Nettoyage de l'écran (fonctionne sous Linux/Mac)
def clear_screen():
    os.system('clear')

# Affichage de la bannière
def display_banner():
    print("""
      __  __                                _ 
     |  \/  | ___  __ _  __ ___  _____   __| |
     | |\/| |/ _ \/ _` |/ _` \ \/ / _ \ / _` |
     | |  | |  __/ (_| | (_| |>  < (_) | (_| |
     |_|  |_|\___|\__, |\__,_/_/\_\___/ \__,_|
                  |___/          IP Generator
    """)

clear_screen()
display_banner()

# Fonction pour afficher le titre du terminal
def Title(text):
    sys.stdout.write(f"\033]0;{text}\a")
    sys.stdout.flush()

# Fonction pour vérifier la validité du webhook
def CheckWebhook(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"{BEFORE + current_time_hour() + AFTER} Error: Webhook URL is not valid.")
            exit()
    except requests.RequestException as e:
        print(f"{BEFORE + current_time_hour() + AFTER} Error: Unable to reach Webhook URL: {e}")
        exit()

# Fonction pour obtenir l'heure actuelle (utile pour les logs)
def current_time_hour():
    return time.strftime("%H:%M:%S")

# Fonction pour envoyer un message au webhook
def SendWebhook(embed_content, webhook_url):
    payload = {
        'embeds': [embed_content],
        'username': username_webhook,
        'avatar_url': avatar_webhook
    }

    headers = {'Content-Type': 'application/json'}

    try:
        requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    except requests.RequestException as e:
        print(f"{BEFORE + current_time_hour() + AFTER} Error sending webhook: {e}{reset}")

# Fonction pour gérer l'envoi des IPs et leur vérification
def IpCheck(webhook_url):
    global number_valid, number_invalid, generated_ips
    ip = ".".join(str(random.randint(1, 255)) for _ in range(4))

    try:
        # Sur Termux, c'est Linux, donc on garde la commande ping adaptée
        result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=0.1)

        if result.returncode == 0:
            number_valid += 1
            if webhook_url:
                embed_content = {
                    'title': 'Ip Valid !',
                    'description': f"**Ip:**\n```{ip}```",
                    'color': color_webhook,
                    'footer': {
                        "text": username_webhook,
                        "icon_url": avatar_webhook,
                    }
                }
                SendWebhook(embed_content, webhook_url)
            print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{green} Status:  {white}Valid{green}  Ip: {white}{ip}{AFTER_GREEN}")
        else:
            number_invalid += 1
            print(f"{BACKGROUND_RED + BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{red} Status: {white}Invalid{red} Ip: {white}{ip}{AFTER_RED}")
    except Exception:
        number_invalid += 1
        print(f"{BACKGROUND_RED + BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{red} Status: {white}Invalid{red} Ip: {white}{ip}{AFTER_RED}")
    
    Title(f"Ip Generator - Invalid: {number_invalid} - Valid: {number_valid}")

    generated_ips += 1
    if generated_ips >= max_ips:
        print(f"\n{BEFORE + current_time_hour() + AFTER} {GEN_VALID} Generation complete. {generated_ips} IPs generated.")
        return False  # Arrêter le processus lorsque la limite est atteinte
    return True

# Fonction pour gérer la demande de génération d'IP avec multithreading
def Request(threads_number, webhook_url):
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads_number) as executor:
            results = executor.map(lambda _: IpCheck(webhook_url), range(threads_number))
            if not any(results):  # Si aucun résultat n'est vrai, arrêter la boucle
                return False
    except Exception as e:
        print(f"Error: {e}")

# Main
try:
    webhook = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook ? (y/n) -> {reset}")
    webhook_url = None
    if webhook.lower() in ['y', 'yes']:
        webhook_url = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook URL -> {reset}")
        CheckWebhook(webhook_url)

    try:
        threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {reset}"))
    except ValueError:
        print(f"Error: Invalid number.")
        exit()

    number_valid = 0
    number_invalid = 0

    while True:
        if not Request(threads_number, webhook_url):
            break  # Quitter la boucle si la limite d'IP est atteinte

    # Demander à l'utilisateur d'entrer "0" pour retourner au menu
    input("\nGeneration terminée. Entrez '0' pour retourner au menu -> ")

except Exception as e:
    print(f"Error: {e}")
