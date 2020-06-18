class Solution(object):
    def mark_border(self, i, j, board):
        if i==-1 or i==len(board):
            return
        if j==-1 or j==len(board[0]):
            return
        if board[i][j]=='O':
            board[i][j]=''
            self.mark_border(i-1, j, board)
            self.mark_border(i+1, j, board)
            self.mark_border(i, j-1, board)
            self.mark_border(i, j+1, board)
        
    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return []
        
        M, N = len(board), len(board[0])
        for i in range(M):
            self.mark_border(i, 0, board)
            self.mark_border(i, N-1, board)
        for j in range(N):
            self.mark_border(0, j, board)
            self.mark_border(M-1, j, board)
        
        for i in range(M):
            for j in range(N):
                if board[i][j]=='':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
    
