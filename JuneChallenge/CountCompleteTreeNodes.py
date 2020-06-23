# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack=[]
        ans=[]
        while stack or root:
            #temp=stack.pop()
            if root:
                stack.append(root)
                root=root.left
            else:
                temp=stack.pop()
                ans.append(temp.val)
                root=temp.right
        return len(ans)        
                
                
