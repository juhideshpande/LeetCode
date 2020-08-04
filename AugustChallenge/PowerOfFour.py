import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
#         if num<1:
#             return False
#         while num%4==0:
#             num/=4
            
#         return num==1    

        if num==1:
            return True
        return num>0 and (num % 10 == 4 or num % 10 == 6) and (num & (num-1)==0)
