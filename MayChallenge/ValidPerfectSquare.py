class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        numsqrt=num**0.5
        print(numsqrt)
        if numsqrt.is_integer() :
            return True
        return False
