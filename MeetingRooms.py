class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals=sorted(intervals, key=lambda x:(x[0],x[1]))
        #print(intervals)
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
               # print(end, start+1)
                return False
        return True    
