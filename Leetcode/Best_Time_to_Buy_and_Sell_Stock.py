class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Go through loop, calculate min price and max profit as you go

        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            
            if price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
    
# RT: 26 ms Beats 97.32%; Memory: 19.14 MB Beats 23.99%