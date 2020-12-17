class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        cnt = collections.defaultdict(lambda : [0] * len(votes[0]))
       # print(cnt)
        for v in votes:
            for i, c in enumerate(v):
                cnt[c][i] -= 1
               # print(cnt,i,c)
        return ''.join(sorted(votes[0], key = lambda x:(cnt[x], x)))        
