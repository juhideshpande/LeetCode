import sys
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        k=self.Kadane(A)
        A_inverted=[-x for x in A]
        A_inverted=self.Kadane(A_inverted)
        temp=sum(A)+A_inverted
        if temp>k and temp!=0:
            return temp
        else:
            return k
    
    def Kadane(self,nums):
        currentMax=-(sys.maxsize-1)
        totalMax=-(sys.maxsize-1)
        for i in range(len(nums)):
            currentMax=max(currentMax,0)+nums[i]
            totalMax=max(currentMax, totalMax)
        return totalMax    
