class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) != len(B): 
            return -1
        same, countA, countB = Counter(), Counter(A), Counter(B)
        
        for a, b in zip(A, B):
            if a == b:
                same[a] += 1
                
        for i in range(1, 7):
            if countA[i] + countB[i] - same[i] == len(A):
                return min(countA[i], countB[i]) - same[i]        
        return -1
