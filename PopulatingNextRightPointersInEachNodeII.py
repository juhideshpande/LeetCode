"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return 
        
        stack=[root]
        stack.append(None)
        
        while stack:
            curr=stack.pop(0) #poll
            
            if curr==None and len(stack)==0:
                return root
            
            elif curr==None:
                stack.append(None)
                continue
                
            else:
                curr.next=stack[0] #peek
                
                if curr.left:
                    stack.append(curr.left)
                    
                if curr.right:
                    stack.append(curr.right)
                    
        return root 
