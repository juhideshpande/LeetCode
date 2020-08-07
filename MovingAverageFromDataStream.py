class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue=collections.deque()
        self.length=size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        avg, temp=0.0,0.0
        if len(self.queue)<self.length:
            self.queue.append(val)
        else:
            remove=self.queue.popleft()
            self.queue.append(val)
            
        for i in range(len(self.queue)):
            avg+=self.queue[i]
           
     
      
        return avg/len(self.queue)

            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
