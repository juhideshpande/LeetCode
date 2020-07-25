class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c = []
        for i, v in enumerate(S):
            if v == C:
                c.append(i)

        r = []
        for i in range(len(S)):
            r.append(min([abs(t - i)for t in c]))
        return r 
            
