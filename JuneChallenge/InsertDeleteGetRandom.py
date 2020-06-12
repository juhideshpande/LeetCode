class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ds=[]
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.ds:
            self.ds.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        try:
            if val in self.ds:
                self.ds.remove(val)
                return True
        except:
            pass
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        try:
            x=random.choice(self.ds)
            return x
        except:
            pass


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
