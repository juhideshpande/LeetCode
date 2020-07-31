class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        n1 = 1
        n2 = 2
        if(n==1):
            return n1
        elif(n==2):
            return n2
        else:
            for i in range(2,n):
                result = n1+n2
                n1=n2
                n2=result

        return(result)

