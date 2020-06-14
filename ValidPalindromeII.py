class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                a=s[:i]+s[i+1:]
                b=s[:j]+s[j+1:]
                i+=1
                j-=1                
                return a==a[::-1] or b==b[::-1]            
            else:
                i+=1
                j-=1
                
        return True       
            
