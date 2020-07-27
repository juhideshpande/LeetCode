class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res={}
        count,subarr=0,0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count+=-1                
            if count==0:
                subarr=i+1
            if count in res:
                subarr=max(subarr,i-res[count])
            else:
                res[count]=i
        return subarr        
                
           
