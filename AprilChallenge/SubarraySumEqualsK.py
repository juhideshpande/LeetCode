class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen={0:1}
        val,count=0,0
        for i in nums:
            val+=i
            if val-k in seen:
                count+=seen[val-k]
            if val in seen:    
                seen[val]+=1
            else:
                seen[val]=1
        return count        
                
