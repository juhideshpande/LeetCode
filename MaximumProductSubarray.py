class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)==1):
            return nums[0]
        else:
            ans,pos,neg=0,0,0
            for i in nums:
                pos,neg=max(pos*i,neg*i,i),min(pos*i,neg*i,i)
                ans=max(pos,neg,ans)
              
            return ans    
        
        # pos = neg = mx =0
        # if len(nums)==1: return nums[0]
        # for n in nums:
        #     pos,neg = max(pos*n,neg*n,n),min(pos*n,neg*n,n)
        #     mx = max(mx,pos,neg)
        # return mx
