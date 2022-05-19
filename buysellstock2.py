def bestStockii(prices):
    i,j = 0,1
    profit = []
    while j<len(prices):
        if prices[j]>prices[i]:
            profit.append(prices[j]-prices[i])
        i+=1
        j+=1

    print(sum(profit))


prices = [7,6,4,3,1]
bestStockii(prices)