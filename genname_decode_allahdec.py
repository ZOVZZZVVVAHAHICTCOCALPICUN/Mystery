#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import random  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import fake_useragent  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
import pyfiglet  #Декоднул @allahdec.
from fake_useragent import UserAgent  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
import subprocess  #Декоднул @allahdec.
import sys  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import platform  #Декоднул @allahdec.
import webbrowser  #Декоднул @allahdec.

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
main = """ Генератор ФИО
╔══════════════════════════════════╗
║[1] - Генератор ФИО               ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""

print(colored(banner, 'magenta'))
print(colored(main, 'magenta'))


def generate_full_name():  #Декоднул @allahdec.
    surnames = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Лебедев', 'Смирнов', 'Гвоздев', 'Умников', 'Золотарев',
                'Пантелеев', 'Героинов', 'Сергеев', 'Воронин', 'Вавилонов']
    names = ['Александр', 'Дмитрий', 'Сергей', 'Николай', 'Амир', 'Михаил', 'Кирилл', 'Геннадий', 'Иван', 'Евгений']
    patronymics = ['Иванович', 'Петрович', 'Сидорович', 'Кузнецович', 'Амирович', 'Михайлович', 'Кириллович',
                   'Иванович', 'Евгеньевич', 'Героинович']

    surname = random.choice(surnames)
    name = random.choice(names)
    patronymic = random.choice(patronymics)

    full_name = f"{surname} {name} {patronymic}"
    return full_name  #Декоднул @allahdec.


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')
        if command == '1':  #Декоднул @allahdec.
            print(generate_full_name())
        elif command.lower() == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print("Неизвестная команда. Пожалуйста, введите '1' для генерации ФИО или '99' для выхода.")


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
