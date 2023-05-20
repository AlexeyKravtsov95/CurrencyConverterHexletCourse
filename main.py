import onlinerequests

CURRENCIES = onlinerequests.response.json()['data']

print("Добро пожаловать в конвертер валют!")
print("""
Наша программа поможет Вам конвертировать валюту.
- Введение имеющийся валюты
- Количество этой валюты
- Выбор валюты для конвертации
""")

print("Вам предложены следующие валюты:")
key_counter = 0
for key, value in CURRENCIES.items():
    key_counter += 1
    print(f'{key_counter}. {key}')


def input_currency():
    while True:
        user_currency = input("Введите имеющийся валюту: ")
        if user_currency in CURRENCIES.keys():
            print("Валюта есть")
            break
        else:
            print("Валюты нет")
    return user_currency

user_currency = input_currency()

def input_current_amount():
    while True:
        current_amount = float(input("Введите имеющуюся сумму: "))
        if current_amount > 0:
            print("Отлично, идем дальше")
            break
        else:
            print("Сумма меньше нуля")
    return current_amount

current_amount = input_current_amount()

def choose_conversion_currency():
    while True:
        conversion_currency = input("Выберите валюту для конвертации: ")
        if conversion_currency in CURRENCIES.keys():
            print("Валюта есть")
            break
        else:
            print("Валюты нет")
    return conversion_currency

conversion_currency = choose_conversion_currency()

def calculated_amount(current_amount, user_currency, conversion_currency):
    converted_amount = current_amount / CURRENCIES.get(user_currency) * CURRENCIES.get(conversion_currency)
    print(f"Итого: {round(converted_amount, 2)} {conversion_currency}")

calculated_amount(current_amount, user_currency, conversion_currency)
