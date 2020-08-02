class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        reachable =0
        for i in range(n):
            if(reachable<i):
                return False
            reachable=max(reachable,i+nums[i])
        return True    
