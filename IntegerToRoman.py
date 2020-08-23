class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        i=0
        while num>0:
           # print(i)
            if num-integers[i]>=0: #subtract the given number from the highest value that matches hence array arranged in descending order
                print(integers[i])
                result+=roman[i]
                num-=integers[i]
            else:
                i+=1
        return result        
