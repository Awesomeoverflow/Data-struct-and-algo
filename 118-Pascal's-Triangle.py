class Solution:
    def generate(self, n: int) -> List[List[int]]:
        pt=[] 
        for i in range(0,n):
            arr=[]
            for j in range(0,i+1):    
                if j==i or j==0:
                    arr.append(1)
                else :
                    a=pt[i-1][j-1]+pt[i-1][j]
                    arr.append(a)
            pt.append(arr)
        return pt





        