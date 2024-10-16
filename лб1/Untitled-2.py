import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def get_exchange_rate(date):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&json"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Помилка запиту: {response.status_code}")
        return None

def get_weekly_exchange_rates(currency_code):
    today = datetime.today()
    rates = []
    dates = []
    
    for i in range(1, 8):
        day = today - timedelta(days=i)
        formatted_date = day.strftime('%Y%m%d')
        result = get_exchange_rate(formatted_date)
        
        if result:
            for rate in result:
                if rate['cc'] == currency_code:
                    rates.append(rate['rate'])
                    dates.append(day.strftime('%Y-%m-%d'))
                    break

    return dates, rates

def plot_currency_rates(currency_code):
    dates, rates = get_weekly_exchange_rates(currency_code)
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, rates, marker='o', linestyle='-', color='b')
    plt.title(f'Зміна курсу {currency_code} за останній тиждень')
    plt.xlabel('Дата')
    plt.ylabel('Курс (UAH)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_currency_rates('USD')