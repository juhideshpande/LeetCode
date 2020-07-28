class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_score = [0]*(N+1)
        for a, b in trust:
            trust_score[b] += 1
            trust_score[a] -= 1

        for idx, score in enumerate(trust_score):
            if idx != 0 and score == N-1:
                return idx
        return -1
