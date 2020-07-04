class Solution(object):
    def isHappy(self, n):
        numbers=[]

        while True:
            sumnum = 0
            while (n > 0):
                temp = n % 10
                sumnum += temp * temp
                #print(sumnum)
                n = n // 10
            if (sumnum == 1):
                return True
            elif sumnum in numbers:
                return False
            else:
                numbers.append(sumnum)
            n = sumnum
        
        
