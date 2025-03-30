#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import os  #Декоднул @allahdec.
import sys  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import ctypes  #Декоднул @allahdec.
import socket  #Декоднул @allahdec.
import json  #Декоднул @allahdec.
import base64  #Декоднул @allahdec.
import random  #Декоднул @allahdec.
import webbrowser  #Декоднул @allahdec.
import threading  #Декоднул @allahdec.
import subprocess  #Декоднул @allahdec.
import re  #Декоднул @allahdec.
import datetime  #Декоднул @allahdec.
from datetime import timedelta  #Декоднул @allahdec.
import requests.exceptions  #Декоднул @allahdec.
from requests.exceptions import RequestException  #Декоднул @allahdec.
import requests  #Декоднул @allahdec.
import bs4  #Декоднул @allahdec.
from bs4 import BeautifulSoup  #Декоднул @allahdec.
import phonenumbers  #Декоднул @allahdec.
from phonenumbers import geocoder, carrier, timezone  #Декоднул @allahdec.
import whois  #Декоднул @allahdec.
import colorama  #Декоднул @allahdec.
from colorama import Fore, init  #Декоднул @allahdec.
import pystyle  #Декоднул @allahdec.
from pystyle import Anime, Colors, Colorate, Center  #Декоднул @allahdec.
import termcolor  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

os.system("cls" if os.name == "nt" else "clear")

banner = """
 ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓
▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒
▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░
▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░
▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░
░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ 
░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░         ░     ░░   ░ ▒ ▒ ░░  
       ░    ░ ░           ░              ░  ░   ░     ░ ░     
            ░ ░                                       ░ ░     
"""

main = """ Поиск по Утечкам
╔════════════════════════════════╗
║[1] - Начать поиск              ║
║[99] - Выход                    ║
╚════════════════════════════════╝"""

print(colored(banner, "magenta"))
print(colored(main, "magenta"))

USERSBOX_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkX2F0IjoxNzI1MTk2NzMwLCJhcHBfaWQiOjE3MjUxOTY3MzB9.qG_GQCdZqvUHSHd0yGpnPiUGKo-KRsgNnMo8ZDpRItg"

def search_by_number():  #Декоднул @allahdec.
    phone = input("Введите запрос: ")
    try:  #Декоднул @allahdec.
        response = requests.get(f"https://api.proxynova.com/comb?query={phone[:-11]}&start=0&limit=100", allow_redirects=False)
        response.raise_for_status()
        lines = response.json().get('lines', [])
        for line in lines:  #Декоднул @allahdec.
            print('Result: ' + line)
    except requests.exceptions.RequestException:  #Декоднул @allahdec.
        print('Error fetching data from ProxyNova.')
    try:  #Декоднул @allahdec.
        response = requests.get(
            "https://api.usersbox.ru/v1/explain",
            headers={"Authorization": f"Bearer {USERSBOX_API_KEY}"},
            params={"q": phone}
        )
        response.raise_for_status()
        items = response.json().get('data', {}).get('items', [])
        for item in items:  #Декоднул @allahdec.
            database = item['source']['database']
            collection = item['source']['collection']
            hits_count = item['hits']['count']
            print(f'Утечки Mystery Projeck: {database}, Collection: {collection}, Found: {hits_count}')
    except requests.exceptions.RequestException:  #Декоднул @allahdec.
        print("Error")
    def search_vk_by_phone(phone):  #Декоднул @allahdec.
        response = requests.get(f"https://find.vk.com/phone/{phone}")
        if response.status_code == 200:  #Декоднул @allahdec.
            print("VK found!")
            return response  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print("VK not found")
            return None  #Декоднул @allahdec.
    result = search_vk_by_phone(phone)
    if result is None:  #Декоднул @allahdec.
        print("User with this phone number not found in VK.")
    url = f"https://www.avito.ru/rossiya/telefony?q={phone}"
    response = requests.head(url)
    if response.status_code == 200:  #Декоднул @allahdec.
        print("Avito found")
    else:  #Декоднул @allahdec.
        print("Avito not found")
    def google_search_phone(phone):  #Декоднул @allahdec.
        query = f"https://www.google.com/search?q={phone}"
        response = requests.get(query)
        if response.status_code == 200:  #Декоднул @allahdec.
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('a')
            links = []
            for result in search_results:  #Декоднул @allahdec.
                href = result.get('href')
                if href and href.startswith('/url?q='):  #Декоднул @allahdec.
                    link = href.replace('/url?q=', '').split('&')[0]
                    links.append(link)
            if len(links) > 0:  #Декоднул @allahdec.
                print("Links found:")
                for link in links:  #Декоднул @allahdec.
                    print(link)
                return None  #Декоднул @allahdec.
            else:  #Декоднул @allahdec.
                print("Links not found")
                return None  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print("Error during request")
            return None  #Декоднул @allahdec.
    google_search_phone(phone)

def main():  #Декоднул @allahdec.
    while True:  #Декоднул @allahdec.
        choice = input("Введите команду: ")
        if choice == "1":  #Декоднул @allahdec.
            search_by_number()
        elif choice == "99":  #Декоднул @allahdec.
            print("Завершение программы.")
            os.system("python main.py")
            return  #Декоднул @allahdec.
        else:  #Декоднул @allahdec.
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == '__main__':  #Декоднул @allahdec.
    main()
