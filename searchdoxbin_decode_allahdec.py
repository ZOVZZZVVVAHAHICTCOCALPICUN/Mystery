#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
from bs4 import BeautifulSoup  #Декоднул @allahdec.
import sys  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
import os  #Декоднул @allahdec.

os.system('cls' if os.name == 'nt' else 'clear')

banner = '\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n       ░    ░ ░           ░              ░  ░   ░     ░ ░     \n            ░ ░                                       ░ ░     \n'
print(colored(banner, 'magenta'))

main_menu = ' Поиск по Doxbin\n╔════════════════════════════════╗\n║[1] - Начать поиск              ║\n║[99] - Выход                    ║\n╚════════════════════════════════╝'
print(colored(main_menu, 'magenta'))

def check_output_redirected():  #Декоднул @allahdec.
    return not sys.stdout.isatty()  #Декоднул @allahdec.

BASE_URL = 'https://doxbin.org'

def get_csrf_token_and_cookies():  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        session = requests.Session()
        response = session.get(BASE_URL + '/search')
        if response.status_code != 200:  #Декоднул @allahdec.
            return None, None, 'Ошибка подключения к сайту.'  #Декоднул @allahdec.
        soup = BeautifulSoup(response.text, 'html.parser')
        token = soup.find('input', {'name': '_token'})['value']
        return token, session.cookies, None  #Декоднул @allahdec.
    except Exception as e:  #Декоднул @allahdec.
        return None, None, 'Ошибка'  #Декоднул @allahdec.

def search_doxbin(query):  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        token, cookies, error = get_csrf_token_and_cookies()
        if error:  #Декоднул @allahdec.
            return None, error  #Декоднул @allahdec.

        data = {'_token': token, 'search-query': query}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Referer': BASE_URL + '/search'}
        response = requests.post(BASE_URL + '/search', data=data, cookies=cookies, headers=headers)

        if response.status_code != 200:  #Декоднул @allahdec.
            return None, 'Ошибка при выполнении поиска.'  #Декоднул @allahdec.

        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', title=True)
        if not results:  #Декоднул @allahdec.
            return None, 'Ничего не найдено.'  #Декоднул @allahdec.

        links = []
        for res in results:  #Декоднул @allahdec.
            href = res.get('href')
            if not href:  #Декоднул @allahdec.
                continue  #Декоднул @allahdec.
            if not href.startswith('http'):  #Декоднул @allahdec.
                href = BASE_URL + href
            links.append({'title': res.get('title'), 'url': href})

        return links, None  #Декоднул @allahdec.
    except requests.RequestException as e:  #Декоднул @allahdec.
        return None, f'Ошибка сети: {e}'  #Декоднул @allahdec.

def fetch_clean_data(link):  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
        response = requests.get(link['url'], headers=headers)

        if response.status_code != 200:  #Декоднул @allahdec.
            return f'Не удалось загрузить: {link["url"]}'  #Декоднул @allahdec.

        soup = BeautifulSoup(response.text, 'html.parser')
        pasta_content = soup.find('div', class_='show-container')
        if pasta_content:  #Декоднул @allahdec.
            return pasta_content.get_text(separator='\n').strip()  #Декоднул @allahdec.
        return 'Основной текст отсутствует.'  #Декоднул @allahdec.
    except Exception as e:  #Декоднул @allahdec.
        return f'Ошибка при обработке ссылки: {e}'  #Декоднул @allahdec.

if __name__ == '__main__':  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ').strip()

        if command == '99':  #Декоднул @allahdec.
            print('Скрипт завершен.')
            os.system('python main.py')
            break  #Декоднул @allahdec.

        if command != '1':  #Декоднул @allahdec.
            print('Неверная команда. Пожалуйста, попробуйте снова.')
            continue  #Декоднул @allahdec.

        query = input('Введите запрос: ').strip()
        if query.lower() == '99':  #Декоднул @allahdec.
            print('Скрипт завершен.')
            break  #Декоднул @allahdec.

        print('Ищем данные...')
        links, error = search_doxbin(query)

        if error:  #Декоднул @allahdec.
            print(error)
            continue  #Декоднул @allahdec.

        print('\nНайдено результатов:', len(links))
        print('\nРезультаты поиска:')
        for link in links:  #Декоднул @allahdec.
            print('--------------------------------------------------------------------------------')
            print(f'Заголовок: {link["title"]}')
            print(f'Ссылка: {link["url"]}')
            clean_data = fetch_clean_data(link)
            print(f'Основной текст:\n{clean_data}')
