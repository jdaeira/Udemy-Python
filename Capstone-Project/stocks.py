
from yahoo_fin.stock_info import *

symbols = input("Enter stock symbols seperated by a space: ")
stocks = symbols.split()

for stock in stocks:
    print(stock.upper())
    price = float(get_live_price(stock.upper()))
    print(round(price, 2))

apple = get_live_price('AAPL')
print(apple)
print(get_quote_table("AAPL"))
print(get_quote_table('AAPL')['Open'])

print(get_day_gainers())

# get list of Dow stocks
dow_list = tickers_dow()
for stock in dow_list:
    print(f"{stock} - {get_live_price(stock)}")

qtec = get_live_price('QTEC')
print(qtec)

print(get_stats('AAPL'))
print(get_data('AAPL'))

# try yahoofinancials as well


 