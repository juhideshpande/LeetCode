# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack=[]
        ans=[]
        
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                tmp=stack.pop()
                ans.append(tmp.val)
                root=tmp.right
        return ans[k-1]            
