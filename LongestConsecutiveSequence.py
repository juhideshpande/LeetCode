class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        else:
            
            nums=sorted(set(nums))
            #print(nums.sort())
            length=0
            result=0
        
        
            for i in range(len(nums)-1):
                #print(nums[i])
                if nums[i+1]==1+nums[i]:
                    length+=1
                    result=max(result,length)
                else:
                    
                    print(result,length)
                    length=0
            return result+1 
