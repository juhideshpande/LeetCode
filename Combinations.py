class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """        
        def combo(n,ans,index, res,k):
            if len(ans)==k:
                res.append(ans[:])
                return
            
            for i in range(index,n+1):
                ans.append(i)
                combo(n, ans, i+1, res,k)
                ans.remove(i)      
        
        
        res=[]
        combo(n,[], 1,res,k)
        return res
