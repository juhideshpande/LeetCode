class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
#         pairs=Counter(A)
        
#         for i in sorted(pairs, key=abs):
#             if pairs[i]>pairs[2*i]:
#                 return False
#             else:
#                 pairs[2*i]-=pairs[i]
#         return True    


        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: 
                continue
            if count[2*x] == 0: 
                return False
            count[x] -= 1
            count[2*x] -= 1
            print(count)

        return True
