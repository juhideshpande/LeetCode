class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(2,len(cost),1):
            cost[i]+=min(cost[i-1],cost[i-2])
        return(min(cost[len(cost)-1],cost[len(cost)-2]))
        
