class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary={} 
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        root=self.dictionary # take the current pointer to root of the dictionary
        
        if not self.search(word): #word not present
            for i in range(len(word)):
                if word[i] not in root:
                    root[word[i]]={} #if the letter of the word not present then create a new dictionary for it
                root=root[word[i]] # otherwise just move to the next pointer
                
            root["#"]={} # this marks the end of the word that points to empty dictionary    
            
            
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        root=self.dictionary
        
        def rec(start, root):
            if start>=len(word): # reached the end
                if "#" in root:  # search do and dog present then should return False
                    return True
                else:
                    return False
            
            if word[start]==".": # need to search all nodes as . is a wildcard
                for key , val in root.items():
                    if rec(start+1, val): # if next and value present return True
                        return True
                return False
            
            elif word[start] in root: # if letter in dictionary
                if rec(start+1, root[word[start]]):
                    return True
            else:
                return False
        
        return rec(0, root)
            
                
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
