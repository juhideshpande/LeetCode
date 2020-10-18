class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        if 2*k >= len(prices):  #because as k is more than half we can do transaction everyday. Time Complexity : O(N) N is number of transactions Space Complexity: O(1)
            profit=0
            for i in range(1, len(prices)):
                if prices[i]>prices[i-1]:
                    profit+=prices[i]-prices[i-1]
            return profit
        
        pnl = [0]*len(prices)
        for j in range(k):   #Time Complexity : O(N*k) N is number of transactions, Space Complexity: O(N)
            val = 0
            for i in range(1, len(pnl)): 
                val = max(pnl[i], val + prices[i] - prices[i-1]) 
                pnl[i] = max(pnl[i-1], val)
        return pnl[-1]
