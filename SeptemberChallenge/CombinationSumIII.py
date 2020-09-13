class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums=range(1,10)
        def combSum(nums,n,res,ans,ind,k):
            if n<0:
                return
            if n==0 and k==0:
                res.append(ans[:])            
                return
            for i in range(ind,len(nums)):
                ans.append(nums[i])
                combSum(nums,n-nums[i],res,ans,i+1,k-1)
                ans.pop()
        res = []
        combSum(nums,n,res,[],0,k)
        return res
