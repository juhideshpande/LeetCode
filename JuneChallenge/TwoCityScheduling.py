class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        mincost=0
        sorted_costs=sorted(costs,key=lambda x: x[0]-x[1])
        
        for i in range (len(costs)):
            if i<len(costs)//2:
                mincost+=sorted_costs[i][0]
            else:
                mincost+=sorted_costs[i][1]
                
        return mincost       
        
