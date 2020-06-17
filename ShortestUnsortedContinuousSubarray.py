class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        comp=sorted(nums)
        res= [index for index, (e1, e2) in enumerate(zip(nums, comp)) if e1 != e2]
        if not res:
            return 0
        else:
            return res[-1]-res[0]+1
