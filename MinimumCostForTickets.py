class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0]* (days[-1]+1)
        for i in range(1,len(dp)):
            if i not in days:   # keep the previous cost, do buy anything
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1]+costs[0], dp[max(0,i-7)]+costs[1], dp[max(0,i-30)]+costs[2])
            
        return dp[-1]
        
