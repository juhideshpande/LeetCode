class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):                         #<-- Approach 1
        x = ("{0:032b}".format(n)[::-1])
        return(int(x,2))
        
    def reverseBits(self, n):                         #<---Bit Manipulation Approach 2
        res = 0
        for _ in xrange(32):
            res = (res<<1) + (n&1)
            n>>=1
        return res    
