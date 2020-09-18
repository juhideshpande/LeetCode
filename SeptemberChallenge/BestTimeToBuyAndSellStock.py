class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        minDay=sys.maxint
        for i in range(len(prices)):
            if prices[i]<minDay:
                minDay=prices[i]
            profit=max(profit,prices[i]-minDay)  
        return profit    
        
