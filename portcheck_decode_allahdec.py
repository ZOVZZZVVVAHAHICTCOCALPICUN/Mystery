#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import socket  #Декоднул @allahdec.
import threading  #Декоднул @allahdec.
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

def scan_port(host, port):  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:  #Декоднул @allahdec.
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:  #Декоднул @allahdec.
                open_ports.append(port)
                print(f"{colored('✔', 'green')} Порт {port} {colored('открыт', 'green')}. (TCP)")
            else:  #Декоднул @allahdec.
                print(f"{colored('✖', 'red')} Порт {port} {colored('закрыт', 'red')}.")
    except:  #Декоднул @allahdec.
        pass  #Декоднул @allahdec.

if __name__ == '__main__':  #Декоднул @allahdec.
    open_ports = []
    if os.name == 'nt':  #Декоднул @allahdec.
        system('cls')
    else:  #Декоднул @allahdec.
        system('clear')
    print(colored(banner, 'magenta'))
    
    target_host = input("Введите домен или IP-адрес для сканирования \nПример(example.com): ").strip()
    if target_host.startswith("http://"):  #Декоднул @allahdec.
        target_host = target_host[7:]
    elif target_host.startswith("https://"):  #Декоднул @allahdec.
        target_host = target_host[8:]
    
    try:  #Декоднул @allahdec.
        ip_address = socket.gethostbyname(target_host)
        print('\nРазрешён IP-адрес: ' + ip_address)
        ports_to_scan = (20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 143, 443, 3306, 514, 123, 5900, 6000, 8080)
        threads = []
        print('\nСканируем порты на ' + target_host + ' (' + ip_address + ')...')
        for port in ports_to_scan:  #Декоднул @allahdec.
            thread = threading.Thread(target=scan_port, args=(ip_address, port))
            threads.append(thread)
            thread.start()
        for thread in threads:  #Декоднул @allahdec.
            thread.join()
    except socket.gaierror as e:  #Декоднул @allahdec.
        print(colored('Ошибка: Не удалось разрешить доменное имя.', 'red'))
        print('Подробности: ' + str(e))
