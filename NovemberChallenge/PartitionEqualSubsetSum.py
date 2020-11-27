class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total=sum(nums)
        if total%2==1: #If the sum of all numbers is odd then it cannot be divided into two equal subsets
            return False
        
        total=total/2  #as it needs to be divided into two equal halves each subset should have total/2 sum
        dp=[0]*(total+1)
        dp[0]=1 #base case
        
        for num in nums:
            for i in range(total,num-1,-1):
                dp[i]=dp[i] or dp[i-num] # num + complement = dp[i] if num =dp[i] ie. number itself in dp is True or not or check if dp[complement] is True 
                
        return dp[total]   #return the last element of dp
