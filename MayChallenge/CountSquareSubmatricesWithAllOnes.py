class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        lenm=len(matrix[0])
        lenn=len(matrix)
        
        ans=[[0] *(lenm+1) for _ in range(lenn+1)]
        
        count=0
        
        for row in range(1,lenn+1):
            for col in range(1,lenm+1):
                if matrix[row-1][col-1]==1:
                    ans[row][col]=1+min(ans[row][col-1],ans[row-1][col],ans[row-1][col-1])
                    count+=ans[row][col]
                    
        return count           
        
