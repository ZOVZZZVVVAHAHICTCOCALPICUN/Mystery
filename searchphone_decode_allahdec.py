#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import fake_useragent  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
import pyfiglet  #Декоднул @allahdec.
from fake_useragent import UserAgent  #Декоднул @allahdec.
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
print(colored(banner, 'magenta'))


class HttpWebNumber:  #Декоднул @allahdec.

    def __init__(self):  #Декоднул @allahdec.
        self.__check_number_link = 'https://htmlweb.ru/geo/api.php?json&telcod='
        self.__not_found_text = 'Информация отсутствует'

    def __return_number_data(self, user_number: str) -> dict:  #Декоднул @allahdec.
        try:  #Декоднул @allahdec.
            response = requests.get(self.__check_number_link + user_number, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15'})
            if response.ok:  #Декоднул @allahdec.
                return response.json()  #Декоднул @allahdec.
            else:  #Декоднул @allahdec.
                return {'status_error': True}  #Декоднул @allahdec.
        except requests.exceptions.ConnectionError:  #Декоднул @allahdec.
            return {'status_error': True}  #Декоднул @allahdec.

    def print_number_results(self):  #Декоднул @allahdec.
        try:  #Декоднул @allahdec.
            user_number = input('Введите номер телефона\n └ [Пример: +79999993993]: ').strip()

            if user_number:  #Декоднул @allahdec.
                print('Поиск данных...\n')
                number_data = self.__return_number_data(user_number=user_number)

                if number_data.get('limit', 1) <= 0:  #Декоднул @allahdec.
                    print('К сожалению, вы израсходовали все лимиты...\n └ Обратитесь к @MysteryKilled')
                    print('Всего лимитов: ' + str(number_data.get('limit', self.__not_found_text)))
                    return None  #Декоднул @allahdec.

                if number_data.get('status_error') or number_data.get('error'):  #Декоднул @allahdec.
                    print('Данные не найдены...\n')
                    return None  #Декоднул @allahdec.

                country = number_data.get('country', {})
                capital = number_data.get('capital', {})
                region = number_data.get('region', {'autocod': self.__not_found_text, 'name': self.__not_found_text, 'okrug': self.__not_found_text})
                other = number_data.get('0', {})

                if country.get('country_code3') == 'UKR':  #Декоднул @allahdec.
                    print(' ├ Страна: Украина')
                else:  #Декоднул @allahdec.
                    print('Данные\n ├ Страна: ' + str(country.get('name', self.__not_found_text)) + ', ' + str(country.get('fullname', self.__not_found_text)))
                print(' ├ Город: ' + str(other.get('name', self.__not_found_text)))
                print(' ├ Почтовый индекс: ' + str(other.get('post', self.__not_found_text)))
                print(' ├ Код валюты: ' + str(country.get('iso', self.__not_found_text)))
                print(' ├ Телефонные коды: ' + str(capital.get('telcod', self.__not_found_text)))
                print(' ├ Гос. номер региона авто: ' + str(region.get('autocod', self.__not_found_text)))
                print(' ├ Оператор: ' + str(other.get('oper', self.__not_found_text)) + ', ' + str(other.get('oper_brand', self.__not_found_text)) + ', ' + str(other.get('def', self.__not_found_text)))
                print(' ├ Местоположение: ' + str(country.get('name', self.__not_found_text)) + ', ' + str(region.get('name', self.__not_found_text)) + ', ' + str(other.get('name', self.__not_found_text)))
                print(' ├ Локация: ' + str(number_data.get('location', self.__not_found_text)))
                print(' ├ Язык общения: ' + str(country.get('lang', self.__not_found_text)).title() + ', ' + str(country.get('langcod', self.__not_found_text)))
                print(' ├ Край/Округ/Область: ' + str(region.get('name', self.__not_found_text)) + ', ' + str(region.get('okrug', self.__not_found_text)))
                print(' ├ Столица: ' + str(capital.get('name', self.__not_found_text)))
                print(' └ Широта/Долгота: ' + str(other.get('latitude', self.__not_found_text)) + ', ' + str(other.get('longitude', self.__not_found_text)))

                print('Проверьте эти ссылки:')
                print(' ├ https://www.instagram.com/accounts/password/reset - Поиск аккаунта в Instagram')
                print(' ├ https://api.whatsapp.com/send?phone=' + user_number + '&text=Привет - Поиск номера в WhatsApp')
                print(' ├ https://facebook.com/login/identify - Поиск аккаунта FaceBook')
                print(' ├ https://www.linkedin.com/checkpoint/rp/request-password-reset - Поиск аккаунта Linkedin')
                print(' ├ https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink - Поиск аккаунта OK')
                print(' ├ https://twitter.com/account/begin_password_reset - Поиск аккаунта Twitter')
                print(' ├ https://viber://add?number=' + user_number + ' - Поиск номера в Viber')
                print(' ├ https://skype:' + user_number + '?call - Звонок на номер с Skype')
                print(' ├ https://t.me/' + user_number + ' - Открыть аккаунт в Телеграмме')
                print(' └ tel:' + user_number + ' - Звонок на номер с телефона')
                print('Всего лимитов: ' + str(number_data.get('limit', self.__not_found_text)))
                input('Чтобы завершить поиск\n └ Нажмите ENTER ')
                os.system('python main.py')
                return None  #Декоднул @allahdec.
            else:  #Декоднул @allahdec.
                print('Ошибка\n └ Введите номер телефона!\n')
                return None  #Декоднул @allahdec.
        except KeyboardInterrupt:  #Декоднул @allahdec.
            print('\nВынужденная остановка работы\n')
            return None  #Декоднул @allahdec.


if __name__ == '__main__':  #Декоднул @allahdec.
    checker = HttpWebNumber()
    checker.print_number_results()
