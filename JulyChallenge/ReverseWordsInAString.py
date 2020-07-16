class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=s.split()
        #print(s)
        ans=""
        
        for word in reversed(r):
            #temp=r.pop()
            if r.index(word)==0:
                ans+=r.pop()
            else:
                ans+=r.pop()+" "
        return ans    
