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
            #print(int(math.sqrt(n)))  
            binary="{0:b}".format(n)
            #count=binary.index(1)
            #print(len(binary))

            for i in range(1,len(binary)):
                #print("i",i)
                #print(int(math.sqrt(n)))
                temp=2**i
                if n%temp!=0:
                    return False
            return True    
