# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = pred = None
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
               # y = root
                if x is None:
                    x = pred 
                y=root
            pred = root
            root = root.right
        print(x.val)
        x.val, y.val = y.val, x.val
        
#         Time complexity : O(1) in the best case, and O(N) in the worst case when one of the swapped nodes is a rightmost leaf.
# Space complexity : up to O(H) to keep the stack where H is a tree height.
