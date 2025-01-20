class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ind=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]==0:
                    ind.append([i,j])
        m=len(matrix)
        n=len(matrix[0])
        for k in ind:
            for i in range(0,m):
                matrix[i][k[1]]=0
            for j in range(0,n):
                matrix[k[0]][j]=0
            


                


        
        