class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1.0

        nn=abs(n)
        while nn!=0:
            if nn%2==1:
                ans=ans*x
                nn=nn-1
            else :
                x=x*x
                nn=nn//2
        if n>0 : return ans
        else : return 1/ans
