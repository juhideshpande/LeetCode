class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        pairs=Counter(A)
        
        for i in sorted(pairs, key=abs):
            if pairs[i]>pairs[2*i]:
                return False
            else:
                pairs[2*i]-=pairs[i]
        return True        
