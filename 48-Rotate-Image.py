class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        \\\
        Do not return anything, modify matrix in-place instead.
        \\\
        for i in range(0,len(matrix)-1):
            for j in range(i+1, len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(0,len(matrix)):
            matrix[i].reverse()
        
    
    
        