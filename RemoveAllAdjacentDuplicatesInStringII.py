class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for val in s:
            if stack and stack[-1][0] == val:
                stack.append((val, stack[-1][1] + 1))
            else:
                stack.append((val, 1))
            if stack and stack[-1][1] == k:
                for i in range(k):
                    stack.pop()
        return "".join([x[0] for x in stack])
        
