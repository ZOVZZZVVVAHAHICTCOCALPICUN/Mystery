#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import os  #Декоднул @allahdec.
import colorama  #Декоднул @allahdec.
from colorama import init, Fore  #Декоднул @allahdec.
import shutil  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
import fake_useragent  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
import pyfiglet  #Декоднул @allahdec.
from fake_useragent import UserAgent  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

if os.name == 'nt':  #Декоднул @allahdec.
    os.system('cls')
else:  #Декоднул @allahdec.
    os.system('clear')

banner = '\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ \n░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n       ░    ░ ░           ░              ░  ░   ░     ░ ░     \n            ░ ░                                       ░ ░     \n'
print(colored(banner, 'magenta'))

main = ' Поиск по LeakOsint\n╔══════════════════════════════════╗\n║[1] - Начать поиск                ║\n║[99] - Выход                      ║\n╚══════════════════════════════════╝'
print(colored(main, 'magenta'))

def load_token_from_file(file_path):  #Декоднул @allahdec.
    with open(file_path, 'r') as file:  #Декоднул @allahdec.
        token = file.readline().strip()
    return token  #Декоднул @allahdec.

TOKEN = load_token_from_file('key.txt')

def center_text(text):  #Декоднул @allahdec.
    columns, _ = shutil.get_terminal_size()
    lines = text.splitlines()
    centered_lines = [line.center(columns) for line in lines]
    line = '\n'
    return line.join(centered_lines)  #Декоднул @allahdec.

def send_osint_request(query, limit=100, lang='en', report_type='json'):  #Декоднул @allahdec.
    url = 'https://leakosintapi.com/'
    data = {
        'token': TOKEN,
        'request': query,
        'limit': limit,
        'lang': lang,
        'type': report_type
    }
    response = requests.post(url, json=data)
    return response.json()  #Декоднул @allahdec.

init(autoreset=True)

def format_results(results):  #Декоднул @allahdec.
    list_data = results.get('List')
    if list_data:  #Декоднул @allahdec.
        for source, source_data in list_data.items():  #Декоднул @allahdec.
            print(Fore.MAGENTA + 'Источник данных: ' + source)
            for entry in source_data.get('Data', []):  #Декоднул @allahdec.
                if isinstance(entry, dict):  #Декоднул @allahdec.
                    if entry.get('FullName'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Полное Имя: ' + str(entry['FullName']))
                    if entry.get('Country'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Страна: ' + str(entry['Country']))
                    if entry.get('City'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Город: ' + str(entry['City']))
                    if entry.get('Region'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Регион: ' + str(entry['Region']))
                    if entry.get('Gender'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Пол: ' + str(entry['Gender']))
                    if entry.get('VkID'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ VkID: ' + str(entry['VkID']))
                    if entry.get('Email'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Почта: ' + str(entry['Email']))
                    if entry.get('LastName'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Фамилия: ' + str(entry['LastName']))
                    if entry.get('FirstName'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Имя: ' + str(entry['FirstName']))
                    if entry.get('MiddleName'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Отчество: ' + str(entry['MiddleName']))
                    if entry.get('Phone'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Телефон: ' + str(entry['Phone']))
                    if entry.get('Data'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Дата: ' + str(entry['Data']))
                    if entry.get('INN'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ ИНН: ' + str(entry['INN']))
                    if entry.get('Snils'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Снилс: ' + str(entry['Snils']))
                    if entry.get('BDay'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Дата рождения: ' + str(entry['BDay']))
                    if entry.get('Description'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Описание: ' + str(entry['Description']))
                    if entry.get('Address'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Адрес: ' + str(entry['Address']))
                    if entry.get('Street'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Улица: ' + str(entry['Street']))
                    if entry.get('HouseNumber'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Номер дома: ' + str(entry['HouseNumber']))
                    if entry.get('PostCode'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Почтовый индекс: ' + str(entry['PostCode']))
                    if entry.get('Location'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Место проживания: ' + str(entry['Location']))
                    if entry.get('Passport'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Паспорт: ' + str(entry['Passport']))
                    if entry.get('PassportIssuedBy'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Выдан: ' + str(entry['PassportIssuedBy']))
                    if entry.get('IssuedAt'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Дата выдачи: ' + str(entry['IssuedAt']))
                    if entry.get('Department'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Отдел: ' + str(entry['Department']))
                    if entry.get('LastActive'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Последняя активность: ' + str(entry['LastActive']))
                    if entry.get('Password(bcrypt)'):  #Декоднул @allahdec.
                        print(Fore.MAGENTA + '├ Пароль (bcrypt): ' + str(entry.get('Password(bcrypt)', 'Нету Информации')))
                    if entry.get('TelegramID'):  #Декоднул @allahdec.
                        print(Fore.MAGENTA + '├ Telegram ID: ' + str(entry['TelegramID']))
                    if entry.get('NickName'):  #Декоднул @allahdec.
                        print(Fore.MAGENTA + '├ Никнейм: ' + str(entry['NickName']))
                    if entry.get('CityCode'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Код города: ' + str(entry['CityCode']))
                    if entry.get('EngStreet2'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Адрес улицы на английском: ' + str(entry['EngStreet2']))
                    if entry.get('RusStreet2'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Адрес улицы на русском: ' + str(entry['RusStreet2']))
                    if entry.get('House2'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Номер второго дома: ' + str(entry['House2']))
                    if entry.get('Type(fiz\\ur)'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Тип (физ/юр): ' + str(entry['Type(fiz\\ur)']))
                    if entry.get('Url'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ ВК: ' + str(entry['Url']))
                    if entry.get('PointAddress'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Адрес точки выдачи: ' + str(entry['PointAddress']))
                    if entry.get('Latitude'):  #Декоднул @allahdec.
                        print(Fore.MAGENTA + '├ Широта: ' + str(entry['Latitude']))
                    if entry.get('Longitude'):  #Декоднул @allahdec.
                        print(Fore.MAGENTA + '├ Долгота: ' + str(entry['Longitude']))
                    if entry.get('IP'):  #Декоднул @allahdec.
                        print(Fore.MAGENTA + '├ IP: ' + str(entry['IP']))
                    if entry.get('AutoNumber'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Номер машины: ' + str(entry['AutoNumber']))
                    if entry.get('DriverLicense'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Вод. права: ' + str(entry['DriverLicense']))
                    if entry.get('Phone2'):  #Декоднул @allahdec.
                        print(Fore.MAGENTA + '├ Телефон: ' + str(entry['Phone2']))
                    if entry.get('Phone3'):  #Декоднул @allahdec.
                        print(Fore.MAGENTA + '├ Телефон: ' + str(entry['Phone3']))
                    if entry.get('Phone4'):  #Декоднул @allahdec.
                        print(Fore.MAGENTA + '├ Телефон: ' + str(entry['Phone4']))
                    if entry.get('CreditCard'):  #Декоднул @allahdec.
                        print(Fore.MAGENTA + '├ Кредитная карта: ' + str(entry['CreditCard']))
                    if entry.get('SenderName'):  #Декоднул @allahdec.
                        print(Fore.MAGENTA + '├ Имя отправителя: ' + str(entry['SenderName']))
                    if entry.get('ReceiverName'):  #Декоднул @allahdec.
                        print(Fore.MAGENTA + '├ Имя получателя: ' + str(entry['ReceiverName']))
                    if entry.get('Date'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Дата отправления: ' + str(entry['Date']))
                    if entry.get('TimeZone'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Часовой пояс: ' + str(entry['TimeZone']))
                    if entry.get('DeliveryCity'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Город доставки: ' + str(entry['DeliveryCity']))
                    if entry.get('PostCode'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Почтовый индекс доставки: ' + str(entry['PostCode']))
                    if entry.get('Status'):  #Декоднул @allahdec.
                        print(Fore.WHITE + '├ Статус доставки: ' + str(entry['Status']))
            print(Fore.MAGENTA + 'Источник: ' + source)
            print(Fore.MAGENTA + '--------------------------------------------------')
        free_requests_left = results.get('free_requests_left')
        if free_requests_left:  #Декоднул @allahdec.
            print(Fore.RED + 'Осталось запросов: ' + str(free_requests_left))
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            return  #Декоднул @allahdec.
    else:  #Декоднул @allahdec.
        print(Fore.RED + 'Ошибка, проверьте API-Ключ!')
        return  #Декоднул @allahdec.

def main_menu():  #Декоднул @allahdec.
    choice = input('Выберите опцию: ')
    return choice  #Декоднул @allahdec.

def start_osint():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        choice = main_menu()
        if choice == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        if choice == '1':  #Декоднул @allahdec.
            query = input('Введите запрос: ')
            results = send_osint_request(query)
            format_results(results)

if __name__ == '__main__':  #Декоднул @allahdec.
    start_osint()
