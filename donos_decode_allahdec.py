#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import pystyle  #Декоднул @allahdec.
from pystyle import Write, Colors  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
from bs4 import BeautifulSoup  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import random  #Декоднул @allahdec.
import fake_useragent  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
import pyfiglet  #Декоднул @allahdec.
from fake_useragent import UserAgent  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

os.system('cls' if os.name == 'nt' else 'clear')

url = 'http://xn--d1asbbbhie.xn--p1ai/report/'

user_agents = [
    'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.7228.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/90.0.0.0 Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.1257.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/79.0.0.0 Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.5234.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/79.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.3170.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/66',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/73.0.0.0 Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.7979.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/108.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/38.0.0.0 Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.5070.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.7640.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/49.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4688.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/90.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3182.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.9176.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/71',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/73.0.0.0 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.6900.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/59.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.6232.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/45.0.0.0 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6601.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/105.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.7252.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/32.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3745.0 Safari/537.36'
]

use_colors = False

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

main = """ Отправить Донос РФ
╔════════════════════════════════╗
║[1] - Отправить донос           ║
║[99] - Выход                    ║
╚════════════════════════════════╝"""


def get_csrf_token():  #Декоднул @allahdec.
    headers = {'User-Agent': random.choice(user_agents)}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    token = soup.find('input', {'name': '_token'})['value']
    return token  #Декоднул @allahdec.


def get_institutions():  #Декоднул @allahdec.
    headers = {'User-Agent': random.choice(user_agents)}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    institutions = soup.find('select', {'name': 'institution'}).find_all('option')
    return [(option['value'], option.text.strip()) for option in institutions]  #Декоднул @allahdec.


def send_report(csrf_token, institution, body, is_anonymous, name, email, phone):  #Декоднул @allahdec.
    headers = {'User-Agent': random.choice(user_agents)}
    data = {
        '_token': csrf_token,
        'institution': institution,
        'body': body,
        'name': name,
        'email': email,
        'phone': phone,
        'anonymously': 'on' if is_anonymous else '',
        'allow_publish': 'on'
    }
    response = requests.post(url, headers=headers, data=data)
    return response.status_code == 200  #Декоднул @allahdec.


def print_colored(text, color, interval):  #Декоднул @allahdec.
    if use_colors:  #Декоднул @allahdec.
        Write.Print(text, color, interval=interval)
    else:  #Декоднул @allahdec.
        print(text)


def input_colored(prompt, color, interval):  #Декоднул @allahdec.
    if use_colors:  #Декоднул @allahdec.
        return Write.Input(prompt, color, interval=interval)  #Декоднул @allahdec.
    else:  #Декоднул @allahdec.
        return input(prompt)  #Декоднул @allahdec.


def main_menu():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        choice = input_colored('Выберите действие: ', Colors.black_to_red, interval=0.0001)
        if choice == '1':  #Декоднул @allahdec.
            csrf_token = get_csrf_token()
            institution_list = get_institutions()
            print_colored('Выберите ведомство:\n', Colors.black_to_red, interval=0.0001)
            for i, (value, name) in enumerate(institution_list, 1):  #Декоднул @allahdec.
                print_colored(str(i) + '. ' + name + '\n', Colors.black_to_red, interval=0.0001)

            institution_index = int(input_colored('Введите номер ведомства: ', Colors.black_to_red, interval=0.0001)) - 1
            institution = institution_list[institution_index][0]
            body = input_colored('Введите текст доноса: ', Colors.black_to_red, interval=0.0001)
            is_anonymous = input_colored('Анонимно? (да/нет): ', Colors.black_to_red, interval=0.0001).lower() == 'да'

            if not is_anonymous:  #Декоднул @allahdec.
                name = input_colored('Введите ФИО: ', Colors.black_to_red, interval=0.0001)
                email = input_colored('Введите Email: ', Colors.black_to_red, interval=0.0001)
                phone = input_colored('Введите Телефон: ', Colors.black_to_red, interval=0.0001)
            else:  #Декоднул @allahdec.
                name = ''
                email = ''
                phone = ''

            if send_report(csrf_token, institution, body, is_anonymous, name, email, phone):  #Декоднул @allahdec.
                print_colored('Донос успешно отправлен!\n', Colors.black_to_green, interval=0.0001)
            else:  #Декоднул @allahdec.
                print_colored('Ошибка при отправке доноса.\n', Colors.black_to_red, interval=0.0001)

            input_colored('Нажмите Enter для возврата в меню...', Colors.black_to_red, interval=0.0001)
            clear_screen()
        elif choice == '92826':  #Декоднул @allahdec.
            use_colors = not use_colors
            print_colored('Цвета ' + ('включены' if use_colors else 'выключены') + '\n', Colors.black_to_red, interval=0.0001)
            input_colored('Нажмите Enter для возврата в меню...', Colors.black_to_red, interval=0.0001)
            clear_screen()
        elif choice == '99':  #Декоднул @allahdec.
            print('Переходим на главную страницу...')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            clear_screen()


def clear_screen():  #Декоднул @allahdec.
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':  #Декоднул @allahdec.
    main_menu()
