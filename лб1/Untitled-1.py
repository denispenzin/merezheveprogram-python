import requests
from datetime import datetime, timedelta

def get_exchange_rate(date):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&json"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Помилка запиту: {response.status_code}")
        return None

def get_weekly_exchange_rates():
    today = datetime.today()
    for i in range(1, 8): 
        day = today - timedelta(days=i)
        formatted_date = day.strftime('%Y%m%d') 
        print(f"Курси валют на {formatted_date}:")
        rates = get_exchange_rate(formatted_date)
        if rates:
            for rate in rates:
                print(f"{rate['cc']} - {rate['rate']}")
        print("-" * 40)

get_weekly_exchange_rates()
