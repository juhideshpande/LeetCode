class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
#         chars={}
      
#         for i in range(len(letters)):
#             if letters[i] not in chars:            
#                  chars[i]=ord(letters[i])-ord('a')+97
                    
        
#         valord=ord(target)-ord('a')+97
        
#         for key,value in chars.items():
#             if valord<value:
#                 return chr(chars[key])
#         else:
#             return chr(chars[0])
        
        for c in letters:
            if c>target:
                return c
        return letters[0]    
            
            
