#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import os  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

os.system('cls' if os.name == 'nt' else 'clear')

banner = '\n\n\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ \n░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n       ░    ░ ░           ░              ░  ░   ░     ░ ░     \n            ░ ░                                       ░ ░     \n  '
print(colored(banner, 'magenta'))

main = ' Зашифровать код\n╔══════════════════════════════════╗\n║[1] - Зашифровать код             ║\n║[99] - Выход                      ║\n╚══════════════════════════════════╝'
print(colored(main, 'magenta'))


def encrypt(text, shift):  #Декоднул @allahdec.
    encrypted_text = ''
    for char in text:  #Декоднул @allahdec.
        if char.isalpha():  #Декоднул @allahdec.
            shift_amount = shift % 26
            if char.islower():  #Декоднул @allahdec.
                start = ord('a')
                encrypted_text += chr((ord(char) - start + shift_amount) % 26 + start)
            else:  #Декоднул @allahdec.
                start = ord('A')
                encrypted_text += chr((ord(char) - start + shift_amount) % 26 + start)
        else:  #Декоднул @allahdec.
            encrypted_text += char
    return encrypted_text  #Декоднул @allahdec.


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')
        if command == '1':  #Декоднул @allahdec.
            path = input('Введите путь к файлу: ')
            try:  #Декоднул @allahdec.
                with open(path, 'r', encoding='utf-8') as file:  #Декоднул @allahdec.
                    code = file.read()
                shift = 3
                encrypted_code = encrypt(code, shift)
                output_filename = input('Введите имя для сохранения зашифрованного файла (без .py): ')
                output_filename += '.py'
                with open(output_filename, 'w', encoding='utf-8') as encrypted_file:  #Декоднул @allahdec.
                    encrypted_file.write(encrypted_code)
                print(f'Отлично, ваш код python зашифрован, и сохранен как: {output_filename}')
            except FileNotFoundError:  #Декоднул @allahdec.
                print('Файл не найден. Проверьте путь и попробуйте снова.')
            except UnicodeDecodeError:  #Декоднул @allahdec.
                print('Ошибка декодирования. Проверьте кодировку вашего файла.')
            except Exception as e:  #Декоднул @allahdec.
                print(f'Произошла ошибка: {e}')
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверная команда. Попробуйте снова.')


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
