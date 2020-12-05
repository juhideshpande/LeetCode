class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ans=[]
        
        for i in range(1,n+1):
            if n%i==0:
                ans.append(i)
        return ans[k-1] if k<=len(ans) else -1
