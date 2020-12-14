class MyCalendarTwo(object):

    def __init__(self):
        self.calendar=[]
        self.overlaps=[]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.overlaps:
            if start<j and end>i:
                return False
        for i, j in self.calendar:
            if start<j and end>i:
                self.overlaps.append((max(start,i), min(end,j)))
        self.calendar.append((start, end)) #do not cleanup calendar if [1,2], [3,4] don't substitute as [1,4]
        return True       


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
