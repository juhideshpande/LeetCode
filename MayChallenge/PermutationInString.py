class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1=[0]*26
        l2=[0]*26
        for i in s1:
            l1[ord(i)-ord('a')]+=1
            
            
        for i in range(len(s2)):
            l2[ord(s2[i])-ord('a')]+=1
            if i>=len(s1):
                l2[ord(s2[i-len(s1)]) -ord('a')]-=1
            if l1==l2:
                return True
        return False                         
                    
               
