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
main = """ IP Сайта
╔══════════════════════════════════╗
║[1] - Ip Checker                  ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""

print(colored(banner, 'magenta'))
print(colored(main, 'magenta'))

def get_ip_address(url):  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        ip_address = socket.gethostbyname(url)
        return ip_address  #Декоднул @allahdec.
    except socket.gaierror:  #Декоднул @allahdec.
        return None  #Декоднул @allahdec.

def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ').strip()
        if command == '1':  #Декоднул @allahdec.
            url = input('Введите ссылку на сайт\n └ Например example.com: ').strip()
            url = url.replace('http://', '').replace('https://', '').replace('www.', '')
            ip_address = get_ip_address(url)
            if ip_address:  #Декоднул @allahdec.
                print(colored('IP-адрес сайта: ', 'magenta'))
                print(colored(f'└ {url}: {ip_address}', 'magenta'))
            else:  #Декоднул @allahdec.
                print(colored('Не удалось получить IP-адрес. Проверьте правильность введенного URL.', 'magenta'))
        elif command.lower() == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print(colored('Неверная команда. Попробуйте снова.', 'magenta'))

if __name__ == '__main__':  #Декоднул @allahdec.
    main()
