import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
#         if n<1:                 #<--- with loop
#             return False
        
#         while(n%3==0):
#             n=n/3
            
#         return n==1    

        if n < 1:                  #<---without loop
            return False
        x = math.log(n,3)
        return abs(round(x) - x) < 0.0000000000001
    
    
    
        
