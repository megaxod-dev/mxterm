import os
import sys
from Config.Util import *
from Config.Config import *
try:
    import requests
    import json
    import random
    import threading
    import time
    import subprocess
    import concurrent.futures

except Exception as e:
    ErrorModule(e)

# Nettoyage de l'écran (fonctionne sous Linux/Mac, sous Windows on peut utiliser 'cls')
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

Title("Ip Generator")

max_ips = 100  # Limite de génération d'IP (par exemple, 100 IPs)
generated_ips = 0

try:
    webhook = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook ? (y/n) -> {reset}")
    if webhook.lower() in ['y', 'yes']:
        webhook_url = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook URL -> {reset}")
        CheckWebhook(webhook_url)

    try:
        threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {reset}"))
    except ValueError:
        ErrorNumber()

    def SendWebhook(embed_content):
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

    number_valid = 0
    number_invalid = 0

    def IpCheck():
        global number_valid, number_invalid, generated_ips
        ip = ".".join(str(random.randint(1, 255)) for _ in range(4))

        try:
            # Sur Termux, c'est Linux, donc on garde la commande ping adaptée
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=0.1)

            if result.returncode == 0:
                number_valid += 1
                if webhook.lower() == 'y':
                    embed_content = {
                        'title': 'Ip Valid !',
                        'description': f"**Ip:**\n```{ip}```",
                        'color': color_webhook,
                        'footer': {
                            "text": username_webhook,
                            "icon_url": avatar_webhook,
                        }
                    }
                    SendWebhook(embed_content)
                print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{green} Status:  {white}Valid{green}  Ip: {white}{ip}{green}")
            else:
                number_invalid += 1
                print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{red} Status: {white}Invalid{red} Ip: {white}{ip}{red}")
        except Exception:
            number_invalid += 1
            print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{red} Status: {white}Invalid{red} Ip: {white}{ip}{red}")
        Title(f"Ip Generator - Invalid: {number_invalid} - Valid: {number_valid}")

        generated_ips += 1
        if generated_ips >= max_ips:
            print(f"\n{BEFORE + current_time_hour() + AFTER} {GEN_VALID} Generation complete. {generated_ips} IPs generated.")
            return False  # Arrêter le processus lorsque la limite est atteinte
        return True

    def Request():
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=threads_number) as executor:
                results = executor.map(lambda _: IpCheck(), range(threads_number))
                if not any(results):  # Si aucun résultat n'est vrai, arrêter la boucle
                    return False
        except Exception as e:
            ErrorNumber()

    while True:
        if not Request():
            break  # Quitter la boucle si la limite d'IP est atteinte

    # Demander à l'utilisateur d'entrer "0" pour retourner au menu
    input("\nGeneration terminée. Entrez '0' pour retourner au menu -> ")

except Exception as e:
    Error(e)
