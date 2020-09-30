class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 1
        else:
            length=range(1,len(nums)+2) #fails at [1] so take length+2
            for i in range(len(length)):
                if length[i] not in nums:
                    return length[i]
                
