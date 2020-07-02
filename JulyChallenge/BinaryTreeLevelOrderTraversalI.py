# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        nodes=[]
        queue=collections.deque([root])
        
        while queue:
            level=len(queue)
            l=[]
            
            for i in range (level):
                curr=queue.popleft()
                l.append(curr.val)
                
                
                if curr.left:
                    queue.append(curr.left)
                    
                if curr.right:
                    queue.append(curr.right)
                    
            nodes.append(l) 
            
        return nodes[::-1]    
        
