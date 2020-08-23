# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if not node:
                return 0,None
            
            heightLeft,lcaLeft = dfs(node.left)
            heightRight,lcaRight = dfs(node.right)
            
            if heightRight > heightLeft: #if right is at greater height return right subtree
                return heightRight + 1,lcaRight
            
            elif heightRight < heightLeft: #if left is at greater height return left subtree
                return heightLeft + 1,lcaLeft
            
            else: #if eqaul then return current node that is root of left and right subtree
                return heightLeft + 1,node
            
        return dfs(root)[1]
    
    # Time On traversal
    # space OHeight recursive
    #   1        left child height 2 lca 4
    #  2 3       right child height 1 lca 3
    # 4          node height 2+1 lca 4
    #
    #   1        left child height 1 lca 2
    # 2   3      right child height 1 lca 3
    #            node height 1+1 lca 1
