class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """ 
        # From 23:59 to 00:00 go over every minute of 24 hours. If A meets this requirement, then totaly 24 * 60 minutes.
        A=sorted(A)
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                t = [h//10, h % 10, m // 10, m % 10]
                ts = sorted(t)
                if ts == A:
                    return str(t[0]) + str(t[1]) +':' + str(t[2]) + str(t[3])
        return '' 
