import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # i, dp = 1, [0] + [float('inf')] * (n)
        # for i in xrange(1, n+1):
        #     for j in range(1, int(math.sqrt(i))+1):
        #         dp[i] = min(dp[i], 1 + dp[i-int(j*j)])
        # return dp[-1]
        
        while not (n%4):       #results are the same for n and 4n
            n /= 4
        if n%8 == 7:
            return 4
        x = int(math.sqrt(n)+1)
        for i in range(x):
            j = math.floor(math.sqrt(n - i*i))
            if i*i + j*j == n:
                if i > 0 and j > 0:
                    return 2
                else:
                    return 1           
        return 3  
        
