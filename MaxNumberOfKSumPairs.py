import collections
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h=collections.defaultdict(int)
        print(h)        
        count=0
        visited=set()
        for i in  range(len(nums)):
            if k-nums[i] in h and h[k-nums[i]]>0:
                count+=1
                h[k-nums[i]]-=1
                
            else:
                h[nums[i]]+=1
                
        return count        
                
            
