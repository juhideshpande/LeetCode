class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while k>0:
            nums.insert(0, nums[-1])
            nums.pop()
            k -= 1
            
           
            
        
        # if len(nums)<2 or k==0 or k==len(nums): return nums
        # if k<len(nums): nums[:]=nums[-k:]+nums[:len(nums)-k]
        # if k>len(nums):
        #     k=k-len(nums)
        #     nums[:]=nums[-k:]+nums[:len(nums)-k]
