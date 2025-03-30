#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import random  #Декоднул @allahdec.
import string  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.


os.system('cls' if os.name == 'nt' else 'clear')

banner = '\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ \n░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n       ░    ░ ░           ░              ░  ░   ░     ░ ░     \n            ░ ░                                       ░ ░     \n'
main = ' Генератор Key LeakOsint\n╔══════════════════════════════════╗\n║[1] - Сгенерировать ключи         ║\n║[99] - Выход                      ║\n╚══════════════════════════════════╝'
print(colored(banner, 'magenta'))
print(colored(main, 'magenta'))


def generate_key():  #Декоднул @allahdec.
    number_part = ''.join(random.choices(string.digits, k=10))
    letters_part = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"{number_part}:{letters_part}"  #Декоднул @allahdec.


def save_keys_to_file(filename, count):  #Декоднул @allahdec.
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:  #Декоднул @allahdec.
        for _ in range(count):  #Декоднул @allahdec.
            key = generate_key()
            file.write(key + '\n')
    print(f"{count} ключей успешно сохранено в папку generate в файл {filename}")


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')
        if command == '1':  #Декоднул @allahdec.
            output_file = 'generate/keyleakosint.txt'
            try:  #Декоднул @allahdec.
                number_of_keys = int(input('Введите количество ключей для генерации: '))
                save_keys_to_file(output_file, number_of_keys)
            except ValueError:  #Декоднул @allahdec.
                print('Пожалуйста, введите корректное число.')
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Некорректная команда. Пожалуйста, попробуйте снова.')


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
