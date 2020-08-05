class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(board), len(board[0])
        crushed = False
		# horizontal crushed
        for i in range(m):
            for j in range(n - 2):
                if board[i][j] == 0: continue
                v = abs(board[i][j])
                if v == abs(board[i][j + 1]) == abs(board[i][j + 2]):
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -v
                    crushed = True
        # vertical crushed
        for i in range(m - 2):
            for j in range(n):
                if board[i][j] == 0: continue
                v = abs(board[i][j])
                if v == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -v
                    crushed = True
        # gravity
        
        print(board)
        if crushed:
            for j in range(n):
                row_index = m - 1
                for i in range(m - 1, -1, -1):
                    if board[i][j] > 0:
                        board[row_index][j] = board[i][j]
                        row_index -= 1
                while row_index >= 0:
                    board[row_index][j] = 0
                    row_index -= 1
        return self.candyCrush(board) if crushed else board
