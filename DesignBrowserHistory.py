class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.curr = 0
        self.bound = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr] = url
        self.bound = self.curr
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.curr = min(self.curr + steps, self.bound)
        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
