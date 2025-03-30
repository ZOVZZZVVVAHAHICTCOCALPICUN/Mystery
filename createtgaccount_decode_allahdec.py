#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
import os  #Декоднул @allahdec.

os.system('cls' if os.name == 'nt' else 'clear')

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

main = ' Дата создания аккаунта Telegram\n╔════════════════════════════════╗\n║[1] - Узнать дату создания      ║\n║[99] - Выход                    ║\n╚════════════════════════════════╝'

print(colored(banner, 'magenta'))
print(colored(main, 'magenta'))

def estimate_creation_date(telegram_id):  #Декоднул @allahdec.
    first_digit = str(telegram_id)[0]
    if first_digit == '1':  #Декоднул @allahdec.
        return '2013 год'  #Декоднул @allahdec.
    elif first_digit == '2':  #Декоднул @allahdec.
        return '2014 год'  #Декоднул @allahdec.
    elif first_digit == '3':  #Декоднул @allahdec.
        return '2015 год'  #Декоднул @allahdec.
    elif first_digit == '4':  #Декоднул @allahdec.
        return '2016 год'  #Декоднул @allahdec.
    elif first_digit == '5':  #Декоднул @allahdec.
        return '2017 год'  #Декоднул @allahdec.
    elif first_digit == '6':  #Декоднул @allahdec.
        return '2018 год'  #Декоднул @allahdec.
    elif first_digit == '7':  #Декоднул @allahdec.
        return '2019 год'  #Декоднул @allahdec.
    elif first_digit == '8':  #Декоднул @allahdec.
        return '2020 год'  #Декоднул @allahdec.
    elif first_digit == '9':  #Декоднул @allahdec.
        return '2021 год'  #Декоднул @allahdec.
    else:  #Декоднул @allahdec.
        return 'Неизвестный ID или аккаунт создан после 2021 года.'  #Декоднул @allahdec.

def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Ваш выбор: ')
        if command == '1':  #Декоднул @allahdec.
            try:  #Декоднул @allahdec.
                telegram_id = input('Введите ID Telegram аккаунта: ')
                telegram_id = int(telegram_id)
                creation_date = estimate_creation_date(telegram_id)
                print(colored('Предположительная дата создания аккаунта:', 'magenta'))
                print(colored(' └ ' + str(creation_date), 'magenta'))
            except ValueError:  #Декоднул @allahdec.
                print('Ошибка: Введите корректный числовой ID.')
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Некорректная команда. Пожалуйста, попробуйте снова.')

if __name__ == '__main__':  #Декоднул @allahdec.
    main()
