class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dictionary = {-1:0}
        for index,value in enumerate(nums):
            self.dictionary[index] = self.dictionary[index-1] + value

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dictionary[j]-self.dictionary[i-1] 

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
