#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import telethon  #Декоднул @allahdec.
from telethon import TelegramClient  #Декоднул @allahdec.
import asyncio  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
import datetime  #Декоднул @allahdec.
import pytz  #Декоднул @allahdec.
import platform  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import fake_useragent  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
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
print(colored(banner, 'magenta'))

main = """ Парсинг Групп Telegram
╔══════════════════════════════════╗
║[1] - Добавить аккаунт            ║
║[2] - Начать Парсинг              ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""
print(colored(main, 'magenta'))


async def get_group_users(client, group_name, filename):
    try:  #Декоднул @allahdec.
        group = await client.get_entity(group_name)
        participants = await client.get_participants(group)
        with open(filename, 'w', encoding='utf-8') as f:  #Декоднул @allahdec.
            for user in participants:  #Декоднул @allahdec.
                user_id = user.id
                first_name = user.first_name if user.first_name else 'None'
                last_name = user.last_name if user.last_name else 'None'
                username = user.username if user.username else 'None'
                f.write(f"{user_id}, {first_name}, {last_name}, {username}\n")
        print(colored(f'Данные о пользователях записаны в файл: {filename}', 'magenta'))
    except Exception as e:  #Декоднул @allahdec.
        print(colored(f'Ошибка при получении пользователей: {e}', 'magenta'))


async def main():
    api_id = input('Введите API Id: ')
    api_hash = input('Введите API hash: ')
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()
    while True:  #Декоднул @allahdec.
        command = input(colored('Введите команду: ', 'magenta'))
        if command == '1':  #Декоднул @allahdec.
            print(colored('Вы успешно вошли в аккаунт Telegram.', 'magenta'))
        elif command == '2':  #Декоднул @allahdec.
            group_name = input('Введите UserName группы\n └ Важно - Не используйте @: ')
            filename = input('Введите название файла для сохранения\n └ Пример [Mystery.txt]: ')
            await get_group_users(client, group_name, filename)
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверная команда\n └ Попробуйте снова.')


if __name__ == '__main__':  #Декоднул @allahdec.
    asyncio.run(main())
