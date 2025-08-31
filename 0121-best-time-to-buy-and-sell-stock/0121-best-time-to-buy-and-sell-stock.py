class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        min_buy=prices[0]
        for i in  range(1,len(prices)):
            if prices[i]>min_buy:
                max_profit=max(max_profit,prices[i]-min_buy)
            min_buy=min(min_buy,prices[i])        
        return max_profit





        