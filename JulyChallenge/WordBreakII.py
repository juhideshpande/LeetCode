class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        self.dfs(s, wordDict, '', res)
        return res

    def dfs(self, s, dic, path, res):
    # Before we do dfs, we check whether the remaining string 
    # can be splitted by using the dictionary,
    # in this way we can decrease unnecessary computation greatly.
        if self.check(s, dic): # prunning
            if not s:
                res.append(path[:-1])
                return # backtracking
            for i in xrange(1, len(s)+1):
                if s[:i] in dic:
                    # dic.remove(s[:i])
                    self.dfs(s[i:], dic, path+s[:i]+" ", res)

    # DP code to check whether a string can be splitted by using the 
    # dic, this is the same as word break I.                
    def check(self, s, dic):
        dp = [False for i in xrange(len(s)+1)]
        dp[0] = True
        for i in xrange(1, len(s)+1):
            for j in xrange(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
        return dp[-1]
