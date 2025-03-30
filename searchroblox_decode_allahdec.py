#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

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
░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░         ░     ░░   ░ ▒ ▒ ░░  
       ░    ░ ░           ░              ░  ░   ░     ░ ░     
            ░ ░                                       ░ ░     
"""

main_menu = """ Поиск по Roblox
╔════════════════════════════════╗
║[1] - Начать поиск              ║
║[99] - Выход                    ║
╚════════════════════════════════╝"""

print(colored(banner, 'magenta'))
print(colored(main_menu, 'magenta'))


def get_user_info(user_id):  #Декоднул @allahdec.
    user_info_response = requests.get(f'https://users.roblox.com/v1/users/{user_id}')
    return user_info_response.json()  #Декоднул @allahdec.


def print_user_info(user_info):  #Декоднул @allahdec.
    userid = user_info.get('id', 'None')
    display_name = user_info.get('displayName', 'None')
    username = user_info.get('name', 'None')
    description = user_info.get('description', 'None')
    created_at = user_info.get('created', 'None')
    is_banned = user_info.get('isBanned', 'None')
    external_app_display_name = user_info.get('externalAppDisplayName', 'None')
    has_verified_badge = user_info.get('hasVerifiedBadge', False)

    print(f'User ID: {userid}')
    print(f' ├ Display Name: {display_name}')
    print(f' ├ Username: {username}')
    print(f' ├ Description: {description}')
    print(f' ├ Created At: {created_at}')
    print(f' ├ Is Banned: {is_banned}')
    print(f' ├ External App Display Name: {external_app_display_name}')
    print(f' └ Has Verified Badge: {has_verified_badge}')


def roblox():  #Декоднул @allahdec.
    choice = input('Выберите команду: [1] Ввести Username | [2] Username ID: ')

    if choice == '1':  #Декоднул @allahdec.
        username_input = input('\nUsername: ')
        response = requests.post('https://users.roblox.com/v1/usernames/users',
                                 json={'usernames': [username_input], 'excludeBannedUsers': True})
        data = response.json()

        if data['data']:  #Декоднул @allahdec.
            user_id = data['data'][0]['id']
            user_info = get_user_info(user_id)
            print_user_info(user_info)
            return None  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print(' └ Пользователь не найден.')
            return None  #Декоднул @allahdec.

    elif choice == '2':  #Декоднул @allahdec.
        user_id = input('\nID: ')
        user_info = get_user_info(user_id)

        if 'id' in user_info:  #Декоднул @allahdec.
            print_user_info(user_info)
            return None  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print(' └ Пользователь не найден.')
            return None  #Декоднул @allahdec.
    else:  #Декоднул @allahdec.
        print('Неверный выбор. Пожалуйста, попробуйте снова.')
        return None  #Декоднул @allahdec.


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        start_choice = input('Введите команду: ')

        if start_choice == '1':  #Декоднул @allahdec.
            roblox()
        elif start_choice == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return None  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print("Неверный ввод. Пожалуйста, введите '1' для начала или '99' для выхода.")


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
