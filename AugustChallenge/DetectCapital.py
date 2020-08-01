class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if all(w.isupper() for w in word) or all(w.islower() for w in word):
            return True
        elif word[0].isupper() and all(w.islower() for w in word[1:len(word)]):
            return True
        else:
            return False
        
