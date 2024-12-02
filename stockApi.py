import requests

api_key = 'e89FMui264a50fkSvxTQtpUPusmY3bqy'

base_url = 'https://financialmodelingprep.com/api/v3/'

def get_stock_price(symbol):
    endpoint = f'stock/real-time-price/{symbol}'
    url = f'{base_url}{endpoint}?apikey={api_key}'
    print(url)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

stock_data = get_stock_price('AAPL')

# Below gets all the stocks
# response = requests.get(f'https://financialmodelingprep.com/api/v3/stock/list?apikey={api_key}')
# Particualar stock information
# response = requests.get(f'https://financialmodelingprep.com/api/v3/profile/AAPL?apikey={api_key}')
appleStock = requests.get(f'https://financialmodelingprep.com/api/v3/ratios/AAPL?apikey={api_key}')
nvidiaStock = requests.get(f'https://financialmodelingprep.com/api/v3/ratios/NVDA?apikey={api_key}')
# https://financialmodelingprep.com/api/v3/ratios/NVDA?apikey=e89FMui264a50fkSvxTQtpUPusmY3bqy
applePeRatio = appleStock.json()[0].get('priceEarningsRatio')
nvidiaPeRatio = nvidiaStock.json()[0].get('priceEarningsRatio')

array = [applePeRatio, nvidiaPeRatio]

print(array)

print(stock_data)