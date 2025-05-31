import time
import hmac
import hashlib
import requests

API_KEY = "8e79422fb7bc7f93317f221af98348b5"
SHOP_ID = 62587

email = 'vladss17114@mail.ru'
ip = '95.141.32.101'
amount = 1000
currency = 'RUB'


data = {
    "shopId": SHOP_ID,
    "nonce": int(time.time()),
    "i": 6,
    "email": email,
    "ip": ip,
    "amount": amount,
    "currency": currency,
}


# Сортировка и формирование строки для подписи
sorted_items = dict(sorted(data.items()))
sign_string = '|'.join(str(value) for value in sorted_items.values())

# Создание подписи HMAC-SHA256
signature = hmac.new(
    API_KEY.encode("utf-8"),
    sign_string.encode("utf-8"),
    hashlib.sha256
).hexdigest()

data["signature"] = signature

response = requests.post(
    'https://api.fk.life/v1/orders/create',
    json=data,
    timeout=10
)

if response.ok:
    result = response.json()
else:
    result = {'error': response.text}

print(result)