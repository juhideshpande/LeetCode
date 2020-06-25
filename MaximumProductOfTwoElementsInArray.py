class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         product=None
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 temp=(nums[i]-1)*(nums[j]-1)
#                 if product< temp:
#                     product=temp
                    
#         return product  


        high=max(nums)
        nums.remove(high)
        nexthigh=max(nums)
        return (nexthigh-1)*(high-1)
    
