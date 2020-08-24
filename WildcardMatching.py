class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [ [ False ] * (len(s)+1) for i in range(len(p)+1)]
        dp[0][0] = True
        # ONLY CHANGE # case 1 : s = "aa", p = "*" ==> (1,0) should be True
        for i in range(1,len(p)+1):
            if p[i-1] == '*' and dp[i-1][0]==True:
                dp[i][0] = True
                
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == s[j-1] or p[i-1] == "?":
                    dp[i][j] = dp[i-1][j-1] 
                if p[i-1] == "*" :
                    # case 1 : extension, check upside and left side also
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]
    #bottom up approach of dynamic programming
#     Time complexity : O(SP) where S and P are lengths of the input string and the pattern correspondingly.
# Space complexity : O(SP) to keep the matrix.

