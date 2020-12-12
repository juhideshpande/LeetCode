class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if S>1000:
            return 0
        
        n=len(nums)
        m=2001
        origin=1000
        
        dp=[[0] * m for _ in range(n+1)]
        dp[0][0+origin]=1 #) is root node and the frequency of 0 at root is 1
        
        for i in range(1,n+1):
            for t in range(m):
                if dp[i-1][t]>0:
                    dp[i][t+nums[i-1]]+=dp[i-1][t]
                    dp[i][t-nums[i-1]]+=dp[i-1][t]
                
        return dp[n][S+origin]        
