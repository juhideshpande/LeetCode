class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0
        
        profit=0
        
        for day in range(len(prices)-1):
            if prices[day]<prices[day+1]:
                profit+=prices[day+1]-prices[day]
        
        return profit
