class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        answer=[]
        i=0
        
        for i, (start,end) in enumerate(intervals):
            if end<newInterval[0]:
                answer.append([start,end])
            elif newInterval[1]<start:
                i-=1
                break
            else:
                newInterval[0]=min(newInterval[0],start)
                newInterval[1]=max(newInterval[1],end)
                
        return answer+[newInterval]+intervals[i+1:]       
