#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import os  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
import bs4  #Декоднул @allahdec.
from bs4 import BeautifulSoup  #Декоднул @allahdec.
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
░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ 
░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  
       ░    ░ ░           ░              ░  ░   ░     ░ ░     
            ░ ░                                       ░ ░   
"""

main = """
 Парсинг Сайтов
╔══════════════════════════════════╗
║[1] - Начать парсинг              ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""

print(colored(banner, 'magenta'))
print(colored(main, 'magenta'))


def parse_website(url):  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('h2')
        important_lines = soup.find_all('p')

        with open('parsing/articles.txt', 'w', encoding='utf-8') as f:  #Декоднул @allahdec.
            f.write('Заголовки статей:\n')
            for article in articles:  #Декоднул @allahdec.
                f.write(article.get_text() + '\n')

            f.write('\nВажные строки:\n')
            for line in important_lines:  #Декоднул @allahdec.
                f.write(line.get_text() + '\n')

        print("Парсинг завершён. Результаты сохранены в 'parsing/articles.txt'.")
    except Exception as e:  #Декоднул @allahdec.
        print('Произошла ошибка: ', e)
        return  #Декоднул @allahdec.


def main():  #Декоднул @allahdec.
    if not os.path.exists('parsing'):  #Декоднул @allahdec.
        os.makedirs('parsing')

    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')

        if command == '1':  #Декоднул @allahdec.
            url = input('Введите ссылку сайта: ')
            parse_website(url)
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверная команда. Попробуйте снова.')


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
