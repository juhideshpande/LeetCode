class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        minimum,profit=sys.maxint,0
        
        for day in prices:
            if day<minimum:
                minimum=day
            
            profit=max(profit,day-minimum)
            
        return profit    
