class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        try:
            x=self.stack[0]
            del self.stack[0]
            return x
        except:
            pass

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        try:
            return self.stack[0]
        except:
            pass
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()