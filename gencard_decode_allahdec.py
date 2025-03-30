#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import random  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import fake_useragent  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
import pyfiglet  #Декоднул @allahdec.
from fake_useragent import UserAgent  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
import subprocess  #Декоднул @allahdec.
import sys  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import platform  #Декоднул @allahdec.
import webbrowser  #Декоднул @allahdec.

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

main = """ Генератор банковских карт
╔══════════════════════════════════╗
║[1] - Сгенерировать карту         ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""
print(colored(main, 'magenta'))


def luhn_check(card_number):  #Декоднул @allahdec.
    """Проверяет, является ли номер карты корректным по алгоритму Луна."""
    num_digits = len(card_number)
    sum_ = 0
    alternate = False
    for i in range(num_digits - 1, -1, -1):  #Декоднул @allahdec.
        n = int(card_number[i])
        if alternate:  #Декоднул @allahdec.
            n *= 2
            if n > 9:  #Декоднул @allahdec.
                n -= 9
        sum_ += n
        alternate = not alternate
    return sum_ % 10 == 0  #Декоднул @allahdec.


def generate_card_number():  #Декоднул @allahdec.
    """Генерирует корректный номер банковской карты."""
    card_number = [str(random.choice([4, 5]))]
    for _ in range(14):  #Декоднул @allahdec.
        card_number += str(random.randint(0, 9))
    
    for i in range(10):  #Декоднул @allahdec.
        potential_card_number = card_number + [str(i)]
        if luhn_check("".join(potential_card_number)):  #Декоднул @allahdec.
            card_number.append(str(i))
            break  #Декоднул @allahdec.

    return "".join(card_number)  #Декоднул @allahdec.


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        user_input = input('Введите значение: ').strip().lower()

        if user_input == '1':  #Декоднул @allahdec.
            card_number = generate_card_number()
            print('Сгенерированный номер карты:')
            print(colored('└ ' + card_number, 'magenta'))
        elif user_input == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print("Неверная команда. Пожалуйста, введите '1' или '99'.")


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
