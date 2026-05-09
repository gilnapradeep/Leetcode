class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0 # buy day     
        right = 1 # sell day 
        max_profit = 0 
        while right < len(prices): 
            if prices[right] > prices[left]: 
                profit = prices[right] - prices[left] 
                max_profit = max(max_profit, profit) 
            else: 
                left = right # better buying opportunity 
            right += 1 
        return max_profit