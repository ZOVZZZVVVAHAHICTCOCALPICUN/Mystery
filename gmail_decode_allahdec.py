#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import json  #Декоднул @allahdec.
import socket  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import fake_useragent  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
import pyfiglet  #Декоднул @allahdec.
from fake_useragent import UserAgent  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

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
main = """ Создать Почту Gmail
╔══════════════════════════════════╗
║[1] - Создать почту Gmail         ║
║[2] - Лист созданных почт         ║
║[99] - Выход                      ║ 
╚══════════════════════════════════╝"""

print(colored(banner, 'magenta'))
print(colored(main, 'magenta'))


def load_accounts():  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        with open('accounts.json', 'r') as file:  #Декоднул @allahdec.
            return json.load(file)  #Декоднул @allahdec.
    except FileNotFoundError:  #Декоднул @allahdec.
        return {}  #Декоднул @allahdec.


def save_accounts(accounts):  #Декоднул @allahdec.
    with open('accounts.json', 'w') as file:  #Декоднул @allahdec.
        json.dump(accounts, file)


def register():  #Декоднул @allahdec.
    username = input('Введите имя пользователя (без @gmail.com): ')
    password = input('Введите пароль: ')  #Декоднул @allahdec.
    email = f'{username}@gmail.com'
    accounts = load_accounts()

    if email in accounts:  #Декоднул @allahdec.
        print(colored('Эта учетная запись уже существует.', 'magenta'))
        return  #Декоднул @allahdec.

    accounts[email] = password
    save_accounts(accounts)
    print(colored(f'Учетная запись {email} успешно создана!', 'magenta'))


def view_accounts():  #Декоднул @allahdec.
    accounts = load_accounts()

    if not accounts:  #Декоднул @allahdec.
        print('Нет созданных учетных записей.')
        return  #Декоднул @allahdec.

    print(colored('Созданные учетные записи:', 'magenta'))
    for email, password in accounts.items():  #Декоднул @allahdec.
        print(colored(f'Почта: {email}, Пароль: {password}', 'magenta'))


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите номер команды: ')

        if command == '1':  #Декоднул @allahdec.
            register()
        elif command == '2':  #Декоднул @allahdec.
            view_accounts()
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверная команда. Пожалуйста, попробуйте снова.')


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
