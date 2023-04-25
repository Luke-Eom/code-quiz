package 멀쩡한정사각형;

class Solution {
    public long solution(int w, int h) {
        long answer = 0;
        long weight = (long)w;
        long height = (long)h;
        
        long num=gcd(weight,height);
        
        answer = weight*height-(weight+height-num);
        return answer;
    }
    
    public long gcd(long x, long y){
        long a = Math.max(x,y);
        long b = Math.min(x,y);
        long temp = 0;
        
        while (b > 0) {
            temp = a % b;
            a = b;
            b = temp;
        }
        
        return a;
    }
}
