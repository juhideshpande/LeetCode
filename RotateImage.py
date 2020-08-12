class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #Transpose and then reverse
        for row in range(len(matrix)):
            for col in range(row,len(matrix[0])):
                matrix[col][row],matrix[row][col]=matrix[row][col],matrix[col][row]
                
        for row in range(len(matrix)):
            for col in range(len(matrix)/2):
                matrix[row][len(matrix)-1-col],matrix[row][col] = matrix[row][col],matrix[row][len(matrix)-1-col]
           
        
        #Substitute for reverse:
#          for row in range(len(matrix[0])):
#             matrix[row].reverse()
                        
