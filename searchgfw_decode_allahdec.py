#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
import bs4  #Декоднул @allahdec.
from bs4 import BeautifulSoup  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
import os  #Декоднул @allahdec.

if os.name == 'nt':  #Декоднул @allahdec.
    os.system('cls')
else:  #Декоднул @allahdec.
    os.system('clear')

banner = '\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ \n░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n       ░    ░ ░           ░              ░  ░   ░     ░ ░     \n            ░ ░                                       ░ ░     \n'
print(colored(banner, 'magenta'))

main_menu = ' Поиск по G.F.W\n╔══════════════════════════════════╗\n║[1] - Начать поиск                ║\n║[99] - Выход                      ║\n╚══════════════════════════════════╝'
print(colored(main_menu, 'magenta'))


def search_leaks(email, full_name, phone):  #Декоднул @allahdec.
    search_queries = {
        'email': email + ' утечка данных',
        'full_name': full_name + ' утечка данных',
        'phone': phone + ' утечка данных'
    }

    for key, query in search_queries.items():  #Декоднул @allahdec.
        print('Ищем утечки для: ' + query)
        url = 'https://www.google.com/search?q=' + query
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='BVG0Nb')

        if results:  #Декоднул @allahdec.
            print('Найдены результаты для ' + key + ':')
            for result in results[:5]:  #Декоднул @allahdec.
                title = result.find('h3')
                link = result.find('a')['href']
                if title:  #Декоднул @allahdec.
                    print(title.text + ' - ' + link)
        else:  #Декоднул @allahdec.
            print('Утечек не найдено для ' + key + '.')


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        choice = input('Введите команду: ').strip()

        if choice == '1':  #Декоднул @allahdec.
            phone_number = input('Введите номер телефона: ')
            full_name = input('Введите ФИО (Ф.И.О): ')
            email_address = input('Введите адрес электронной почты: ')
            search_leaks(email_address, full_name, phone_number)
        elif choice == '99':  #Декоднул @allahdec.
            print('Выход из программы...')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверный выбор. Пожалуйста, попробуйте снова.')


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
