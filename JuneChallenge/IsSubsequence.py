class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j,i=0,0
        temp=""

        while(i<len(s) and j<len(t)):

            if s[i]==t[j]:
                temp+=s[i]
                i+=1
                j+=1

            elif s[i]!=t[j]:
                 j+=1
                    

                  
        return (True if temp==s else False) 
