class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        perimeter=0
        lrow,lcol=len(grid), len(grid[0])
        
        for row in range(lrow):
            for col in range(lcol):
                if grid[row][col]==1:               
                    if row==lrow-1 or grid[row+1][col] ==0:
                        perimeter+=1
                    if  row==0 or grid[row-1][col]==0: 
                        perimeter+=1
                    if col==0 or grid[row][col-1]==0: 
                        perimeter+=1
                    if col==lcol-1 or grid[row][col+1]==0: 
                        perimeter+=1 
                  
        return perimeter         
                
