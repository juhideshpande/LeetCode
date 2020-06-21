class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """       
        
        lnum=None
        snum=None
        tnum=None       
        if len(nums)==2:
            return sorted(nums)[1]
        if len(nums)==3:
            if nums[0]!=nums[1]!=nums[2]:
                return (min(nums))
            else: #nums[0]==nums[1] or nums[1]==nums[2] or nums[0]==nums[1]:
                return (max(nums))
        if(len(nums)>3):
            for i in range(len(nums)):
                if(nums[i]>lnum and nums[i]>snum and nums[i]>tnum):
                    tnum=snum
                    snum=lnum
                    lnum=nums[i]
                    print("First If:" ,(lnum,snum,tnum))
                if(nums[i]<lnum and nums[i]>snum and nums[i]>tnum):
                    tnum=snum
                    snum=nums[i]
                    print("Second if",(lnum,snum,tnum))
                if(nums[i]<snum and nums[i]>tnum):    
                    tnum=nums[i]
                    
            if(tnum==None):
                return lnum               
                    
        return tnum       
        
