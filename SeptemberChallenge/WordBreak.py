class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[False]*(len(s)+1)
        dp[0]=True
        
        
        for i in range(1,len(s)+1):
            for j in range(i):
                #count+=1
                print(j,dp[j])
                if dp[j] and s[j:i] in wordDict:
                    print(s[j:i])
                    dp[i]=True
                    break
        #print("count",count)            
        return dp[-1]            
         
        #Time complexity : O(n^3) Size of recursion tree can go up to n^2
#Space complexity : O(n) The depth of recursion tree can go up to n

            
