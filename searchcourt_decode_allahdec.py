#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
from bs4 import BeautifulSoup  #Декоднул @allahdec.
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
░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ 
░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  
       ░    ░ ░           ░              ░  ░   ░     ░ ░     
            ░ ░                                       ░ ░     
"""

main_menu = """ Поиск по судебным делам
╔══════════════════════════════════╗
║[1] - Поиск                       ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""

print(colored(banner, 'magenta'))
print(colored(main_menu, 'magenta'))


def check_case(platform, base_url, query, parse_function):  #Декоднул @allahdec.
    url = base_url.format(query=query)
    headers = {'User-Agent': 'CaseSearchBot'}
    try:  #Декоднул @allahdec.
        response = requests.get(url, headers=headers)
        if response.status_code == 200:  #Декоднул @allahdec.
            if parse_function:  #Декоднул @allahdec.
                parse_function(platform, response.text)
                return  #Декоднул @allahdec.
            else:  #Декоднул @allahdec.
                print(f"Результаты найдены на {platform}: {url}")
                return  #Декоднул @allahdec.
        elif response.status_code == 404:  #Декоднул @allahdec.
            print(f"Информация не найдена на {platform}.")
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print(f"Ошибка {response.status_code} при проверке {platform}.")
            return  #Декоднул @allahdec.
    except Exception as e:  #Декоднул @allahdec.
        print(f"Ошибка подключения к {platform}: {e}")
        e = None
        return  #Декоднул @allahdec.


def parse_kadarbitr(platform, html):  #Декоднул @allahdec.
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='search-result')
    if results:  #Декоднул @allahdec.
        print(f"Результаты на {platform}:")
        for result in results[:6]:  #Декоднул @allahdec.
            case_name = result.find('a', class_='result-title').get_text(strip=True)
            case_details = result.find('div', class_='result-info').get_text(strip=True)
            print(colored(f"Название дела: {case_name}\nДетали: {case_details}\n", 'magenta'))
        return  #Декоднул @allahdec.
    else:  #Декоднул @allahdec.
        print(colored(f"Нет результатов на {platform}.", 'magenta'))
        return  #Декоднул @allahdec.


def search_case(query):  #Декоднул @allahdec.
    platforms = {
        'Арбитражный Суд': ('https://kad.arbitr.ru/Search/index', parse_kadarbitr),
        'Московский Суд': ('https://mos-sud.ru/search', parse_kadarbitr)
    }

    print(f"Ищем информацию по делу: {query}")

    for platform, (base_url, parse_function) in platforms.items():  #Декоднул @allahdec.
        check_case(platform, base_url, query, parse_function)


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ').strip()
        if command == '1':  #Декоднул @allahdec.
            query = input('Введите номер дела или ключевые слова: ').strip()
            search_case(query)
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неизвестная команда. Попробуйте снова.')


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
