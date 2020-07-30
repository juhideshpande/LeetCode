class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:      #https://www.youtube.com/watch?v=w6xk5Po-DX0
            return 0
        
        if len(prices)==2 and prices[0]<prices[1]:
            return prices[1]-prices[0]
        
        elif len(prices)==2 and prices[0]>prices[1]:
            return 0
        
        buy=[0]*len(prices)
        sell=[0]*len(prices)
        
        buy[0]=-prices[0]
        sell[0]=0
        
        sell[1]=max(sell[0],buy[0]+prices[1])
        buy[1]=max(buy[0],sell[0]-prices[1])
        
        for i in range(2,len(prices)):
            sell[i]=max(buy[i-1]+prices[i], sell[i-1])
            buy[i]=max(sell[i-2]-prices[i],buy[i-1])
            
        return sell[len(prices)-1]    #sell because we do not have to keep the bought stocks at last 
