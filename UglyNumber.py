class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        
        uglyNums=[2,3,5]
        for x in uglyNums:
            while num%x==0:
                num=num/x
                print(num)
        return num==1        
            
                
            
