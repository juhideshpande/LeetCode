import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        majority=collections.Counter(nums)
        for key, val in enumerate(nums):
            if (majority[val]> n/2):
                return nums[key]
       
    
