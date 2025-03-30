#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import os  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
import json  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import colorama  #Декоднул @allahdec.
from colorama import Fore  #Декоднул @allahdec.

os.system('cls' if os.name == 'nt' else 'clear')

banner = """
 ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓
▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒
▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░
▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░
▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░
░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ 
░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ 
░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  
       ░    ░ ░           ░              ░  ░   ░     ░ ░     
            ░ ░                                       ░ ░     
"""

print(colored(banner, 'magenta'))

main_menu = """ Поиск по нику
╔══════════════════════════════════╗
║[1] - Поиск                       ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""

print(colored(main_menu, 'magenta'))

links = {
    "Facebook": "https://facebook.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://instagram.com/{}",
}


def usernamm():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input("Введите команду: ")
        if command == "1":  #Декоднул @allahdec.
            eusername = input("Введите имя пользователя: ")
            print("Поиск данных...")
            if eusername == "":  #Декоднул @allahdec.
                print("Это не является никнеймом пользователя")
                continue  #Декоднул @allahdec.

            url = "https://leakcheck.net/api/public?key=49535f49545f5245414c4c595f4150495f4b4559&check=" + eusername
            response = requests.get(url)

            if response.status_code == 200:  #Декоднул @allahdec.
                data = json.loads(response.text)
                if data.get('success', False):  #Декоднул @allahdec.
                    print("Данные:")
                    sources = data.get('sources', [])
                    for source in sources:  #Декоднул @allahdec.
                        name = source.get('name')
                        if name:  #Декоднул @allahdec.
                            print(colored(f"Найденные утечки: {name}", 'magenta'))
                else:  #Декоднул @allahdec.
                    print("Данные в базах данных не найдены")
            else:  #Декоднул @allahdec.
                print(f"Код состояния ответа: {response.status_code}")

            print("Поиск социальных сетей...")
            results = {}
            for networks, url_template in links.items():  #Декоднул @allahdec.
                full_url = url_template.format(eusername)
                response = requests.get(full_url)

                if response.status_code == 200:  #Декоднул @allahdec.
                    time.sleep(0.1)
                    print(colored(f"{networks}: {full_url}", 'magenta'))
                    results[networks] = full_url

            if not results:  #Декоднул @allahdec.
                print(colored(f"Социальные сети с ником {eusername} не найдены", 'magenta'))

        elif command == "99":  #Декоднул @allahdec.
            print("Выход из программы...")
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print("Неверная команда! Пожалуйста, попробуйте снова.")


usernamm()
