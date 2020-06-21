class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seq=Counter(nums)        
        res,ans=0,0
        for key,value in seq.items():
            if key+1 in seq:
                res=seq[key]+seq[key+1]
                ans=max(ans,res)
        return ans        
                
                
         
            
