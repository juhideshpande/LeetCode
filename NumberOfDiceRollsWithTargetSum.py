class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        mod = 10**9 + 7
        dp = [[0] * (target+1) for i in range(d+1)]
        dp[0][0] = 1
        
        for i in range(1, d+1):
            for j in range(1, target+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                dp[i][j] %= mod
                if j - f - 1 >= 0:
                    dp[i][j] = (dp[i][j] + mod - dp[i-1][j-f-1]) % mod
        return dp[-1][-1]
    
  #  Time complexity: O(d*f*target) Space Complexity:((d+1)*(target+1))
#https://www.youtube.com/watch?v=UiYVToWORMY
