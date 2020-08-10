class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=len(nums)-1
        
        while i<j:
            mid = i+(j-i)//2            
            if nums[mid]<nums[j]:
                j=mid
            else:
                i=mid+1
        return nums[i]
    
    
############To find Maximum#################

        i=0
        j=len(nums)-1
        
        while i<j:
            mid=i+(j-i) // 2 
            
            if (mid < j and nums[mid + 1] < nums[mid]): 
                return nums[mid] 
                
            if (mid > i and nums[mid] < nums[mid - 1]): 
                return nums[mid - 1]    
            
            if nums[i]>nums[mid]:
                j=mid-1
            else:
                i=mid+1
        return nums[i]  
                
