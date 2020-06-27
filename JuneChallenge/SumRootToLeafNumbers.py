# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, prev):
            if not root:
                return
            elif not root.left and not root.right:
                self.res += prev * 10 + root.val
            prev = 10 * prev + root.val
            dfs(root.left, prev)
            dfs(root.right, prev)
            
        self.res = 0
        dfs(root, 0)
        return self.res
