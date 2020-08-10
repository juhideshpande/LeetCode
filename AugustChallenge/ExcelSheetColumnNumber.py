class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in s:
            #print(res,"b")
            res = res*26 + ord(i)-ord('A')+1
            #print(res,"a")
        return res
