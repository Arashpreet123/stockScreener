import requests
from config import API_KEY

BASE_URL = 'https://financialmodelprep.com/api/v3'

def fetch_stock_ratios(stock_symbols):
    stock_data = {}
    print(stock_symbols)
    for symbol in stock_symbols:
        print('Test')
        response = requests.get(f'https://financialmodelingprep.com/api/v3/ratios/{symbol}?apikey=e89FMui264a50fkSvxTQtpUPusmY3bqy')
        # print(f"Request URL: {response.url}")  # Check the full request URL
        # print(f"Status Code: {response.status_code}")  # Check the status code of the response
        # print((response.status_code))
        if (response.status_code == 200):
            data = response.json()
            print("Entered if block!")
            if data:
                stock_data[symbol] = {
                    'P/E Ratio': data[0].get('priceEarningsRatio', 'N/A'),
                    'EPS': data[0].get('eps', 'N/A'),
                    'ROE': data[0].get('returnOnEquity', 'N/A'),
                    # Add more ratios as needed
                }
            # print(stock_data)
        else:
            print("Didn't enter the if block!")
    return stock_data