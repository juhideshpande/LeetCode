# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack=[(root,root.val)]
        
        while stack:
            curr, curr.val=stack.pop()
            
            if not curr.left and not curr.right:
                if curr.val==sum:
                    return True
            
            if curr.left:
                stack.append((curr.left, curr.val+curr.left.val))
                
            if curr.right:
                stack.append((curr.right, curr.val+curr.right.val))
                
        return False        
