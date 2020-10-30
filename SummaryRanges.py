class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        begin, res = 0, []
        strout = lambda b, e: str(b) + "->" + str(e) if b != e else str(b)
        for i in range(1, len(nums)+1):
            if i == len(nums) or nums[i] - nums[i-1] != 1:
                res.append(strout(nums[begin], nums[i-1]))
                begin = i
        return res
