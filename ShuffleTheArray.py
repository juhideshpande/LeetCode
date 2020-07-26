class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            if i+n >len(nums)-1:
                break
            res.append(nums[i])
            res.append(nums[i+n])
        return res    
            
        
 
