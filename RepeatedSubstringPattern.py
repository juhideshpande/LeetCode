class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        kmp=[0]*len(s)
        
        for i in range(1, len(s)):
            j=kmp[i-1] #for suffix
            
            while j>0 and s[i]!=s[j]:
                j=kmp[j-1]
                
            if s[i]==s[j]: #prefix and suffix match
                j+=1
                
            kmp[i]=j  

        p=kmp[len(s)-1]
        
        return p!=0 and len(s)%(len(s)-p)==0  # check if it's repeated pattern string
    
    
#     Time complexity: O(N). During the execution, j could be decreased at most N times and then increased at most N times, that makes overall execution time to be linear O(N).

# Space complexity: O(N) to keep the lookup table.
