class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels=set("AEIOUaeiou")
        words=S.split()

        for i in range(len(words)):
            if words[i][0] in vowels:
                words[i]=words[i]+"ma"+(i+1)*"a"                
            else:
                words[i]=words[i][1:]+words[i][0]+"ma"+(i+1)*"a"
                
        return " ".join(words)         
                
        # Time and Space Complexity : O(n)+O(k**2) k= number of words        
