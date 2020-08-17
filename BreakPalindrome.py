class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome)==1:
            return ""
               
        
        for i in range(len(palindrome)):
            if palindrome[i]!="a" and i != len(palindrome)//2:
                return palindrome[:i]+"a" + palindrome[i+1:]
            elif palindrome[i]=="a" and i == len(palindrome)-1:
                return palindrome[:-1]+"b"        
            
