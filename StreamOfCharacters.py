class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie       
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word
        

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.stream.appendleft(letter)
        
        node = self.trie
        for ch in self.stream:
            if '$' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]
        return '$' in node
    
    
   # Time complexity: O(M), where M is a max word length, i.e. the depth of trie.

#Space complexity: O(M) to keep a stream of characters.


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
