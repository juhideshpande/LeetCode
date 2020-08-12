class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        search={}
        for index, val in enumerate(order):
            search[val]=index
            
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            
            for j in range(min(len(w1),len(w2))):
                c=w1[j]
                d=w2[j]
                if c!=d:
                    if search[c]>search[d]:
                        return False
                    break          
                
                if j==min(len(w1),len(w2))-1 and len(w1)>len(w2):
                    return False
        return True        
            
    #   Time Complexity : O(C) where C is total content of words
    # Space Complexity : O(1)
