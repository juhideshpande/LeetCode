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
                
