#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
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
main = ' Проверка нагрузки на сайт\n╔══════════════════════════════════╗\n║[1] - Начать тест                 ║\n║[99] - Выход                      ║\n╚══════════════════════════════════╝'

print(colored(banner, 'magenta'))
print(colored(main, 'magenta'))


def check_site_load(url):  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        start_time = time.time()
        response = requests.get(url)
        response_time = time.time() - start_time
        if response.status_code == 200:  #Декоднул @allahdec.
            print(colored(f"Сайт {url} доступен.", 'magenta'))
            print(colored(f"├ Время ответа: {response_time:.2f} секунд.", 'magenta'))
            if response_time < 1:  #Декоднул @allahdec.
                print(colored("├ Нагрузка на сайт:\n└ Низкая", 'magenta'))
                return  #Декоднул @allahdec.
            if response_time < 3:  #Декоднул @allahdec.
                print(colored("├ Нагрузка на сайт:\n└ Средняя", 'magenta'))
                return  #Декоднул @allahdec.
            print(colored("├ Нагрузка на сайт:\n└ Высокая", 'magenta'))
            return  #Декоднул @allahdec.
        print(f"Сайт {url} недоступен:\n└ Статус код: {response.status_code}")
    except requests.exceptions.RequestException as e:  #Декоднул @allahdec.
        print(f"Ошибка при обращении к сайту {url}: {e}")


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ').strip()
        if command == '1':  #Декоднул @allahdec.
            url = input('Введите ссылку на сайт\n└ например [https://www.example.com]: ').strip()
            check_site_load(url)
        elif command.lower() == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверная команда\n└ Попробуйте снова.')


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
