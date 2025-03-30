#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
import bs4  #Декоднул @allahdec.
from bs4 import BeautifulSoup  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
import fake_useragent  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
import pyfiglet  #Декоднул @allahdec.
from fake_useragent import UserAgent  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.
import subprocess  #Декоднул @allahdec.
import sys  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import platform  #Декоднул @allahdec.
import webbrowser  #Декоднул @allahdec.
import random  #Декоднул @allahdec.

system = os.system
name = os.name

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

main = """ Бесплатные Proxy
╔══════════════════════════════════╗
║[1] - Лист свободных Proxy        ║
║[2] - Подключиться к Proxy        ║
║[99] - Выход                      ║
╚══════════════════════════════════╝"""

print(colored(banner, "magenta"))
print(colored(main, "magenta"))


def fetch_proxies():  #Декоднул @allahdec.
    url = "https://free.proxy-sale.com/ru/"
    response = requests.get(url)
    if response.status_code == 200:  #Декоднул @allahdec.
        soup = BeautifulSoup(response.text, "html.parser")
        proxies = []
        proxy_table = soup.find("proxy__table", class_="proxy__table")
        if proxy_table:  #Декоднул @allahdec.
            rows = proxy_table.find_all("css-ckmntm", class_="css-ckmntm")
            for row in rows:  #Декоднул @allahdec.
                ip = row.find("css-c524v5", class_="css-c524v5").text
                port = row.find("proxy__table-text", class_="proxy__table-text").text
                anonymity = row.find("proxy__table-anon-type", class_="proxy__table-anon-type").text
                proxies.append((f"{ip}:{port}", anonymity))
            return proxies  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            return proxies  #Декоднул @allahdec.
    else:  #Декоднул @allahdec.
        print(colored("Ошибка при получении прокси", "colored"))
        return []  #Декоднул @allahdec.


def test_proxy(proxy):  #Декоднул @allahdec.
    try:  #Декоднул @allahdec.
        response = requests.get(
            "http://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5
        )
        if response.status_code == 200:  #Декоднул @allahdec.
            print(colored(f"Успешное подключение к прокси: {proxy}", "magenta"))
            return True  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            return False  #Декоднул @allahdec.
    except requests.exceptions.RequestException as e:  #Декоднул @allahdec.
        print(colored(f"Ошибка подключения к прокси {proxy}: {e}", "magenta"))
        return False  #Декоднул @allahdec.


def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        command = input("Введите номер команды: ")

        if command == "1":  #Декоднул @allahdec.
            proxies = fetch_proxies()
            if proxies:  #Декоднул @allahdec.
                print("Список прокси:")
                for idx, (proxy, anonymity) in enumerate(proxies):  #Декоднул @allahdec.
                    print(f"{idx + 1}: {proxy} ({anonymity})")
            else:  #Декоднул @allahdec.
                print("Нет доступных прокси.")

        elif command == "2":  #Декоднул @allahdec.
            proxies = fetch_proxies()
            if proxies:  #Декоднул @allahdec.
                print(colored("Выберите прокси по номеру для подключения:", "magenta"))
                for idx, (proxy, anonymity) in enumerate(proxies):  #Декоднул @allahdec.
                    print(f"{idx + 1}: {proxy} ({anonymity})")

                try:  #Декоднул @allahdec.
                    choice = int(input("Введите номер прокси: ")) - 1
                    if 0 <= choice < len(proxies):  #Декоднул @allahdec.
                        proxy = proxies[choice][0]
                        if test_proxy(proxy):  #Декоднул @allahdec.
                            print(
                                colored(f"Вы успешно подключены к прокси: {proxy}", "magenta")
                            )
                        else:  #Декоднул @allahdec.
                            print(
                                colored(f"Не удалось подключиться к прокси: {proxy}", "magenta")
                            )
                    else:  #Декоднул @allahdec.
                        print("Неверный номер прокси.")
                except ValueError:  #Декоднул @allahdec.
                    print("Пожалуйста, введите корректное число.")

            else:  #Декоднул @allahdec.
                print(colored("Нет доступных прокси.", "magenta"))

        elif command == "99":  #Декоднул @allahdec.
            print("Выход из программы.")
            os.system("python main.py")
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print("Неверная команда. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":  #Декоднул @allahdec.
    main()
