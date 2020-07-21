class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        
        dp=[[0]*n for _ in range(n)]
        
        for j in range(n):
            for i in range(j-1,-1,-1):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=min(dp[i][j-1],dp[i+1][j])+1
                    
        return dp[0][n-1]             
