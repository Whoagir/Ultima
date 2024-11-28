import requests
import xml.etree.ElementTree as ET

data={}

def parse_xml_to_dict(xml_data):
    root = ET.fromstring(xml_data)
    result = {}

    for valute in root.findall('Valute'):
        valute_dict = {}
        for child in valute:
            valute_dict[child.tag] = child.text
        result[valute_dict['CharCode']] = valute_dict

    return result

def update_data(day, month, year):
    global data
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}"
    response = requests.get(url)
    if response.status_code == 200:
        data = parse_xml_to_dict(response.text)
    else:
        print("Ошибка при отправке запроса:", response.status_code)

while (True):
    print("------------------------------------")
    print("Введите день (от 1 до 31):")
    day = input()
    if (int(day) < 10 and day[0] != 0):
        day = "0" + day

    print("Введите месяц (от 1 до 12):")
    month = input()
    if (int(month) < 10 and month[0] != 0):
        month = "0" + month

    print("Введите год (от 1994 до 2024):")
    year = input()

    update_data(day, month, year)
    wallet = "0"
    while (wallet!="-1"):
        print("Введите код валюты (0 для USD или -1 для изменения даты):")
        wallet = input().upper()
        if (wallet == "0"):
            wallet = "USD"
        elif (wallet == "-1"):
            break

        print("------------------------------------")
        print(f"Название: {data[wallet]['Name']}")
        print(f"За {data[wallet]['Nominal']} {data[wallet]['CharCode']}:  {data[wallet]['Value']}₽ ")
        print("------------------------------------")