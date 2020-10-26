class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans=[]
        third=-sys.maxint
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < third:
                return True
            
            while ans and ans[-1]<nums[i]:
                third=ans.pop()
                
            ans.append(nums[i])        
           
        return False
