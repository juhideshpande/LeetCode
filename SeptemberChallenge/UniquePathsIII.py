class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.totalPaths = 0
        empty = 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1: 
                    x,y = (i, j)        # start point
                elif grid[i][j] == 2: 
                    self.end = (i, j)   # end point
                elif grid[i][j] == 0: 
                    empty += 1          # count no. of empty spaces
                    
        self.dfs(grid, x, y, empty)
        return self.totalPaths
    
    def dfs(self, grid, x, y, empty):

        if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] >= 0): 
            return

        if (x, y) == self.end:
            if empty == 0:              # Problem says -> path that walk over every non-obstacle square exactly once.
                self.totalPaths += 1
            return

        grid[x][y] = -2
        self.dfs(grid, x + 1, y, empty - 1)
        self.dfs(grid, x - 1, y, empty - 1)
        self.dfs(grid, x, y + 1, empty - 1)
        self.dfs(grid, x, y - 1, empty - 1)
        grid[x][y] = 0
