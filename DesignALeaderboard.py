class Leaderboard(object):

    def __init__(self):
        self.leaderboard=defaultdict(int)
        

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        if playerId not in self.leaderboard:
            self.leaderboard[playerId]=score
        else: 
            self.leaderboard[playerId]+=score            
        
        

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        total=list(sorted(self.leaderboard.items(), key = lambda x: -x[1])[:K])
        #print(total)
        score = 0
        for i in range(len(total)):
            score+=total[i][1]
            
        return score    

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        self.leaderboard[playerId]=0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
