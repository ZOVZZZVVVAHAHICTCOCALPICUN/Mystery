#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
from datetime import datetime  #Декоднул @allahdec.
import pytz  #Декоднул @allahdec.
import platform  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
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
import random  #Декоднул @allahdec.

os.system('cls' if os.name == 'nt' else 'clear')

banner = '\n\n\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ \n░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n       ░    ░ ░           ░              ░  ░   ░     ░ ░     \n            ░ ░                                       ░ ░     \n  '
print(colored(banner, 'magenta'))

main = ' My IP Address\n╔══════════════════════════════════╗\n║[Enter] - Обновить страницу       ║\n║[99] - Выход                      ║\n╚══════════════════════════════════╝'
print(colored(main, 'magenta'))

API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'

def get_ip_info():  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        response = requests.get('https://ipinfo.io/json')
        if response.status_code == 200:  #Декоднул @allahdec.
            return response.json()  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            return None  #Декоднул @allahdec.
    except Exception as e:  #Декоднул @allahdec.
        return {'ip': str(e), 'error': 'Не удалось получить IP-адрес'}  #Декоднул @allahdec.

def get_moscow_time():  #Декоднул @allahdec.
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')  #Декоднул @allahdec.

def get_device_info():  #Декоднул @allahdec.
    device = platform.system()
    version = platform.version()
    return f'{device} {version}'  #Декоднул @allahdec.

while True:  #Декоднул @allahdec.
    ip_info = get_ip_info()
    current_time = get_moscow_time()

    if ip_info:  #Декоднул @allahdec.
        ip = ip_info.get('ip', 'Не удалось получить IP')
        location = ip_info.get('city', 'Неизвестно') + ', ' + ip_info.get('region', 'Неизвестно') + ', ' + ip_info.get('country', 'Неизвестно')
        device_info = get_device_info()

        print(colored('Данные вашего IP', 'magenta'))
        print(colored(f'├ Ваш IP-адрес: {ip}', 'magenta'))
        print(colored(f'├ Геопозиция: {location}', 'magenta'))
        print(colored(f'├ Текущая дата и время в Москве: {current_time}', 'magenta'))
        print(colored(f'└ Устройство: {device_info}', 'magenta'))
    else:  #Декоднул @allahdec.
        print('Не удалось получить информацию об IP.')

    command = input('Введите команду: ')
    if command.lower() == '99':  #Декоднул @allahdec.
        print('Выход из программы...')
        os.system('python main.py')
        break  #Декоднул @allahdec.
    time.sleep(10)
