class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_index=[]
        for i in range(0,len(matrix)):
            for j in range(0,len((matrix[i]))):
                if matrix[i][j]==0:
                    zero_index.append([i,j])
        for i, j in zero_index:
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
            for k in range(len(matrix)):
                matrix[k][j] = 0
        
        

