#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
from bs4 import BeautifulSoup  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
import os  #Декоднул @allahdec.

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
print(colored(banner, "magenta"))

main_menu = """ Поиск по соц. сетям
╔══════════════════════════════════╗
║[1] - Начать поиск                ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""
print(colored(main_menu, "magenta"))
def check_nickname(nickname):  #Декоднул @allahdec.
    links = {
        'Telegram': 'https://t.me/',
        'TikTok': 'https://www.tiktok.com/',
        'VK': 'https://vk.com/',
        "Roblox Trade": "https://rblx.trade/p/",
        "Internet Archive": "https://archive.org/search?query=",
        "Xbox": "https://www.xboxgamertag.com/search/",
        "WhatsApp": "https://wa.me/{}",
        "Discord": "https://discord.com/users/{}",
        'https://znanija.com/app/profile/': '',
        'GitHub': 'https://github.com/'
    }
    found_links = []
    for platform, base_url in links.items():  #Декоднул @allahdec.
        if "{}" in base_url:  #Декоднул @allahdec.
          url = base_url.format(nickname)
        else:  #Декоднул @allahdec.
          url = base_url + nickname
        try:  #Декоднул @allahdec.
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            if nickname in str(soup):  #Декоднул @allahdec.
                found_links.append(f"{platform}: {url}")
        except requests.exceptions.RequestException as e:  #Декоднул @allahdec.
            print(f"Ошибка при проверке {platform}, или пользователь не найден")
    return found_links  #Декоднул @allahdec.

while True:  #Декоднул @allahdec.
    command = input("Введите команду: ")
    if command == '1':  #Декоднул @allahdec.
        nickname = input("Введите никнейм: ")
        found_links = check_nickname(nickname)
        if found_links:  #Декоднул @allahdec.
            print("Найдено на следующих платформах:")
            for link in found_links:  #Декоднул @allahdec.
                print(link)
        else:  #Декоднул @allahdec.
            print("Никнейм не найден ни на одной из платформ.")
    elif command == '99':  #Декоднул @allahdec.
        print("Выход из программы...")
        os.system("python main.py")
        break  #Декоднул @allahdec.
    else:  #Декоднул @allahdec.
        print("Некорректная команда. Пожалуйста, попробуйте еще раз.")
