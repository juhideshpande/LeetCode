class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack=[]
            
        for i in range(len(S)):
            if not stack or stack[-1]!=S[i]:
                stack.append(S[i])
            else:    
                while stack and stack[-1]==S[i]:
                    stack.pop()
               
            
                
        return "".join(stack)
