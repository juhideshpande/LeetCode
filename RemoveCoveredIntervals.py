class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        total=1
        intervals=sorted(intervals, key=lambda i: (i[0], -i[1]))
        end=intervals[0][1]
        
        for i in intervals:
            if i[1]>end:
                end=i[1]
                total+=1
                
        return total        
       
