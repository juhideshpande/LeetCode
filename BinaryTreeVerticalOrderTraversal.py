# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        res = []
        frontier =collections.deque( [(root, 0)])
        h = collections.defaultdict(list)
        while frontier:
            u,x=frontier.popleft()
            h[x].append(u.val)
            if u.left: 
                frontier.append((u.left, x-1)) 
            if u.right: 
                frontier.append((u.right, x+1))
              
        for k in sorted(h):
            res.append(h[k])
        return res
