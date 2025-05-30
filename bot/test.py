import requests

url = "https://api.fk.life/v1/orders/create"

json = {
    "shop_id": 1,
    "nonce": 1,
    # signature
    "paymentId": 1,
    "i": 1,
    "email": "vladss17114@mail.ru",
    "ip": "82.179.51.83",
    "amount": 100.23,
    "currency": "RUB"
}

response = requests.post(url)

print(response.json())