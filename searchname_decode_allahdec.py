#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
from bs4 import BeautifulSoup  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
import os  #Декоднул @allahdec.

os.system('cls' if os.name == 'nt' else 'clear')

banner = '\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ \n░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n       ░    ░ ░           ░              ░  ░   ░     ░ ░     \n            ░ ░                                       ░ ░     \n'
print(colored(banner, 'magenta'))

main = ' Поиск по Ф.И.О\n╔══════════════════════════════════╗\n║[1] - Начать Поиск                ║\n║[99] - Выход                      ║\n╚══════════════════════════════════╝'
print(colored(main, 'magenta'))


def slow_print(text, delay):  #Декоднул @allahdec.
    for char in text:  #Декоднул @allahdec.
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def search_pipl(full_name):  #Декоднул @allahdec.
    url = 'https://pipl.com/search/?q=' + full_name.replace(' ', '%20')
    response = requests.get(url)
    if response.status_code == 200:  #Декоднул @allahdec.
        soup = BeautifulSoup(response.content, 'html.parser')
        return 'Информация найдена на Pipl'  #Декоднул @allahdec.
    return None  #Декоднул @allahdec.


def search_whitepages(full_name):  #Декоднул @allahdec.
    url = 'https://www.whitepages.com/name/' + full_name.replace(' ', '-')
    response = requests.get(url)
    if response.status_code == 200:  #Декоднул @allahdec.
        soup = BeautifulSoup(response.content, 'html.parser')
        return 'Информация найдена на Whitepages'  #Декоднул @allahdec.
    return None  #Декоднул @allahdec.


def search_truepeoplesearch(full_name):  #Декоднул @allahdec.
    url = 'https://www.truepeoplesearch.com/results?name=' + full_name.replace(' ', '%20')
    response = requests.get(url)
    if response.status_code == 200:  #Декоднул @allahdec.
        soup = BeautifulSoup(response.content, 'html.parser')
        return 'Информация найдена на TruePeopleSearch'  #Декоднул @allahdec.
    return None  #Декоднул @allahdec.


def search_zabasearch(full_name):  #Декоднул @allahdec.
    url = 'https://www.zabasearch.com/people/' + full_name.replace(' ', '-') + '/'
    response = requests.get(url)
    if response.status_code == 200:  #Декоднул @allahdec.
        soup = BeautifulSoup(response.content, 'html.parser')
        return 'Информация найдена на ZabaSearch'  #Декоднул @allahdec.
    return None  #Декоднул @allahdec.


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        choice = input('Введите команду: ').strip()
        if choice == '1':  #Декоднул @allahdec.
            full_name = input('Введите ф.и.о: ').strip()
            print('Информацию по имени: {}'.format(full_name))

            pipl_result = search_pipl(full_name)
            whitepages_result = search_whitepages(full_name)
            truepeoplesearch_result = search_truepeoplesearch(full_name)
            zabasearch_result = search_zabasearch(full_name)

            print('Результаты поиска:')
            if pipl_result:  #Декоднул @allahdec.
                print('Pipl: ' + pipl_result)
            else:  #Декоднул @allahdec.
                print('Pipl: Ничего не найдено')
            if whitepages_result:  #Декоднул @allahdec.
                print('Whitepages: ' + whitepages_result)
            else:  #Декоднул @allahdec.
                print('Whitepages: Ничего не найдено')
            if truepeoplesearch_result:  #Декоднул @allahdec.
                print('TruePeopleSearch: ' + truepeoplesearch_result)
            else:  #Декоднул @allahdec.
                print('TruePeopleSearch: Ничего не найдено')
            if zabasearch_result:  #Декоднул @allahdec.
                print('ZabaSearch: ' + zabasearch_result)
            else:  #Декоднул @allahdec.
                print('ZabaSearch: Ничего не найдено')

            if any([pipl_result, whitepages_result, truepeoplesearch_result, zabasearch_result]):  #Декоднул @allahdec.
                pass  #Декоднул @allahdec.
            else:  #Декоднул @allahdec.
                input('Нажмите Enter, чтобы вернуться...')

        elif choice == '99':  #Декоднул @allahdec.
            print('Выход из программы...')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверный выбор. Пожалуйста, попробуйте снова.')


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
