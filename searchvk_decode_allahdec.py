#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import os  #Декоднул @allahdec.
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
░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ 
░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  
       ░    ░ ░           ░              ░  ░   ░     ░ ░     
            ░ ░                                       ░ ░     
"""

print(colored(banner, 'magenta'))

main_menu = """ Поиск по VK
╔══════════════════════════════════╗
║[1] - Поиск                       ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""

print(colored(main_menu, 'magenta'))

VK_TOKEN = '0af157510af157510af15751aa0a89e69600af10af157516a0bc15996e74fe2b440998c'
VK_API_URL = 'https://api.vk.com/method/users.get'

def get_user_info(user_id):  #Декоднул @allahdec.
    params = {
        'access_token': VK_TOKEN,
        'v': '5.131',
        'user_ids': user_id,
        'fields': 'first_name,last_name,status,sex,city,country,photo_max_orig,mobile_phone,home_phone'
    }
    response = requests.get(VK_API_URL, params=params)

    if response.status_code != 200:  #Декоднул @allahdec.
        print(f"Ошибка: {response.status_code}")
        return None  #Декоднул @allahdec.

    data = response.json()

    if 'response' not in data:  #Декоднул @allahdec.
        print('Пользователь не найден или произошла ошибка.')
        return None  #Декоднул @allahdec.

    if not data['response']:  #Декоднул @allahdec.
        print('Пользователь не найден или произошла ошибка.')
        return None  #Декоднул @allahdec.

    return data['response'][0]  #Декоднул @allahdec.


def display_user_info(user):  #Декоднул @allahdec.
    print(colored(" Данные:\n ├ Имя: " + user.get('first_name', 'Не найдено'), 'magenta'))
    print(colored(" ├ Фамилия: " + user.get('last_name', 'Не найдено'), 'magenta'))
    print(colored(" ├ Статус: " + user.get('status', 'Не найден'), 'magenta'))
    sex = user.get('sex')
    if sex == 2:  #Декоднул @allahdec.
        print(colored(" ├ Пол: Мужской", 'magenta'))
    elif sex == 1:  #Декоднул @allahdec.
        print(colored(" ├ Пол: Женский", 'magenta'))
    else:  #Декоднул @allahdec.
        print(colored(" ├ Пол: Не указан", 'magenta'))

    city = user.get('city')
    if city:  #Декоднул @allahdec.
        print(colored(" ├ Город: " + city.get('title', 'Не найден'), 'magenta'))
    else:  #Декоднул @allahdec.
        print(colored(" ├ Город: Не найден", 'magenta'))

    country = user.get('country')
    if country:  #Декоднул @allahdec.
        print(colored(" ├ Страна: " + country.get('title', 'Не найдена'), 'magenta'))
    else:  #Декоднул @allahdec.
        print(colored(" ├ Страна: Не найдена", 'magenta'))
    print(colored(" ├ Мобильный телефон: " + user.get('mobile_phone', 'Не найден'), 'magenta'))
    print(colored(" └ Домашний телефон: " + user.get('home_phone', 'Не найден'), 'magenta'))


if __name__ == '__main__':  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')

        if command == '1':  #Декоднул @allahdec.
            user_id = input('Введите ID / Username пользователя: ')
            user = get_user_info(user_id)
            if user:  #Декоднул @allahdec.
                display_user_info(user)
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            exit()
        else:  #Декоднул @allahdec.
            print('Неверная команда. Пожалуйста, попробуйте снова.')
