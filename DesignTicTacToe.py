class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row=[0]*n
        self.col=[0]*n
        self.diag=0
        self.antidiag=0
        self.n=n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        points = 1 if player==1 else -1 
        self.row[row] +=points
        self.col[col] +=points   
        if row==col:
            self.diag+=points
        if row+col==self.n-1:
            self.antidiag+=points
            
        if abs(self.row[row])==self.n or abs(self.col[col])==self.n or abs(self.diag)==self.n or abs(self.antidiag)==self.n:
            return player
        return 0
            
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
