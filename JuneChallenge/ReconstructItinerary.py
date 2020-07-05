class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        route=[]
        stack=['JFK']
        itinerary= defaultdict(list)
     
        for src, dest in sorted(tickets, reverse=True):
            itinerary[src].append(dest)
       
        
        while stack:
            while itinerary[stack[-1]]:
                t_dest = itinerary[stack[-1]].pop()
                stack.append(t_dest)

            route.append(stack.pop())

        return route[::-1]    
                
        
    
