class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=2*n
        ans = self.factorial(a)
        div= self.factorial(n+1)*self.factorial(n)
        
        res=ans/div
        return res
    
    
    def factorial(self,n):
        res=1
        for i in range(1,n+1):
            res*=i
        return res

        
