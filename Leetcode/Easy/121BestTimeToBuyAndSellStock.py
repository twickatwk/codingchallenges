
# Time: O(N)
def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        maxProfit = 0
        maxPrice = 0
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > maxPrice:
                maxPrice = prices[i]
                continue
                
            profit = maxPrice - prices[i]
            
            if profit > maxProfit:
                maxProfit = profit
        
        return maxProfit

print(maxProfit([7,1,5,3,6,4]))