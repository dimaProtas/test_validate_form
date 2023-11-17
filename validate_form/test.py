import requests


url = "http://127.0.0.1:8000/api/get_form/"
url_get_formlist = "http://127.0.0.1:8000/api/formlist/"

data = {
    "email_order": "dima_pro@mail.ru",
    "phone_order": "+79252257315"
}

data2 = {
    "email_my": "dima_pro@mail.ru",
    "phone_my": "+79333214566"
}

data3 = {
    "text_form": "hello form all",
    "email_form": "email_form@maill.ru",
    "phone_form": "+79253453344",
    "date_form": "11.11.2011",
}


headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
}


response = requests.post(url, json=data, headers=headers)
print(response.text)

response2 = requests.post(url, json=data2, headers=headers)
print(response2.text)

response3 = requests.post(url, json=data3, headers=headers)
print(response3.text)

response4 = requests.get(url_get_formlist, headers=headers)
print(response4.text)


