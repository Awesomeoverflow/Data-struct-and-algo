class Solution {
public:
    int reverse(int x) {
        bool if_neg= false ;
        if(x>=pow(2,31)-1 || x<=-(pow(2,31))){
            return 0;
        }
        if(x<0){
            x=x*-1;
            if_neg= true;
        }
        double res=0;

        while(x!=0){
            res=(res*10)+(x%10);
            x=x/10;
        }
        if(if_neg){
            res=res*-1;
        }
        if(res>=pow(2,31)-1 || res<=(-1)*(pow(2,31))){
            return 0;
        }
        return res;
    }
};