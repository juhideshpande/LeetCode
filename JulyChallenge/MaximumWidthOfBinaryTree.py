# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        maxwidth=0
        q=collections.deque()
        q.append((root,0))
        while q:
            #print(q[-1][1],q[0][1])
            maxwidth=max(maxwidth,q[-1][1]-q[0][1]+1)
            n=len(q)
            for i in range(n):
                cur,idx=q.popleft()
                if cur.left:
                    q.append((cur.left,2*idx))
                if cur.right:
                    q.append((cur.right,2*idx+1))

        return maxwidth    
