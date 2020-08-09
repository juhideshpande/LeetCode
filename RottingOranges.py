class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        fresh=0
        queue=collections.deque() #bfs traversal to add adjacent fresh oranges of rotten ones and timer+1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append((i,j,0)) # timer set to 0
                    
        seen=set() # to keep track of already rotten oranges that are visited           
                    
        
        
        while queue:
            direction=[[0,1],[1,0],[0,-1],[-1,0]] #do not consider diagonal elements
            x,y,timer=queue.popleft()
            
            for x1, y1 in direction:
                if 0<=x+x1<len(grid) and 0<=y+y1<len(grid[0]) and (x+x1, y+y1) not in seen and grid[x+x1][y+y1]==1:
                    seen.add((x+x1,y+y1))
                    fresh-=1
                    if fresh==0:
                        return timer+1
                    queue.append((x+x1, y+y1, timer+1))
                    
        if fresh!=0:
            return -1
        else:
            return 0 #because if no fresh present it should return 0 eg. [[0,2]]
        
        
                
