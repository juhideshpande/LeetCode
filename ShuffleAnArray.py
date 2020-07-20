class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arrayshuffled=nums
        self.arrayreset=list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.arrayshuffled=self.arrayreset
        self.arrayreset=list(self.arrayreset)
        return self.arrayshuffled

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.arrayshuffled)):
            swap=random.randrange(i,len(self.arrayshuffled))
            self.arrayshuffled[swap], self.arrayshuffled[i]= self.arrayshuffled[i], self.arrayshuffled[swap]
            
        return  self.arrayshuffled    


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
