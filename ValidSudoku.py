class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen=set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    cur=board[i][j]
                    if (i,cur) in seen or (cur,j) in seen or (i//3, j//3, cur) in seen:  
                        return False
                    
                    seen.add((i,cur))
                    seen.add((cur,j))
                    seen.add((i//3, j//3, cur))
                    
        return True             
    
#Time complexity : O(1) since all we do here is just one iteration over the board with 81 cells
# Space complexity : O(1)
