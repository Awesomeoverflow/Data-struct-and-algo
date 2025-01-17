class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x != 0 && x % 10 == 0)) {
            return false;
        }
        double rev=0;
        int cpo=x;
        while(cpo!=0){
            rev=(rev*10)+(cpo%10);
            cpo=cpo/10;

        }
        if(rev==x){
            return true;
        }
        else{
            return false;
        }
    }
};