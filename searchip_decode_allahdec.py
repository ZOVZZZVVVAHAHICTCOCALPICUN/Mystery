#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
from platform import system  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.


def clear_console():  #Декоднул @allahdec.
    if system() != 'Windows':  #Декоднул @allahdec.
        os.system('clear')
    else:  #Декоднул @allahdec.
        os.system('cls')


funk = ' Поиск по IP\n╔══════════════════════════════════╗\n║[1] - Поиск по IP                 ║\n║[99] - Выход                      ║\n╚══════════════════════════════════╝'


def display_logo():  #Декоднул @allahdec.
    logo = '\n    ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n    ▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n    ▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n    ▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n    ▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n    ░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n    ░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n           ░    ░ ░           ░              ░  ░   ░     ░ ░     \n                ░ ░                                       ░ ░     '
    print(colored(logo, 'magenta'))
    print(colored(funk, 'magenta'))


def get_ip_info(ip):  #Декоднул @allahdec.
    api = f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es'
    data = requests.get(api).json()
    if data['status'] == 'fail':  #Декоднул @allahdec.
        print('Ошибка:', data['message'])
        return  #Декоднул @allahdec.

    print('\n [IP]:', data['query'])
    print('ISP:', data['isp'] if data['isp'] else 'ISP не найден')
    print('Организация:', data['org'] if data['org'] else 'Организация не найдена')
    print('Город:', data['city'] if data['city'] else 'Город не найден')
    print('Страна:', data['country'] if data['country'] else 'Страна не найдена')
    print('Регион:', data['region'] if data['region'] else 'Регион не найден')
    print('Континент:', data['continent'] if data['continent'] else 'Континент не найден')
    print('Название региона:', data['regionName'] if data['regionName'] else 'Название региона не найдено')
    print('Код Континента:', data['continentCode'] if data['continentCode'] else 'Код континента не найден')
    print('Широта:', data['lat'] if data['lat'] else 'Широта не найдена')
    print('Долгота:', data['lon'] if data['lon'] else 'Долгота не найдена')
    print('Тайм Зона:', data['timezone'] if data['timezone'] else 'Тайм зона не найдена')
    print('Индекс:', data['zip'] if data['zip'] else 'Индекс не найден')
    print('Оператор номера:', data['as'] if data['as'] else 'Оператор номера не найден')
    print('Код Страны:', data['countryCode'] if data['countryCode'] else 'Код Страны не найден')
    print('DNS: ', data['reverse'] if data['reverse'] else 'DNS не найден')
    print('Mobile:', data['mobile'] if data['mobile'] else 'Mobile не найден')
    print('Код Валюты:', data['currency'] if data['currency'] else 'Код Валюты не найден')
    print('[~] [Distrito (subdivisión de la ciudad)]:', data['district'] if data['district'] else '[~] [Distrito не найден!]')
    print('VPN/Proxy:', data['proxy'] if data['proxy'] else 'VPN/Proxy не найдены')


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        clear_console()
        display_logo()
        command = input('Введите команду: ')
        if command == '1':  #Декоднул @allahdec.
            ip = input('Введите IP: ')
            print('Информация по IP - ', ip)
            time.sleep(2)
            get_ip_info(ip)
            input('\nНажмите Enter для продолжения...')
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверная команда. Попробуйте снова.')


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
