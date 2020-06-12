class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        wordList=set(wordList)
        q= collections.deque([[beginWord,1]])
        
        while q:
            word,length=q.popleft()
            if word==endWord: return length 
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrtsuvwxyz':
                    temp=word[:i]+c+word[i+1:]
                    
                    if temp in wordList:
                        wordList.remove(temp)
                        q.append([temp,length+1])
        return 0                
        
        


