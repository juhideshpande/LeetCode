class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x==0:
            return True
        
        if x<0 or x%10==0:
            return False
        
        else:
            
            temp=0
            p=x
            
            while x>temp:
                rem=x%10
                p=x
                x=x/10
                
                temp=temp*10+rem
                
            if p==temp or x==temp:
                return True
            else:
                return False
                
                
            
