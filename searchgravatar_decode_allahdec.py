#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import os  #Декоднул @allahdec.
import hashlib  #Декоднул @allahdec.
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

main_menu = """ Поиск по Gravatar
╔══════════════════════════════════╗
║[1] - Начать поиск                ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""

print(colored(banner, 'magenta'))
print(colored(main_menu, 'magenta'))

def fetch_gravatar_info(email):  #Декоднул @allahdec.
    hash_email = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    gravatar_url = f"https://www.gravatar.com/{hash_email}.json"
    try:  #Декоднул @allahdec.
        response = requests.get(gravatar_url)
        if response.status_code == 200:  #Декоднул @allahdec.
            data = response.json()
            display_user_info(data)
            return  #Декоднул @allahdec.
        print('Пользователь не найден')
    except requests.exceptions.RequestException as e:  #Декоднул @allahdec.
        print(f'Ошибка! {e}')

def display_user_info(data):  #Декоднул @allahdec.
    entry = data.get('entry', [{}])[0] if data.get('entry') else {}
    name = entry.get('displayName', 'N/A')
    about = entry.get('aboutMe', 'N/A')
    profile_url = entry.get('profileUrl', 'N/A')
    thumbnail_url = entry.get('thumbnailUrl', 'N/A')

    print(f"""
Имя: {name}
О себе: {about}
Профиль URL: {profile_url}
Изображение URL: {thumbnail_url}
    """)

def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ').strip()
        if command == '1':  #Декоднул @allahdec.
            search_value = input('Введите электронную почту: ').strip().lower()
            fetch_gravatar_info(search_value)
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверная команда. Пожалуйста, попробуйте снова.')

if __name__ == '__main__':  #Декоднул @allahdec.
    main()
