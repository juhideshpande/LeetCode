# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        lenin=len(inorder)
        lenpos=len(postorder)
        
        
          #len-1
        
        if lenin!=lenpos or inorder==None or postorder==None or lenin==0 or lenpos==0:
            return None
        
        root=TreeNode(postorder[-1])
        rootindex=inorder.index(root.val)
        
        root.left=self.buildTree(inorder[:rootindex],postorder[:rootindex])
        root.right=self.buildTree(inorder[rootindex+1:],postorder[rootindex:lenpos-1])
        
        return root
