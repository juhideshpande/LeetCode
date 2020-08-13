class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
		      return 0

        dp = [0 for x in range(len(s) + 1)]  # dp stores number of ways to decode a string
        #index stores length of integer in string
        # base case initialization
        dp[0] = 1 # empty string would be decoded as empty string so 1 way
        dp[1] = 0 if s[0] == "0" else 1   #(1) way to decode it

        for i in range(2, len(s) + 1): 
            # One step jump
            if 0 < int(s[i-1:i]) <= 9:    #(2)
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
        return dp[-1]
