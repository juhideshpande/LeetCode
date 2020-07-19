class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        integer_sum = int(a, 2) + int(b, 2)
        binary_sum = bin(integer_sum)
        return(binary_sum[2:])
