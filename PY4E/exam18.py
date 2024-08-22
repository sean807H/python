def stock_profit(stocks, sells):
    stock_info = stocks.split(',')
    stock_data = []
    
    for info in stock_info:
        name, quantity, average_price = info.split('/')
        quantity = int(quantity)
        average_price = int(average_price)
        sell_price = sells.pop(0)
        
        profit = (sell_price - average_price) / average_price * 100
        
        stock_data.append((name, profit))
    
    stock_data.sort(key=lambda x: x[1], reverse=True)
    
    for name, profit in stock_data:
        print(f"{name}의 수익률 {profit:.2f}")

stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

stock_profit(stocks, sells)
