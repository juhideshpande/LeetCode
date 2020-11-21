class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        elif len(set(nums))==1:
            return nums[0]==target
        
        i=0
        j=len(nums)-1
        
        while nums[i]==nums[j]:
            i+=1
            
        while i<=j:
            mid=i+(j-i)//2
            
            if nums[mid]==target:
                #found=True
                return True
            
            elif nums[i]<=nums[mid]:
                if nums[i]<=target<=nums[mid]:
                    j=mid-1
                else:
                    i=mid+1
                    
            else:
                if nums[mid] <= target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
                
        return False    
