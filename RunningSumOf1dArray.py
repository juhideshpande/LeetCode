class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        temp=0
        for i in range(len(nums)):
            temp+=nums[i]
            res.append(temp)
            
        return res    
            
