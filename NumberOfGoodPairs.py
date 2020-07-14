class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        pairs = 0
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        for key in freq.keys():
            if (freq[key] > 1):
                pairs += sum(range(freq[key]))
        return pairs
