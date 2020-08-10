class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[amount+1]*(amount+1)
        dp[0]=0
        
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if coins[j]<=i:
                    dp[i]=min(dp[i], 1+dp[i-coins[j]])
                    
        if dp[-1]==amount+1:
            return -1
        else:
            return dp[-1]
                
            
                
            
        
