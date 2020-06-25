class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        numbers=0
        for i in range(L,R+1):
            temp='{0:0032b}'.format(i)
            ones=temp.count('1')
            if ones>1:
                for j in range(2, ones):
                    if ones%j==0:
                        break
                else:  
                    numbers+=1
        return numbers             
            
        
