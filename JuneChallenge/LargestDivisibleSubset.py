class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        res = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(res[i]) < len(res[j]) + 1:
                    res[i] = res[j] + [nums[i]]
        return max(res, key=len)
                    
    
