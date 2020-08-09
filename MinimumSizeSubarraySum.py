class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
       
        minLength=len(nums)+1
        start,end,currSum=0,0,0
        
        while end<len(nums):  
                currSum+=nums[end]
                              
                while currSum>=s:
                    minLength=min(minLength,end-start+1)
                    currSum-=nums[start]
                    start+=1
                end+=1     
                
        if minLength<=len(nums): 
            return minLength
        else:
            return 0 #if answer not present eg. s=3 nums=[1,1]
