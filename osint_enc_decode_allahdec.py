#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import random  #Декоднул @allahdec.
import re  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
from bs4 import BeautifulSoup  #Декоднул @allahdec.
from urllib.parse import quote_plus  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

os.system('cls' if os.name == 'nt' else 'clear')

banner = '\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n       ░    ░ ░           ░              ░  ░   ░     ░ ░     \n            ░ ░                                       ░ ░     \n'
print(colored(banner, 'magenta'))

main = ' Поиск по OSINT\n╔════════════════════════════════╗\n║[1] - Начать поиск              ║\n║[99] - Выход                    ║\n╚════════════════════════════════╝'
print(colored(main, 'magenta'))


def searchbd():  #Декоднул @allahdec.
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    ]

    def get_random_user_agent():  #Декоднул @allahdec.
        return random.choice(USER_AGENTS)  #Декоднул @allahdec.

    def is_valid_value(value):  #Декоднул @allahdec.
        return not re.match(r'^[a-f0-9]{32,}$', value.strip())  #Декоднул @allahdec.

    def extract_emails(text):  #Декоднул @allahdec.
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
        emails = [email for email in emails if 'email protected' not in email.lower()]
        return list(set(emails))  #Декоднул @allahdec.

    def search_info(query):  #Декоднул @allahdec.
        query_encoded = quote_plus(query)
        headers = {'User-Agent': get_random_user_agent()}
        reveng_url = f'https://reveng.ee/search?q={query_encoded}&per_page=100'
        results = []

        try:  #Декоднул @allahdec.
            reveng_response = requests.get(reveng_url, headers=headers)
            if reveng_response.status_code == 200:  #Декоднул @allahdec.
                soup = BeautifulSoup(reveng_response.text, 'html.parser')
                for link in set(  #Декоднул @allahdec.
                        a['href'] for a in soup.find_all('a', href=True) if 'entity' in a['href']):
                    page_response = requests.get(f'https://reveng.ee{link}', headers=headers)
                    if page_response.status_code == 200:  #Декоднул @allahdec.
                        soup = BeautifulSoup(page_response.text, 'html.parser')
                        entity = soup.find('div', class_='bg-body rounded shadow-sm p-3 mb-2 entity-info')

                        if entity:  #Декоднул @allahdec.
                            result = {'База данных': 'Mystery Project | DataBase'}
                            name = entity.find('span', class_='entity-prop-value')
                            if name:  #Декоднул @allahdec.
                                result['Имя'] = name.get_text(strip=True)

                            emails = extract_emails(page_response.text)
                            if emails:  #Декоднул @allahdec.
                                result['E-mail'] = ', '.join(emails)

                            for row in entity.find_all('tr', class_='property-row'):  #Декоднул @allahdec.
                                prop_name = row.find('td', class_='property-name').get_text(strip=True)
                                prop_value = row.find('td', class_='property-values').get_text(strip=True)
                                if not is_valid_value(prop_value):  #Декоднул @allahdec.
                                    continue  #Декоднул @allahdec.
                                result[prop_name] = prop_value

                            results.append(result)
            return results  #Декоднул @allahdec.
        except requests.exceptions.RequestException as e:  #Декоднул @allahdec.
            print('Ошибка при выполнении запроса\nПопробуйте использовать VPN либо попробуйте снова.')
            return results  #Декоднул @allahdec.

    def format_results(results, duration):  #Декоднул @allahdec.
        if not results:  #Декоднул @allahdec.
            return f'Информация не найдена\nПоиск занял: {duration:.2f} секунд'  #Декоднул @allahdec.

        formatted_text = f'Информация найдена\nПоиск занял: {duration:.2f} секунд\n\n'
        for result in results:  #Декоднул @allahdec.
            formatted_text += f'База данных: {result["База данных"]}\n'
            for key, value in result.items():  #Декоднул @allahdec.
                if key != 'База данных':  #Декоднул @allahdec.
                    formatted_text += f'   {key}: {value}\n'
            formatted_text += '\n'
        return formatted_text  #Декоднул @allahdec.

    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')
        if command == '1':  #Декоднул @allahdec.
            query = input('Введите данные для поиска: ')
            if not query.strip():  #Декоднул @allahdec.
                print('Пожалуйста, введите корректные данные.')
                continue  #Декоднул @allahdec.

            print('Поиск... Пожалуйста, подождите.')
            start_time = time.time()
            results = search_info(query)
            duration = time.time() - start_time
            print(format_results(results, duration))
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверная команда. Пожалуйста, попробуйте снова.')


if __name__ == '__main__':  #Декоднул @allahdec.
    searchbd()
