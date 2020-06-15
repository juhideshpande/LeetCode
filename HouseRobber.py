class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        temp1=0
        temp2=0
        for num in nums:
            temp1,temp2=temp2,max(num+temp1, temp2)
        return temp2     
