# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        lenpre=len(preorder)
        lenin=len(inorder)
        
        if lenpre!=lenin or lenpre==0 or lenin==0 or preorder==None or inorder==None:
            return None
        
        root=TreeNode(preorder[0])
        rootindex=inorder.index(root.val)
        
        root.left=self.buildTree(preorder[1:rootindex+1],inorder[:rootindex])
        root.right=self.buildTree(preorder[rootindex+1:],inorder[rootindex+1:])
        
        return root
        
