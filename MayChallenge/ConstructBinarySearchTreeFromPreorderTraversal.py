# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        inorder=sorted(preorder)
        return self.helper(preorder,inorder)
    
    def helper(self,preorder,inorder):
        lenpre=len(preorder)
        lenin=len(inorder)
        
        if lenpre!=lenin or lenpre==0 or inorder==None or preorder==None:
            return None
        
        root =TreeNode(preorder[0])
        rootindex=inorder.index(root.val)
        
        root.left=self.helper(preorder[1:rootindex+1],inorder[:rootindex])
        root.right=self.helper(preorder[rootindex+1:],inorder[rootindex+1:])
        
        return root
