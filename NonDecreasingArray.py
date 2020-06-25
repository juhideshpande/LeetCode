class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        changed=0
        for i in range(0,len(nums)-1):
            if i==0 and nums[i]>nums[i+1] :
                nums[i]=nums[i+1]
                changed+=1
                    
            elif nums[i]>nums[i+1] and nums[i-1]>nums[i+1]:
                nums[i+1]=nums[i]
                changed+=1
                                
            elif nums[i]>nums[i+1] and nums[i-1]<=nums[i+1]:  
                nums[i]=nums[i+1]
                changed+=1
                
            if changed >1:
                return False
        return True    
        
        
