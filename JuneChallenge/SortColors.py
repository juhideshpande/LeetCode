class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        counter = Counter(nums)
        cur = prev = 0
        for key, count in counter.items():
            cur += count
            nums[prev:cur] = [key] * count
            prev = cur
