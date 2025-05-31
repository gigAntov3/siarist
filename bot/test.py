import time
import hmac
import hashlib
import json
import requests

api_key = '8e79422fb7bc7f93317f221af98348b5'

data = {
    'shopId': 62587,
    'nonce': int(time.time()),
    'i': 6,
    'email': 'vladss17114@mail.ru',
    'ip': '95.141.32.101',
    'amount': 1000,
    'currency': 'RUB'
}

# Сортировка словаря по ключам и объединение значений через '|'
sorted_items = dict(sorted(data.items()))
sign_string = '|'.join(str(value) for value in sorted_items.values())

# Генерация подписи
signature = hmac.new(
    api_key.encode('utf-8'),
    sign_string.encode('utf-8'),
    hashlib.sha256
).hexdigest()

# Добавление подписи к данным
data['signature'] = signature

# Отправка POST-запроса
response = requests.post(
    'https://api.fk.life/v1/orders/create',
    json=data,
    timeout=10
)

# Обработка ответа
if response.ok:
    result = response.json()
else:
    result = {'error': response.text}

print(result)