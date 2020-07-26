class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = int("{0:b}".format(num))
        print(binary)
        i=0
        decimal=0
        while(binary>0):
            x=binary%10
            decimal = decimal+((x==0 if 1 else 0))*pow(2,i)
            i+=1
            binary=binary//10
        return (decimal)
