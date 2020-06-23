class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        num1=[str(x) for x in A]
        res=int("".join(num1))
    
        ans=res+K
        res2 = list(map(int, str(ans))) 
        return res2
        
        
