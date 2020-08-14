class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        seen=set()
        
        for c in s:
            if c not in seen:
                seen.add(c)
            else:
                seen.remove(c)
                
        if len(seen)>0:        
            return len(s)-len(seen)+1
        else:
            return len(s)
