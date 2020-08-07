class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        temp=0
        
        while n/5>0:  #5*2=10 count the quotient of multiples of 5, 25, 125, 625, 3125...
            temp=n/5
            count+=temp
            n=temp
            
        return count    
    
   
