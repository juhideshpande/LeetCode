# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        new_node = TreeNode(val)

        if not root:
             return new_node

        curr = root
        while True:
            if curr.val > val:
                if not curr.left:
                    curr.left = new_node
                    break
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = new_node
                    break
                else:
                    curr = curr.right
        return root
