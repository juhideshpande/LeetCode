class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        maps = {}
        for i in range(len(intervals)):
			maps[tuple(intervals[i])] = i
        intervals.sort(key = lambda x: x[0])
        res = [0]*len(intervals)
        for i in range(len(intervals)):
            start, end = intervals[i]
            index = self.binary_search(end, i + 1, len(intervals), intervals)
            if index == len(intervals):
                res[maps[tuple(intervals[i])]] = -1
            else:
                res[maps[tuple(intervals[i])]] = maps[tuple(intervals[index])]
        return res


    def binary_search(self, target, left, right, intervals):
        while left < right:
            mid = (left + right)/2
            if intervals[mid][0] >= target:
                right = mid
            else:
                left = mid + 1

        return left
