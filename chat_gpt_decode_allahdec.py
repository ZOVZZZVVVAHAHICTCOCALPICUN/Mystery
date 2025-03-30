#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import g4f  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import pyfiglet  #Декоднул @allahdec.
import xlrd  #Декоднул @allahdec.
from openpyxl import load_workbook  #Декоднул @allahdec.
import colorama  #Декоднул @allahdec.
from colorama import init, Fore, Style  #Декоднул @allahdec.
from pystyle import *  #Декоднул @allahdec.
import random  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
from fake_useragent import UserAgent  #Декоднул @allahdec.
import subprocess  #Декоднул @allahdec.
import colorama  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

def clear_console():  #Декоднул @allahdec.
    if os.name == 'nt':  #Декоднул @allahdec.
        os.system('cls')
    else:  #Декоднул @allahdec.
        os.system('clear')

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

main = """ Chat GPT
╔══════════════════════════════════╗
║[1] - Начать                      ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""

clear_console()
print(colored(banner, 'magenta'))
print(colored(main, 'magenta'))

while True:  #Декоднул @allahdec.
    choice = input('Введите опцию: ' + Style.RESET_ALL)
    if choice == '1':  #Декоднул @allahdec.
        user_input = input('Введите ваш запрос: ')
        print(colored('Обработка...', 'magenta'))
        response = g4f.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': user_input}],
        )
        print(response)
    elif choice == '99':  #Декоднул @allahdec.
        print('Выход из программы...')
        os.system('python main.py')
        break  #Декоднул @allahdec.
    else:  #Декоднул @allahdec.
        print('Неверный выбор')
