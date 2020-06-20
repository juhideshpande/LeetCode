class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         res=itertools.permutations(nums)
#         return res

        if len(nums)<=1:
            return [nums]
        res = []
        for i in range(len(nums)):
            rest = nums[:i]+nums[i+1:]
            for p in self.permute(rest):
                res.append([nums[i]]+p)
        return res 
        
