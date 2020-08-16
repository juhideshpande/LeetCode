class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        step=1
        start=1
        numbers=n
        left=True
        
        while numbers>1:
            if left or numbers%2:
                start+=step
                
            step=step*2    
            numbers=numbers//2           
            
            left = not left
            
        return start     
        
     #   Time complexity : O(logN)
     #   Space Complexity : O(1)
