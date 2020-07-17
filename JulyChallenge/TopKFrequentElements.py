class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency={}
        for i in nums:
            if i not in frequency:
                frequency[i]=1
            else:
                frequency[i]+=1
                
        result=sorted(frequency,key=lambda w:(-frequency[w],w))[:k]
        return (result)
