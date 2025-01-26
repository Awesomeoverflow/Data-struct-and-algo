class Solution:
    def merge(self, inter: List[List[int]]) -> List[List[int]]:
        inter = sorted(inter, key=lambda x: (x[0], x[1]))
        merg=[]
        i=0
        n=len(inter)
        mergp=-1

        for i in range(0,n):
            if mergp==-1:
                merg.append(inter[i])
                mergp+=1
            elif merg[mergp][1]>=inter[i][0] and merg[mergp][1]>=inter[i][1]:
                continue
            elif merg[mergp][1]>=inter[i][0] and merg[mergp][1]<inter[i][1]:
                merg[mergp][1]=inter[i][1]
            elif merg[mergp][1]<inter[i][0]:
                merg.append(inter[i])
                mergp+=1

        return merg 
            
        


            



        