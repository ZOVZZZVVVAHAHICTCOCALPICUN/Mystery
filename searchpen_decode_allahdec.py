#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import os  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

if os.name == 'nt':  #Декоднул @allahdec.
    os.system('cls')
else:  #Декоднул @allahdec.
    os.system('clear')

banner = '''
 ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓
▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒
▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░
▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░
▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░
░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ 
░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░         ░     ░░   ░ ▒ ▒ ░░  
       ░    ░ ░           ░              ░  ░   ░     ░ ░     
            ░ ░                                       ░ ░     
'''

main = ''' Поиск по Размеру Члена
╔════════════════════════════════╗
║[1] - Начать поиск              ║
║[99] - Выход                    ║
╚════════════════════════════════╝'''

print(colored(banner, 'magenta'))
print(colored(main, 'magenta'))

def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')
        if command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        elif command == '1':  #Декоднул @allahdec.
            user_input = input('Введите сантиметры размера члена: ')
            if user_input.isdigit():  #Декоднул @allahdec.
                print('Ищем данные с размером - ' + user_input)
                print('Данные найдены! Местоположение: Твое очко, проверь попку)')
            else:  #Декоднул @allahdec.
                print('Введите сантиметры.')
        else:  #Декоднул @allahdec.
            print('Ошибка: Неверная команда.')

if __name__ == '__main__':  #Декоднул @allahdec.
    main()
