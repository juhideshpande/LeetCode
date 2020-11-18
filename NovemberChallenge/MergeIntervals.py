class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        out = []
        if len(intervals)<2:
            return intervals
        
        intervals.sort()
        
        out.append(intervals[0])
        for (x, y) in intervals:
            lx, ly = out[-1]
            if x>ly: # meaning no overlapping
                out.append((x, y))
            else:
                out.pop()
                out.append((min(x, lx), max(ly, y)))
        return out                     
        
