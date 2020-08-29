class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        res = []
        for i in range(n):
            cur_max = max(A[0:n-i])
            j = 0
            while A[j] != cur_max:
                j += 1
            # should reverse j+1 elements
            A[:j+1] = reversed(A[:j+1])
            res.append(j+1)
            # reverse all
            A[:n-i] = reversed(A[:n-i])
            res.append(n-i)
        return res
        
