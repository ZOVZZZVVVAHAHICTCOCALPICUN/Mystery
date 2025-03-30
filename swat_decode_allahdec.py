#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import os  #Декоднул @allahdec.
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
░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░         ░     ░░   ░ ▒ ▒ ░░  
       ░    ░ ░           ░              ░  ░   ░     ░ ░     
            ░ ░                                       ░ ░     
"""

print(colored(banner, 'magenta'))

def replace_chars(text, use_fence):  #Декоднул @allahdec.
    replacements = {
        'А': 'А', 'а': 'а', 'Б': 'Б', 'б': 'б', 'В': 'B', 'в': 'в', 'Г': 'Г', 'г': 'г',
        'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'Ё', 'ё': 'ё', 'Ж': 'Ж', 'ж': 'Ж',
        'З': '3', 'з': '3', 'И': 'U', 'и': 'u', 'й': 'й', 'К': 'K', 'к': 'k', 'Л': 'JI',
        'л': 'JI', 'М': 'M', 'м': 'м', 'Н': 'Н', 'н': 'н', 'о': '0', 'п': 'n', 'р': 'p',
        'с': 'c', 'С': 'S', 'T': 'y', 'ф': 'x', 'ч': '4', 'Ч': '4', 'ш': 'III', 'Ш': 'III',
        'щ': 'ъ', 'ъ': 'bI', 'ы': 'ы', 'Ы': 'Ы', 'ю': 'ю', 'я': 'я',
    }
    replacements.update(dict.fromkeys(('т', 'у', 'ф', 'х', 'ч', 'Ч', 'ш', 'Ш', 'щ', 'ъ', 'ы', 'Ы', 'ю', 'я')))
    result = ''
    for char in text:  #Декоднул @allahdec.
        if use_fence:  #Декоднул @allahdec.
            result += replacements.get(char.upper(), char)
        else:  #Декоднул @allahdec.
            result += replacements.get(char.upper(), char.upper())
    return result  #Декоднул @allahdec.

import random  #Декоднул @allahdec.
import os  #Декоднул @allahdec.

main = """ Текст для Сватинга
╔════════════════════════════════╗
║[1] - ВblвОд в ВuдЕ 3а60рА      ║
║[2] - ВСЕ ЗАГЛАВНЫЕ             ║
║[99] - Выход                    ║
╚════════════════════════════════╝"""

print(colored(main, 'magenta'))

option = input('Выберите опцию: ')

if option not in ('1', '2', '99'):  #Декоднул @allahdec.
    print('Ошибка: Неправильная опция.')
    exit()

if option == '1':  #Декоднул @allahdec.
    user_input = input('Введите текст: ')
    replaced_text = replace_chars(user_input, True)
    print('Результат замены:\n    ')
    print(replaced_text)
    

elif option == '99':  #Декоднул @allahdec.
    print('Выход из программы.')
    os.system('python main.py')
    exit()

else:  #Декоднул @allahdec.
    user_input = input('Введите текст: ')
    replaced_text = replace_chars(user_input, False)
    print('Результат замены:\n    ')
    print(replaced_text)
