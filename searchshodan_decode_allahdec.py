#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import random  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
import urllib.parse  #Декоднул @allahdec.
from urllib.parse import quote_plus  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import colorama  #Декоднул @allahdec.
from colorama import Fore, Style  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.


os.system('cls' if os.name == 'nt' else 'clear')

banner = '\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n       ░    ░ ░           ░              ░  ░   ░     ░ ░     \n            ░ ░                                       ░ ░     \n'
print(colored(banner, 'magenta'))

SHODAN_API_KEYS = []
SHODAN_API_KEYS.extend(["Api", "Api", "Api", "Api"])


def search_shodan(query):  #Декоднул @allahdec.
    shodan_api_key = random.choice(SHODAN_API_KEYS)
    results = []
    try:  #Декоднул @allahdec.
        shodan_url = f'https://api.shodan.io/shodan/host/search?key={shodan_api_key}&query={quote_plus(query)}'
        response = requests.get(shodan_url)
        if response.status_code == 200:  #Декоднул @allahdec.
            data = response.json()
            if 'matches' in data:  #Декоднул @allahdec.
                for match in data['matches']:  #Декоднул @allahdec.
                    result = {
                        'IP': match['ip_str'],
                        'Port': match['port'],
                        'Data': match['data']
                    }
                    results.append(result)
                return results  #Декоднул @allahdec.
            else:  #Декоднул @allahdec.
                print('Результаты не найдены.')
                return results  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Не удалось получить данные.')
            return results  #Декоднул @allahdec.
    except requests.exceptions.RequestException as e:  #Декоднул @allahdec.
        print('Ошибка при выполнении поиска в SHODAN:')
        return results  #Декоднул @allahdec.


def format_results(results, duration):  #Декоднул @allahdec.
    output = f'Поиск завершен за {duration:.2f} секунд.\n\n'
    if not results:  #Декоднул @allahdec.
        output += 'Результаты не найдены.'
        return output  #Декоднул @allahdec.
    output += f'Найдено {len(results)} результатов:\n'
    for result in results:  #Декоднул @allahdec.
        output += f"IP: {result['IP']}, Port: {result['Port']}, Data: {result['Data']}\n"
    return output  #Декоднул @allahdec.


def startosint():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        print(colored(' Поиск по Shodan\n╔════════════════════════════════╗\n║[1] - Начать поиск              ║\n║[99] - Выход                    ║\n╚════════════════════════════════╝', 'magenta'))
        menu_choice = input('Введите команду: ').lower()

        if menu_choice == '99':  #Декоднул @allahdec.
            print('Заврешение программы')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        elif menu_choice == '1':  #Декоднул @allahdec.
            query = input('Введите запрос: ')
            if not query.strip():  #Декоднул @allahdec.
                print('Пожалуйста, введите допустимые данные.')
            else:  #Декоднул @allahdec.
                print('Поиск в SHODAN')
                start_time = time.time()
                results = search_shodan(query)
                duration = time.time() - start_time
                print(format_results(results, duration))
        else:  #Декоднул @allahdec.
            print('Недействительный выбор. Пожалуйста, выберите допустимый вариант.')


if __name__ == '__main__':  #Декоднул @allahdec.
    startosint()
