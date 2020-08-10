class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentMax=-(sys.maxsize-1)
        totalMax=-(sys.maxsize-1)
        for i in range(len(nums)):
            currentMax=max(currentMax,0)+nums[i]
            totalMax=max(currentMax, totalMax)
        return totalMax  
            
        



        
        
