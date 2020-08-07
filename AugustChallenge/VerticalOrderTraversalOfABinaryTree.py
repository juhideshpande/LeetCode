# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        frontier = [(root, 0)]
        h = collections.defaultdict(list)
        while frontier:
            temp = []
            for u, x in frontier:
                h[x].append(u.val)
                if u.left: 
                    temp.append((u.left, x-1)) 
                if u.right: 
                    temp.append((u.right, x+1))
                #print("before sort",temp)    
                temp.sort(key = lambda x: (x[1], x[0].val))
               # print("after sort",temp)
            frontier = temp
      #  print(h,"dict")   
      #  print("sorted h",sorted(h))
        for k in sorted(h):
            res.append(h[k])
        return res
