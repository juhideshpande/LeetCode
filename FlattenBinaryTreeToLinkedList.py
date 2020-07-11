# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return None
        
        stack=[]
        stack.append(root)
        while stack:
            temp=TreeNode(0)
            temp=stack.pop()
            
            if temp.right:
                stack.append(temp.right)
                
            if temp.left:
                stack.append(temp.left)
                
            if (len(stack)!=0):
                temp.right=stack[-1]
                
            temp.left=None    
