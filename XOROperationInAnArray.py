class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        xor=0
        for i in range(0,n):
            xor = xor ^ (start+2*i)            
        return xor    
            
 
