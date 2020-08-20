#X is start
#O is out of bound or water
#U is up
#D is down
# L is Left
# R Right
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0 
        self.steps = ''
        distinctIslands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # 'o' for origin
                    self.helper(grid, i, j, 'o')
                    distinctIslands.add(self.steps)
                    self.steps = ''
        return len(distinctIslands)
    
    def helper(self, grid, i, j, direct):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            self.steps += direct
            grid[i][j] = 0
            self.helper(grid, i+1, j, 'd')  # down
            self.helper(grid, i-1, j, 'u')  # upper
            self.helper(grid, i, j+1, 'r')  # right
            self.helper(grid, i, j-1, 'l')  # left
            self.steps += 'b'  # back
            
   #Time and space complexity : O(rows*cols)        
