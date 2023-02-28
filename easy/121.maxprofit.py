def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    
    print(prices)
    maxval = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] < prices[j]:
                if maxval < abs(prices[i] - prices[j]):
                    maxval = abs(prices[i] - prices[j])
                    
    print(maxval)
            # if maxval < (prices[i] - prices[j]):
            #     maxval = prices[i] - prices[j]
            #     print(i,j)
            #     print(maxval)
    
    
maxProfit([7,1,5,3,6,4])
maxProfit([7,6,4,3,1])