class Node1(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        # self.count is the size of the left-subtree plus number of times val is repeated.
        # No need for dupe here.
        self.count = 1
        return

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        root, counts = None, [0]*N
        for i in range(N-1, -1, -1):
            if root == None:
                root = Node1(nums[i])
                continue
            counts[i] = self.insert(root, nums[i])
        return counts
    
    def insert(self, root, val):
        count = 0
        while True:
            if val <= root.val:
                root.count = root.count + 1
                if root.left == None:
                    root.left = Node1(val)
                    break
                else:
                    root = root.left
            else:
                count = count + root.count
                if root.right == None:
                    root.right = Node1(val)
                    break
                else:
                    root = root.right
        return count
