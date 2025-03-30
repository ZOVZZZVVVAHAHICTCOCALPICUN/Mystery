#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import os  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import googlesearch  #Декоднул @allahdec.
from googlesearch import search  #Декоднул @allahdec.
import random  #Декоднул @allahdec.
import re  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

os.system('cls' if os.name == 'nt' else 'clear')

banner = '\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n       ░    ░ ░           ░              ░  ░   ░     ░ ░     \n            ░ ░                                       ░ ░     \n'
print(colored(banner, 'magenta'))
main = ' Поиск по Email\n╔════════════════════════════════╗\n║[1] - Начать поиск              ║\n║[99] - Выход                    ║\n╚════════════════════════════════╝'
print(colored(main, 'magenta'))


def main():  #Декоднул @allahdec.
    email = input('Введите email: ')
    if email.strip():  #Декоднул @allahdec.
        regex = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\\b'
        if re.fullmatch(regex, email):  #Декоднул @allahdec.
            print('Валидный email.️')
        else:  #Декоднул @allahdec.
            print('ХАХАХАХАХХА ЕБАТЬ ТЫ ЛОХ ЭТО НОН ВАЛИД, ЕБАТЬ ТЫ КЛОУН')
            return None  #Декоднул @allahdec.
        dom = []
        dom.extend(['com', 'com.tw', 'co.in', 'be', 'de', 'co.uk', 'co.ma', 'dz', 'ru', 'ca'])
        tld = random.choice(dom)
        print('Запуск socialscan...')
        time.sleep(3)
        os.system(f'socialscan {email}')
        print('Сканирование завершено.')
        return None  #Декоднул @allahdec.
    else:  #Декоднул @allahdec.
        print('Ошибка: вы должны ввести email.')
        time.sleep(2)
        return None  #Декоднул @allahdec.


if __name__ == '__main__':  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')
        if command == '1':  #Декоднул @allahdec.
            main()
        elif command == '99':  #Декоднул @allahdec.
            print('Завершение программы.')
            os.system('python main.py')
            return None  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Некорректная команда.')
