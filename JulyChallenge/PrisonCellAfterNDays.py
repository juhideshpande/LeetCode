class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def next_day(arr):
            temp = [0] * len(arr)
            for i in range(1, len(arr) - 1):
                temp[i] = 1 if arr[i - 1] == arr[i + 1] else 0
            return temp
                
        hashset = set()
        count = 0
        while count < N:
            # print cells, count
            temp = next_day(cells)
            if str(temp) in hashset:
                # print "break"
                break
            else:
                hashset.add(str(temp))
                cells = temp
                count += 1
                
        if count != N:
            # print "inside"
            N = N % count
            for i in range(N):
                cells = next_day(cells)
        
            
        return cells
