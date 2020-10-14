class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def robbery(nums, i, j):
            temp1=0
            temp2=0
            for num in range(i,j):
                temp1,temp2=temp2,max(nums[num]+temp1, temp2)
            return temp2     
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            n = len(nums)
            return max(robbery(nums, 1, n), robbery(nums, 0, n-1))
