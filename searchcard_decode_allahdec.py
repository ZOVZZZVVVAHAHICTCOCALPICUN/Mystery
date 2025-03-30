#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

os.system('cls' if os.name == 'nt' else 'clear')

banner = """
 ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓
▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒
▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░
▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░
▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░
░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ 
░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░         ░     ░░   ░ ▒ ▒ ░░  
       ░    ░ ░           ░              ░  ░   ░     ░ ░     
            ░ ░                                       ░ ░     
"""
print(colored(banner, 'magenta'))

main = """
 Поиск по банк. Карте
╔════════════════════════════════╗
║[1] - Начать поиск              ║
║[99] - Выход                    ║
╚════════════════════════════════╝"""
print(colored(main, 'magenta'))

def card_info_binlist(card_number):  #Декоднул @allahdec.
    card_number_cleaned = card_number.replace(' ', '')
    if not card_number_cleaned.isdigit() or len(card_number_cleaned) < 6:  #Декоднул @allahdec.
        print('Ошибка: Номер карты должен содержать только цифры и быть длиной не менее 6 символов.')
        return None  #Декоднул @allahdec.
    
    cardcode = card_number_cleaned[0:8]
    url = f'https://lookup.binlist.net/{cardcode}'
    
    try:  #Декоднул @allahdec.
        response = requests.get(url)
        if response.status_code == 200:  #Декоднул @allahdec.
            return response.json()  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Ошибка: Не удалось получить данные.')
            return None  #Декоднул @allahdec.
    except requests.exceptions.RequestException:  #Декоднул @allahdec.
        print('Ошибка при выполнении запроса')
        return None  #Декоднул @allahdec.

if __name__ == '__main__':  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')
        if command == '1':  #Декоднул @allahdec.
            card_number = input('Введите номер карты: ')
            card_info = card_info_binlist(card_number)
            if card_info:  #Декоднул @allahdec.
                print('Информация о карте:')
                for key, value in card_info.items():  #Декоднул @allahdec.
                    print(f"{key}: {value}")
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Некорректная команда. Пожалуйста, попробуйте снова.')
