class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0 
      
    # initialize max 
        result = 0 
        n=len(nums)
        for i in range(0, n): 
      
        # Reset count when 0 is found 
           if (nums[i] == 0): 
                count = 0
  
        # If 1 is found, increment count 
        # and update result if count  
        # becomes more. 
           else: 
              
            # increase count 
                count+= 1 
                result = max(result, count)  
          
        return result
        
        
