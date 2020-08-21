# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.l, self.r = None, None
        def numNodes(root, x):
            if not root:
                return 0 
            l = numNodes(root.left, x)
            r = numNodes(root.right, x)
            if root.val ==x:
                self.l = l
                self.r = r
            return l+r+1
        numNodes(root,x)
        return max(self.l, self.r, n-self.l-self.r-1)>n/2
    
#         Time O(N)
#         Space O(height) for recursion


# There are three "zones" in the tree:

# Left subtree under Red
# Right subtree under Red
# The remainder of the tree "above" Red
# Blue can pick the left child, right child, or parent of Red to control zones 1, 2, or 3, respectivley.

# Therefore we count the number of nodes in two of the zones. The third zone is simply n - sum(the other two zones) -1

# If one of the zones is larger than the other two combined (plus 1 for the Red node), then we (Blue) can control it and win the game. Otherwise we lose :(

