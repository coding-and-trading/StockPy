import tushare as ts

# compute ema
def compute_EMA(stock_code, days, start, end):
    ''' Aglrothims detail : "Tranding for a living"Chapter 4'''
    k = round(2/(days+1), 2)
    price_history = ts.get_k_data(stock_code, start=start, end=end)
    close_price = price_history['close']
    print(close_price)
    price_len = len(price_history.index)
    
    EMA = []

    for i, price in enumerate(close_price[days:price_len]):
        days_MA = sum(close_price[0+i:days+i]) /days
        EMA.append(price*k + days_MA*(1-k))
    
    return EMA

def compute_diff(ema_12, ema_26):
    ''' compute the fast line(diff) '''
    return [x-y for x, y in zip(ema_12, ema_26)]

def compute_dea(diff):
    ''' compute the slow line(dea) '''
    days = 9 
    k = round(2/(days+1), 2)
    
    slow = []
    
    for i, value in enumerate(diff):
        days_MA = sum(diff[0+i:days+i]) /days
        slow.append(value*k + days_MA*(1-k))
    
    return slow

if __name__ == '__main__':
	start = '2017-10-11'
	end = '2017-10-31'
	ema = compute_EMA('002128', 10, start, end)
	ema_12 = compute_EMA('002128', 12, start, end)
	ema_26 = compute_EMA('002128', 26, start, end)

	print(ema_12)
	print(ema_26)
	diff = compute_diff(ema_12, ema_26)
	dea = compute_dea(diff)
	print(diff)
	print(dea)
	print(ema)
