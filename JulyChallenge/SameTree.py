# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stackp=[p]
        stackq=[q]
        
        while stackp or stackq:
            nodep=stackp.pop()
            nodeq=stackq.pop()
            
            if not nodep and not nodeq:
                continue
            if not nodep or not nodeq or nodeq.val!=nodep.val:
                return False
            else:
                stackp.append(nodep.left)
                stackp.append(nodep.right)
                stackq.append(nodeq.left)
                stackq.append(nodeq.right)
        return True    
