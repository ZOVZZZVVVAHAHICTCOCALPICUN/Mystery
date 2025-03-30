#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import socket  #Декоднул @allahdec.
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

system = os.system
name = os.name

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


def check_database_type(port):  #Декоднул @allahdec.
    database_types = {
        3306: 'MySQL',
        5432: 'PostgreSQL',
        1433: 'MSSQL',
        27017: 'MongoDB',
        1521: 'Oracle',
        6379: 'Redis',
        27018: 'MongoDB (Secondary)',
        8086: 'InfluxDB',
        5439: 'Amazon Redshift',
        9200: 'Elasticsearch',
        27000: 'Cassandra'
    }
    return database_types.get(port, 'Unknown')  #Декоднул @allahdec.


def check_port(host, port):  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  #Декоднул @allahdec.
            s.settimeout(2)
            if s.connect_ex((host, port)) == 0:  #Декоднул @allahdec.
                return True  #Декоднул @allahdec.
    except socket.error:  #Декоднул @allahdec.
        return False  #Декоднул @allahdec.


def main(hostname):  #Декоднул @allahdec.
    open_ports = []
    for port in [3306, 5432, 1433, 27017, 1521, 6379, 27018, 8086, 5439, 9200, 27000]:  #Декоднул @allahdec.
        if check_port(hostname, port):  #Декоднул @allahdec.
            open_ports.append(port)

    if open_ports:  #Декоднул @allahdec.
        for port in open_ports:  #Декоднул @allahdec.
            print(colored(f'Порт {port} открыт, исходя из этого тип базы данных скорее всего:', 'magenta'))
            print(colored(f'└ {check_database_type(port)}', 'magenta'))
    else:  #Декоднул @allahdec.
        print(colored('Не удалось найти открытые порты для баз данных.', 'magenta'))


def main_menu():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        host = input('Введите домен или IP-адрес (или нажмите Enter для выхода): ')
        if host == '':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        main(host)
        print('Нажмите Enter')
        time.sleep(1)
        os.system('python main.py')


if __name__ == '__main__':  #Декоднул @allahdec.
    system('cls' if os.name == 'nt' else 'clear')
    print(colored(banner, 'magenta'))
    main_menu()
