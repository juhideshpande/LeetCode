class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lenA=len(A)
        lenB=len(B)
        
        dp=[[0 for i in range(lenB+1)] for j in range (lenA+1)]
        
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    dp[i+1][j+1]=dp[i][j]+1                   
                    
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
                    
        return dp[lenA][lenB]            
                
        
