import math
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c1 = c2 = float('inf')
        for num in nums:
            if num <= c1:
                c1 = num
            elif num <= c2:
                c2 = num
            else:
                return True

        return False
    
        
        
