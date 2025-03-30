#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
from geopy.geocoders import Nominatim  #Декоднул @allahdec.
from geopy.exc import GeocoderTimedOut, GeocoderServiceError  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.


def get_location_data(latitude, longitude):  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        geolocator = Nominatim(user_agent="GeoServiceApp")
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        if location:  #Декоднул @allahdec.
            return location.address  #Декоднул @allahdec.
        return 'Местоположение не найдено.'  #Декоднул @allahdec.
    except GeocoderTimedOut:  #Декоднул @allahdec.
        return 'Запрос тайм-аут. Пожалуйста, попробуйте позже.'  #Декоднул @allahdec.
    except GeocoderServiceError as e:  #Декоднул @allahdec.
        return 'Ошибка сервиса геокодирования: ' + str(e)  #Декоднул @allahdec.


def get_coordinates_from_address(address):  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        geolocator = Nominatim(user_agent="GeoServiceApp")
        location = geolocator.geocode(address, exactly_one=True)
        if location:  #Декоднул @allahdec.
            return {'latitude': location.latitude, 'longitude': location.longitude, 'address': location.address}  #Декоднул @allahdec.
        return None  #Декоднул @allahdec.
    except GeocoderTimedOut:  #Декоднул @allahdec.
        return 'Запрос тайм-аут. Пожалуйста, попробуйте позже.'  #Декоднул @allahdec.
    except GeocoderServiceError as e:  #Декоднул @allahdec.
        return 'Ошибка сервиса геокодирования: ' + str(e)  #Декоднул @allahdec.


def get_ip_info(ip_address):  #Декоднул @allahdec.
    ipinfo_url = f'http://ip-api.com/json/{ip_address}'
    information = {}
    try:  #Декоднул @allahdec.
        response = requests.get(ipinfo_url)
        response.raise_for_status()
        information = response.json()
        if information.get('status') == 'fail':  #Декоднул @allahdec.
            print('Ошибка: ' + str(information.get('message')))
        return information  #Декоднул @allahdec.
    except requests.RequestException as e:  #Декоднул @allahdec.
        print('Ошибка при запросе к ip-api.com: ' + str(e))
        return information  #Декоднул @allahdec.


def main():  #Декоднул @allahdec.
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = '\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ \n░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n       ░    ░ ░           ░              ░  ░   ░     ░ ░     \n            ░ ░                                       ░ ░     \n'
    print(colored(banner, 'magenta'))
    main = ' GeOsint\n╔══════════════════════════════════╗\n║[1] - Поиск по ш. и д.            ║\n║[2] - Поиск по IP                 ║\n║[3] - Поиск по адресу             ║\n║[99] - Выход                      ║\n╚══════════════════════════════════╝'
    print(colored(main, 'magenta'))

    while True:  #Декоднул @allahdec.
        choice = input('Введите команду: ')
        if choice == '1':  #Декоднул @allahdec.
            coords_input = input('Введите широту и долготу (например, 54.0000, 50.0000): ')
            latitude, longitude = map(float, coords_input.split(','))
            address = get_location_data(latitude, longitude)
            print(colored(f'Адрес: {address}', 'magenta'))
        elif choice == '2':  #Декоднул @allahdec.
            print('Пример: 81.195.141.148')
            ip_address = input('Введите IP-адрес для запроса: ')
            ip_info = get_ip_info(ip_address)
            if ip_info:  #Декоднул @allahdec.
                print('\nИнформация о IP:')
                for key, value in ip_info.items():  #Декоднул @allahdec.
                    print(colored(f'{key}: {value}', 'magenta'))
        elif choice == '3':  #Декоднул @allahdec.
            print('Пример: Москва, ул. Ленина, д. 5')
            address_input = input('Введите адрес для поиска: ')
            print(f"Ищем адрес: '{address_input}'")
            result = get_coordinates_from_address(address_input)
            if result:  #Декоднул @allahdec.
                print(colored(f"Координаты для адреса '{result['address']}':", 'magenta'))
                print(colored(f"Широта: {result['latitude']}, Долгота: {result['longitude']}", 'magenta'))
                location_data = get_location_data(result['latitude'], result['longitude'])
                print(colored(f'Адрес по координатам: {location_data}', 'magenta'))
                ip_info = get_ip_info(location_data)

                if ip_info:  #Декоднул @allahdec.
                    print('\nИнформация о местоположении:')
                    for key, value in ip_info.items():  #Декоднул @allahdec.
                        print(colored(f'{key}: {value}', 'magenta'))
            else:  #Декоднул @allahdec.
                print('Адрес не найден. Попробуйте упростить адрес или изменить его формат.')
        elif choice == '99':  #Декоднул @allahdec.
            print('Выход из программы...')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Некорректный ввод. Пожалуйста, выберите 1, 2, 3 или 99.')


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
