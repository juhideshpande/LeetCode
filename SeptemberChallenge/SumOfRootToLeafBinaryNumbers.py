# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [(root, root.val)]
        res = 0
        while stack:
            root, val = stack.pop(0)
            if root.left:
                stack.append((root.left, val*2+root.left.val))
            if root.right:
                stack.append((root.right, val*2+root.right.val))
            if not root.left and not root.right:
                res += val
        return res
