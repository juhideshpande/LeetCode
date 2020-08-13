class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.output=[]
        self.curr=-1
        
        q=collections.deque()
        q.append(("",0))
        n=len(characters)
        
        while q:
            temp, count = q.popleft()
            if len(temp)==combinationLength:
                self.output.append(temp)
                continue
                
            for i in range(count,n):
                q.append((temp+characters[i], i+1))
        

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.curr+=1
            return self.output[self.curr]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.curr+1 < len(self.output):
            return True
        else:
            return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
