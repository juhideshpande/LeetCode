class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for chr in s:
            if chr != ']':
                stack.append(chr)
            else:
                temp_s = ''
                while stack:
                    x = stack.pop()
                    if x == '[':
                        n = ''
                        while stack and stack[-1].isdigit():
                            n = stack.pop() + n
                        stack.append(temp_s*int(n))
                        break
                    else:
                        temp_s = x + temp_s
        return ''.join(stack)
       
        #Time and Space=O(1)

