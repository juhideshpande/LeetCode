class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        
        
        while i > 0 and nums[i-1] >= nums[i]: #find the first ascending part 
            i-=1
        if i==0:#numbers were all in descending order so the next permutation is [] and need to return the lowest permutation
            nums.reverse()
            return
        
        k=i-1
        while j<len(nums) and nums[j]<=nums[k]: # find the next greatest element then nums[k] in the second part and swap them
            j-=1
        nums[k],nums[j]=nums[j],nums[k]
        
        l=k+1 #element that was greater 
        r=len(nums)-1
        
        while l<r: #sort the second part
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
            
#Time Complexity: O(N) N=len(nums)  Space Complexity: O(1)         
        
        
        
        
        
        
        
        
        
        
