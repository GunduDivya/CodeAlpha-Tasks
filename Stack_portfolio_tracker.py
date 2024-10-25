import json.decoder

import requests
API_KEY='RYCC67TRA5FCGOIO'
BASE_URL='https://www.alphavantage.co/query'
portfolio={}

def add_investment(symbol,shares):
    if symbol in portfolio:
        portfolio[symbol] +=shares
    else:
        portfolio[symbol]=shares
    print(f"Added {shares} shares of {symbol}")
def remove_investment(symbol,shares):
    if symbol in portfolio:
        if portfolio[symbol]>=shares:
            portfolio[symbol]-=shares
            if portfolio[symbol]==0:
                del portfolio[symbol]
            print(f'removed {shares} shares of {symbol}')
        else:
            print(f"Not enough shares to remove")
    else:
        print(f"{symbol} not found in portfolio.")
def get_stock_price(symbol):
    response=requests.get(BASE_URL,params={
        'function':'TIME_SERIES_INTRADAY',
        'symbol':symbol,
        'interval':'1min',
        'apikey':API_KEY
    })
    print("Reponse status code:",response.status_code)
    print("Response URL:",response.url)
    print("Response Text:",response.text)

    if response.status_code==200:
        try:
            data = response.json()
            latest_time=next(iter(data['Time Series (1min)']))
            price=data['Time Series (1min)'][latest_time]['1. open']
            return float(price)
        except KeyError:
            print(f'Error fetching data for {symbol}. please check the symbol or api response.')
            return None
        except json.decoder.JSONDecodeError:
            print("Received non-json response.")
            return None
def track_performance():
    total_value=0
    for symbol,shares in portfolio.items():
        price=get_stock_price(symbol)
        if price is not None:
            value = price* shares
            total_value +=value
            print(f'{shares} shares of {symbol} at ${price:.2f} each: ${value:.2f}')
    print(f'Total portfolio value: ${total_value:.2f}')
while True:
    action=input("Would you like to (add/remove) shares or (exit)?").strip().lower()
    if action== 'add':
        symbol=input("enter inverstor symbol here:")
        shares=int(input("enter investor shares here:"))
        add_investment(symbol,shares)
    elif action=='remove':
        symbol=input("enter investor symbol here:")
        shares=int(input("enter investor shares here:"))
        remove_investment(symbol,shares)
    elif action=='exit':
        break
    else:
        print("invalid action.please choose 'add','remove','exit' .")
track_performance()
