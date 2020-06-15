# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:                      #  <---- Iterative
            if root.val==val:
                return root
            elif val<root.val:
                root=root.left
            else:
                root=root.right
        return root  
        
        
        if not root:                    # <----- Recursive       
          return None
        if root.val == val: 
          return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        
        return self.searchBST(root.right, val)
                
                
