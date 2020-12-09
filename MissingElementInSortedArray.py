class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        missing = lambda index: nums[index]-nums[0]-index
        
        if k>missing(len(nums)-1):
            return nums[-1]+k-missing(len(nums)-1) #larger than last element
        
        index=1
        while missing(index)<k:
            index+=1
            
        return nums[index-1]+k-missing(index-1)
