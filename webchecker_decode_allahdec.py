#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
import os  #Декоднул @allahdec.

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

main = """ Поиск Уязвимостей Сайта
╔══════════════════════════════════╗
║[1] - Начать поиск уязвимостей    ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""

print(colored(banner, 'magenta'))
print(colored(main, 'magenta'))

def check_xss(url):  #Декоднул @allahdec.
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url + '/search?q=' + payload)
    return payload in response.text  #Декоднул @allahdec.

def check_admin_panel(url):  #Декоднул @allahdec.
    response = requests.get(url + '/admin')
    return response.status_code == 200  #Декоднул @allahdec.

def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')
        if command == '1':  #Декоднул @allahdec.
            site = input('Введите ссылку\n └ [без https://]: ')
            url = 'https://' + site
            print(f'Проверка уязвимостей для {url}...')
            xss_result = check_xss(url)
            admin_panel_result = check_admin_panel(url)
            print(colored('Найденные уязвимости:', 'magenta'))
            print(colored(' ├ XSS: ' + ('True' if xss_result else 'Folse'), 'magenta'))
            print(colored(' └ Admin Panel: ' + ('True' if admin_panel_result else 'Folse'), 'magenta'))
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверная команда. Попробуйте снова.')

if __name__ == '__main__':  #Декоднул @allahdec.
    main()
