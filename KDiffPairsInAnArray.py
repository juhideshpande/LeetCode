class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        if k == 0:
            dic = collections.Counter(nums)
            res = 0
            for val in dic.values():
                if val >= 2:
                    res += 1
            return res
        res = 0
        rec = set(nums)
        for key in rec:
            if key+k in rec:
                res += 1
        return res
