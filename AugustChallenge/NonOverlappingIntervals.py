class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals=sorted(intervals, key = lambda x :(x[1]))
        removed=0
        end=intervals[0][1]
        
        for i in range(1,len(intervals)):            
            if end >intervals[i][0]:                
                removed+=1
            else:
                end=intervals[i][1]
               

        return removed       
        
        
