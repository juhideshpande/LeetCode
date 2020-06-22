class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count=Counter(nums)
        # for key, value in count.items():
        #     if value==1:
        #         return key
        
        ones=0
        twos=0
        
        for i in nums:
            ones=(ones ^ i) & (~twos)
            twos=(twos ^ i ) & (~ones)
        return ones    
