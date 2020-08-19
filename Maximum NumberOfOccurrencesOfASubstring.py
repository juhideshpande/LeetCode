class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        occ=collections.defaultdict(int)
        
        for i in range(len(s)):
            for j in range(i+minSize-1,min(i+maxSize,len(s))):
                temp=s[i:j+1]
                
                if len(set(temp))<=maxLetters:
                    occ[temp]+=1
                  
        if occ:            
            return max(occ.values())
        else:
            return 0
