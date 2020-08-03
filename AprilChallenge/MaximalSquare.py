class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        
        grid=[[0]*(n+1) for _ in range(m+1)]
        maxsqlen=0
       # print(grid)
        
         
        for r in range(1,m+1):
            for c in range(1,n+1):
                if matrix[r-1][c-1]=="1": 
                    grid[r][c] = min(min(grid[r-1][c],grid[r][c-1]), grid[r-1][c-1])+1
                    maxsqlen=max(maxsqlen, grid[r][c])
        
        return maxsqlen**2       
