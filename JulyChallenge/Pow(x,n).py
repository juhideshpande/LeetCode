class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: 
            return 1.0
        if n == 1: 
            return x
        if n < 0: 
            return self.myPow(1/x, -n)
        
        result = self.myPow(x, n//2)
        result *= result
        if n%2 == 1: 
            result *= x
        return result
