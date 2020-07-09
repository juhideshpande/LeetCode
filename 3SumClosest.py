class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums=sorted(nums)
        closest=sum(nums[:3])
        
        for i in range(len(nums)-2):
            low=i+1
            high=len(nums)-1
            
            while low<high:
                total = nums[i]+nums[low]+nums[high]
                
                if abs(closest-target) > abs(total-target):
                    closest=total
                    
                if total<target:
                    low+=1
                elif total>target:
                    high-=1
                else:
                    return total
        return closest       
            
            
