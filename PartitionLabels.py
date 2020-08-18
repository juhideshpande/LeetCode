class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result=[]
        endIndex={}
        lastSeen=0
        left=0 #partition
        for index, char in enumerate(S):
            endIndex[char]=index
            
        for index, char in enumerate(S):
            lastSeen=max(lastSeen, endIndex[char])
           
            
            if index==lastSeen:
                result.append(index-left+1)
                left=index+1
        return result        
            
       #Time Complexity: O(N) = N is length of S; O(1) to keep data structure "endIndex" of not more than 26 characters.
