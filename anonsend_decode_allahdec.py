#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import smtplib  #Декоднул @allahdec.
from email.mime.text import MIMEText  #Декоднул @allahdec.
from email.mime.multipart import MIMEMultipart  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

os.system('cls' if os.name == 'nt' else 'clear')

banner = '\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ \n░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n       ░    ░ ░           ░              ░  ░   ░     ░ ░     \n            ░ ░                                       ░ ░     \n'
print(colored(banner, 'magenta'))

main = ' Анонимное письмо на почту\n╔══════════════════════════════════╗\n║[1] - Отправить                   ║\n║[99] - Выход                      ║\n╚══════════════════════════════════╝'
print(colored(main, 'magenta'))


def send_email(sender_email, sender_password, receiver_email, message):  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = 'Mystery Project'
        msg.attach(MIMEText(message, 'plain'))
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f'Письмо успешно отправлено от {sender_email} на {receiver_email}!')
    except Exception as e:  #Декоднул @allahdec.
        print(f'Ошибка при отправке письма от {sender_email} на {receiver_email}')


senders = {
    'anonymous854785@gmail.com': 'wmth dinz jiek nhfy',
    'maksimafanacefish@gmail.com': 'hdpn tbfp acwv jyro',
    'shshsbsbsbwbwvw@gmail.com': 'jqrx qivo qxjy jejt',
    'IvanKarma2000@gmail.com': 'irlr cggo xksq tlbb',
    'misha28272727@gmail.com': 'kgwqxvkgjyccibkm',
    'maksimafanacefish@gmail.com': 'hdpn tbfp acwv jyro',
    'dlatt7055@gmail.com': 'tpzd nxle odaw uqwf',
    'dlyabravla655@gmail.com': 'kprn ihvr bgia vdys',
    'vladimiradmiralov664@gmail.com': 'papq hkip geao rkuz',
    'IvanKarma2000@gmail.com': 'irlr cggo xksq tlbb',
    'misha28272727@gmail.com': 'kgwq xvkg jycc ibkm',
    'edittendo0@gmail.com': 'mzdl lrmx puyq epur',
    'shshsbsbsbwbwvw@gmail.com': 'jqrx qivo qxjy jejt',
    'Ivan27727272hwhs@gmail.com': 'ozcu edfd gmgk rkqg',
    'dlyabravla655@gmail.com': 'kprn ihvr bgia vdys',
    'dlatt6677@gmail.com': 'usun ruef otzx zcrh'
}


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input('Введите команду: ')
        if command == '1':  #Декоднул @allahdec.
            gmail = input('Куда: ')
            receivers = [gmail]
            message = input('Текст: ')
            for sender_email, sender_password in senders.items():  #Декоднул @allahdec.
                for receiver_email in receivers:  #Декоднул @allahdec.
                    send_email(sender_email, sender_password, receiver_email, message)
        elif command == '99':  #Декоднул @allahdec.
            print('Выход из программы...')
            os.system('python main.py')
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print("Некорректный ввод. Пожалуйста, введите '1' для начала или '99' для выхода.")


if __name__ == '__main__':  #Декоднул @allahdec.
    main()
