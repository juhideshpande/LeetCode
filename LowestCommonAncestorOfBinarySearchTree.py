# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if p.val > root.val and q.val>root.val: #Ancestor in right sub tree
                root=root.right
            elif p.val < root.val and q.val<root.val: #Ancestor in left sub tree
                root=root.left
            else:
                return root #found the split point which is LCA
                
        #Time Complexity : O(N) N=Number of nodes in BST
        #Space Complexity : O(1)
            
            
        
        
