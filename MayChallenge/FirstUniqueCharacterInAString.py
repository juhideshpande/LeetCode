class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        # count=collections.Counter(s)
        # print(count)
        # for key,val in enumerate(s):
        #     if count[val]==1:
        #         return key
        # return -1  
        
        for i in range(len(s)):
            if(s.count(s[i])==1):
                return i
        return -1

        
