class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(nums)-1
        
        while low<high:
            mid=low+(high-low)//2
            #print(mid)
            if nums[mid]>nums[high]:
                #print("in if")
                low=mid+1
                
            elif nums[mid]==nums[high] and nums[low]==nums[high]:                
                if nums[mid]>nums[mid+1] or nums[high-1]<nums[mid]:
                    low=mid+1
                else:
                    high=mid
                    
            else:
                high=mid
               # print("in else")
        return nums[low]        
