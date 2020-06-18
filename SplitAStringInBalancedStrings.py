class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count,ans=0,0
        for i in range(len(s)):
            if s[i]=="R":
                count-=1
            elif s[i]=="L":
                count+=1
            
            if count==0:
                ans+=1
        
        return ans 
