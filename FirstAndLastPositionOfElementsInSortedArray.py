class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count=Counter(nums)
        #print(count)
        res=[]
        
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
                temp=i+(count[nums[i]]-1)
                res.append(temp)
                break
            
            
            
        if len(res)==0:    
                res=[-1,-1]
        return res  
