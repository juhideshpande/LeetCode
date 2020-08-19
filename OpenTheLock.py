class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead_set = set(deadends) #runs without using set but takes more time
        queue = collections.deque([('0000', 0)])
        visited = set('0000')

        while queue:
            (string, steps) = queue.popleft()
            if string == target:
                return steps
            elif string in dead_set:
                continue
            for i in range(4):
                digit = int(string[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_string = string[:i]+str(new_digit)+string[i+1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append((new_string, steps+1))
        return -1
    
    #Time complexity: O(N**2 * A**N + D) where A is the number of digits in our alphabet, N is the number of digits in the lock, and D is the size of deadends
    #Space Complexity : O( A**N + D)for the queue and the set dead_set.
