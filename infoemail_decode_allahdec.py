#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import os  #Декоднул @allahdec.
import colorama  #Декоднул @allahdec.
from colorama import init, Fore  #Декоднул @allahdec.
import shutil  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
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

main = """ Информация о почте
╔════════════════════════════════╗
║[1] - Начать поиск              ║
║[99] - Выход                    ║
╚════════════════════════════════╝"""
print(colored(main, 'magenta'))

def get_email_info(email):  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        username, domain = email.split('@')
        email_services = {
            'gmail.com': 'Google (Gmail)',
            'yahoo.com': 'Yahoo Mail',
            'hotmail.com': 'Microsoft (Hotmail)',
            'outlook.com': 'Microsoft (Outlook)',
            'mail.ru': 'Mail.ru',
            'yandex.ru': 'Yandex.Mail'
        }
        service_name = email_services.get(domain, 'Неизвестный почтовый сервис')

        print(colored('Данные о почте:', 'magenta'))
        print(colored(f' ├ Имя почты: {username}', 'magenta'))
        print(colored(f' ├ Домен: {domain}', 'magenta'))
        print(colored(f' └ Сайт: {service_name}', 'magenta'))
    except ValueError:  #Декоднул @allahdec.
        print('Неверный формат E-mail.')

def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')
        if command == '1':  #Декоднул @allahdec.
            email = input('Введите E-mail: ')
            get_email_info(email)
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверная команда. Пожалуйста, попробуйте снова.')

if __name__ == '__main__':  #Декоднул @allahdec.
    main()
