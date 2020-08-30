class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort(reverse=1)
        print(events)
        h = []
        res = d = 0
        
        while events or h:
            if not h: 
                d = events[-1][0]
                print(d)
            while events and events[-1][0] <= d:
                heapq.heappush(h, events.pop()[1])
                print(h,"heap")
            heapq.heappop(h)
            res += 1
            d += 1
            print("befor",h)
            while h and h[0] < d:
                heapq.heappop(h)
                print("after",h)
        return res
