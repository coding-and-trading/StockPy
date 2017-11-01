import tushare as ts

start = '2017-10-11'
end = '2017-10-31'

def compute_EMA(stock_code, days, start, end):
    ''' Aglrothims detail : "Tranding for a living"Chapter 4'''
    k = round(2/(days+1), 2)
    price_history = ts.get_k_data(stock_code, start=start, end=end)
    close_price = price_history['close']
    price_len = len(price_history.index)
    
    EMA = []
    days_MA = sum(close_price[0:days]) /days

    for i, price in enumerate(close_price[days:price_len]):
        days_MA = sum(close_price[0+i:days+i]) /days
        EMA.append(price*k + days_MA*(1-k))
    
    return EMA

if __name__ == '__main__':
	ema = compute_EMA('002128', 10, start, end)
	print(ema)
