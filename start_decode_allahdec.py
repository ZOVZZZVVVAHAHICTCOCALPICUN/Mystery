#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import time  #Декоднул @allahdec.
import sys  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
from colorama import init, Fore, Style  #Декоднул @allahdec.
import fake_useragent  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
import pyfiglet  #Декоднул @allahdec.
from fake_useragent import UserAgent  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

banner = """
 ⣸⠒⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠑⠄⡀⠀⠀⠀⣀⠀⠀⠀
⠃⠀⠀⠀⠀⠀⢈⣵⣦⢸⣿⡧⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⣿⣾⢏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣼⣿⢟⣷⣷⣆⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⡿⠈⢆
⠀⠀⠀⠀⠀⢰⢸⣿⣿⣿⣿⠇⠀⠈
⠀⠀⠀⠀⠀⢸⢸⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⡈⣼⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠾⢿⣿⣿⠿⠿⣿⡿⠀
"""


init(autoreset=True)


def clear_console():  #Декоднул @allahdec.
    if os.name == 'nt':  #Декоднул @allahdec.
        os.system('cls')
    else:  #Декоднул @allahdec.
        os.system('clear')


def animated_print(text, delay, colors):  #Декоднул @allahdec.
    for char in text:  #Декоднул @allahdec.
        if colors:  #Декоднул @allahdec.
            color = colors[len(text) % len(colors)]
            print(color + char, end='', flush=True)
        else:  #Декоднул @allahdec.
            print(char, end='', flush=True)
        time.sleep(delay)
    print()


def smooth_text_print(text, delay):  #Декоднул @allahdec.
    for char in text:  #Декоднул @allahdec.
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def main():  #Декоднул @allahdec.
    clear_console()
    colors = [Fore.MAGENTA]
    animated_print(banner, 0.02, colors)
    main_text = """
    Настройка софта:
    1. API-Ключ - Заходим в бота LeakOsint и пишем /api
    и получаем ключ, после чего копируем его и вставляем
    в файл key.txt после чего перезаходим в софт.

    2. При использовании и эксплуатации программы
    используйте vpn/proxy.

    3. В программе используются сервисы, которые
    насчитывают в себе около 16.6 терабайт памяти.

    4. 70% данных содержат в себе RU данные.

    О программе:
    Программа [Mystery] не рассчитана на продажи
    если вы скачали кряк/репак и подцепили локкер,
    стфиллер, троян то это не мои проблемы, качайте
    программу из официального источника

    Официальный телеграм канал:
    @decoded_softs

    Владелец:
    https://t.me/decoded_softs
    """
    smooth_text_print(main_text, 0.01)
    smooth_text_print('//////////////////////////////////////////////////////////////////////////////////////////', 0.05)
    smooth_text_print('Нажмите Enter для выхода.')
    input()
    os.system('python main.py')


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
