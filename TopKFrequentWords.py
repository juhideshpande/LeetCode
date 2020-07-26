class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        frequency={}
       
        #count=0
        for i in words:
          #  print(words[i])
            if i not in frequency:
                frequency[i]=1
            else:
                frequency[i]+=1
                
        s1 = sorted(frequency, key=lambda w :(-frequency[w],w))  
        return s1[:k]  
