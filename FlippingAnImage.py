class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
		i, j = 0, len(row) - 1
		while i <= j:
			if row[i] == row[j]:
				row[i], row[j] = row[i]^1, row[j]^1
			i += 1
			j -= 1
	return A
