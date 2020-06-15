def findCheapestPrice(n, flights, src, dst, K):
    """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
     """
    pq, g = [(0,src,K+1)], collections.defaultdict(dict)
    for s,d,w in flights: 
        g[s][d] = w
    while pq:
        cost, s, k = heapq.heappop(pq)
        if s == dst: 
            return cost
        if not k: continue
        for d in g[s]:
            heapq.heappush(pq, (cost+g[s][d], d, k-1))
    return -1
