class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.collection=[]
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.collection.append(val)
        #    print("insert",self.collection)
        return True
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        try:
            if val in self.collection:
                self.collection.remove(val)
                #print(self.collection)
                return True
            else:

                return False
        except:
            pass
        
    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        try:
            if self.collection:
                return random.choice(self.collection)
        except:
            pass
            


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
