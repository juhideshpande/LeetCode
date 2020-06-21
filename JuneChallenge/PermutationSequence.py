class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        x=[i for i in range(1,n+1)]              #<---- Using In built function
        result=list(itertools.permutations(x))
        return "".join([str(i) for i in list(result[k-1])])  
       

           
