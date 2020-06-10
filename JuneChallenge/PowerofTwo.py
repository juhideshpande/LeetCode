class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        elif n==0:
            return False
        else:
            binary="{0:b}".format(n)
            
            for i in range(1,len(binary)):
                temp=2**i
                if n%temp!=0:
                    return False
            return True    
