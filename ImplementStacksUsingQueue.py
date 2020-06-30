class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=[]

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        try:
            x=self.queue[-1]
            self.queue.remove(x)
            return x
        except:
            pass
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        try:
            return self.queue[-1]
        except:
            pass
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.queue)==0:
            return True
        else:
            return False
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
