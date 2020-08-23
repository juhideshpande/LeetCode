class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        n = len(words[0])
        prefixes= collections.defaultdict(list)
        for word in words:
            for i in range(n):
                prefixes[word[:i]].append(word)
       # print(prefixes)   
        
        
        def build(cur):
            if len(cur) == n:
                squares.append(cur)
                return
        
            prefix = ''
            for word in cur:
                prefix += word[len(cur)]
                #print(prefix,word,cur,word[len(cur)])

            for word in prefixes[prefix]:
                build(cur + [word])
                
        squares = []
        for word in words:
            build([word])
        return squares
