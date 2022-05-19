def BuySellStock(prices):
    i = 0
    j = 1
    max_diff = 0
    while j<len(prices):
        if prices[j]-prices[i]>max_diff:
            max_diff = prices[j]-prices[i]

        if prices[j]<prices[i]:
            i = j
            j = i+1
        else:
            j+=1

    return max_diff
prices = [7,1,5,3,6,4]
print(BuySellStock(prices))