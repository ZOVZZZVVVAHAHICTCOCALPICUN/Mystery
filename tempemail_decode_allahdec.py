#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
import bs4  #Декоднул @allahdec.
from bs4 import BeautifulSoup  #Декоднул @allahdec.
import datetime  #Декоднул @allahdec.
from datetime import timedelta  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import pystyle  #Декоднул @allahdec.
from pystyle import Colors  #Декоднул @allahdec.
from pystyle import Box  #Декоднул @allahdec.
from pystyle import Write  #Декоднул @allahdec.
from pystyle import Center  #Декоднул @allahdec.
from pystyle import Colorate  #Декоднул @allahdec.
from pystyle import Anime  #Декоднул @allahdec.

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

main = """ Временная Почта
╔══════════════════════════════════╗
║[1] - Сгенерировать почту         ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""
print(colored(main, 'magenta'))


def temp_mail():  #Декоднул @allahdec.
    def create_temp_mail():  #Декоднул @allahdec.
        local_part = input('\nПридумайте название: ')
        if local_part == '0':  #Декоднул @allahdec.
            return None  #Декоднул @allahdec.
        domain = 'rteet.com'
        email = f'{local_part}@{domain}'
        return email  #Декоднул @allahdec.

    def get_mailbox_messages(login, domain):  #Декоднул @allahdec.
        response = requests.get(
            f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')
        if response.status_code == 200:  #Декоднул @allahdec.
            return response.json()  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Не удалось получить сообщения.')
            return []  #Декоднул @allahdec.

    def get_message_details(login, domain, message_id):  #Декоднул @allahdec.
        response = requests.get(
            f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={message_id}')
        if response.status_code == 200:  #Декоднул @allahdec.
            return response.json()  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Не удалось получить сведения о сообщении.')
            return None  #Декоднул @allahdec.

    def extract_text_from_html(html_content):  #Декоднул @allahdec.
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text()  #Декоднул @allahdec.

    def save_message_to_file(filename, sender, date, subject, body):  #Декоднул @allahdec.
        with open(filename, 'a', encoding='utf-8') as file:  #Декоднул @allahdec.
            file.write(f'От: {sender}\n')
            file.write(f'Дата: {date}\n')
            file.write(f'Субъект: {subject}\n')
            file.write(f'Сообщение: {body}\n\n')

    def adjust_time(date_str):  #Декоднул @allahdec.
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        adjusted_time = date_obj + timedelta(hours=3)
        return adjusted_time.strftime('%Y-%m-%d %H:%M:%S')  #Декоднул @allahdec.

    email = create_temp_mail()
    if email:  #Декоднул @allahdec.
        print(colored(f'Временная почта: {email}', 'magenta'))
        login, domain = email.split('@')
        processed_messages = set()
        print('Ожидаются новые сообщения...')
        while True:  #Декоднул @allahdec.
            try:  #Декоднул @allahdec.
                messages = get_mailbox_messages(login, domain)
                if messages:  #Декоднул @allahdec.
                    for message in messages:  #Декоднул @allahdec.
                        if message['id'] not in processed_messages:  #Декоднул @allahdec.
                            message_details = get_message_details(login, domain, message['id'])
                            if message_details:  #Декоднул @allahdec.
                                sender = message_details['from']
                                date = adjust_time(message_details['date'])
                                subject = message_details['subject']
                                message_body = extract_text_from_html(message_details['body'])
                                save_message_to_file('emails.txt', sender, date, subject, message_body)
                                print()
                                print(colored(f'Сообщение получено: \n ├ От: {sender}', 'magenta'))
                                print(colored(f' ├ Дата: {date}', 'magenta'))
                                print(colored(f' ├ Субъект: {subject}', 'magenta'))
                                print(colored(f' └ Сообщение: {message_body}\n', 'magenta'))
                                processed_messages.add(message['id'])
                time.sleep(5)
            except KeyboardInterrupt:  #Декоднул @allahdec.
                print('\nВыход из программы.')
                return  #Декоднул @allahdec.
    else:  #Декоднул @allahdec.
        return  #Декоднул @allahdec.


if __name__ == '__main__':  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')
        if command == '1':  #Декоднул @allahdec.
            temp_mail()
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            exit()
        else:  #Декоднул @allahdec.
            print("Неверная команда. Пожалуйста, введите '1' или '99'.")
