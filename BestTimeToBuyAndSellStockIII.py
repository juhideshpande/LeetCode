class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=0: 
            return 0
        
        firstBuy,secondBuy= - sys.maxint, -sys.maxint
        firstSell,secondSell= 0,0 
        
        for i in range(len(prices)):
            firstBuy=max(firstBuy,-prices[i])
            firstSell=max(firstSell, firstBuy+prices[i])
            secondBuy=max(secondBuy, firstSell-prices[i])
            secondSell=max(secondSell,secondBuy+prices[i])
            
        return secondSell   
    
    #Time and Space Complexity: O(n) , O(1)
