# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        s = [root]
        res = 0
        while s:
            tmp = s.pop()
            if tmp.left:
                s.append(tmp.left)
                if not tmp.left.left and not tmp.left.right:
                    res += tmp.left.val
            if tmp.right:
                s.append(tmp.right)
        return res
