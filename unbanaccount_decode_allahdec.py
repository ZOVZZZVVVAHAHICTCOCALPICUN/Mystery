#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import smtplib  #Декоднул @allahdec.
from email.mime.multipart import MIMEMultipart  #Декоднул @allahdec.
from email.mime.text import MIMEText  #Декоднул @allahdec.
import getpass  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
import os  #Декоднул @allahdec.

os.system('cls' if os.name == 'nt' else 'clear')

banner = '''
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
'''
print(colored(banner, 'magenta'))

main = ''' Разбан аккаунта Telegram
╔══════════════════════════════════╗
║[1] - Разбан аккаунта             ║
║[99] - Выход                      ║
╚══════════════════════════════════╝'''
print(colored(main, 'magenta'))

def send_email(from_email, password, subject, body, smtp_server, port):  #Декоднул @allahdec.
    msg = MIMEMultipart()
    msg['From'] = 'support@telegram.org'
    msg['To'] = 'support@telegram.org'
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:  #Декоднул @allahdec.
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        print(colored('Письмо успешно отправлено в поддержку Telegram!', 'magenta'))
    except Exception as e:  #Декоднул @allahdec.
        print(colored(f'Ошибка при отправке письма: {e}', 'magenta'))

def main():  #Декоднул @allahdec.
    from_email = input('Введите ваш email: ')
    password = getpass.getpass('Введите ваш пароль: ')  #Декоднул @allahdec.
    name = input('Введите ваше имя: ')
    phone_number = input('Введите номер телефона: ')
    email = input('Введите адрес электронной почты от аккаунта (если есть): ')
    account_id = input('Введите ID аккаунта (если есть): ')
    subject = 'Запрос на восстановление заблокированного аккаунта'
    body = f'Здравствуйте, команда поддержки Telegram!\n\nМеня зовут {name}, и я пишу вам, чтобы запросить восстановление моего аккаунта, который был заблокирован. Вот информация о моем аккаунте:\n\n• Номер телефона: {phone_number}\n\n• Адрес электронной почты: {email}\n\n• ID аккаунта (если есть): {account_id}\n\nЯ не нарушал правила использования Telegram и был удивлён блокировкой моего аккаунта. Пожалуйста, рассмотрите мою заявку и дайте мне знать, что нужно сделать для восстановления доступа.\n\nЗаранее благодарю за помощь!\n\nС уважением,\n{name}'

    while True:  #Декоднул @allahdec.
        provider = input('Выберите почтовый сервис (gmail/mail/hotmail): ').lower()
        if provider == 'gmail':  #Декоднул @allahdec.
            smtp_server = 'smtp.gmail.com'
            port = 587
            break  #Декоднул @allahdec.
        elif provider == 'mail':  #Декоднул @allahdec.
            smtp_server = 'smtp.mail.ru'
            port = 587
            break  #Декоднул @allahdec.
        elif provider == 'hotmail':  #Декоднул @allahdec.
            smtp_server = 'smtp.live.com'
            port = 587
            break  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверный выбор почтового сервиса. Пожалуйста, попробуйте снова.')

    send_email(from_email, password, subject, body, smtp_server, port)

if __name__ == '__main__':  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')
        if command == '1':  #Декоднул @allahdec.
            main()
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы.')
            os.system('python main.py')
            break  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print('Неверная команда. Пожалуйста, попробуйте снова.')
