class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        search={}
        nums=sorted(nums)
        triplets=set()
        for i,n in enumerate(nums):
            search[n]=i
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                target=-(nums[i]+nums[j])
                if target in search and search[target]>j:
                    triplets.add((nums[i],nums[j],-(nums[i]+nums[j])))
                    
        return list(triplets)
