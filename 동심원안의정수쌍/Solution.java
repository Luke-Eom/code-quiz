public class Solution {
    
    public long solution(Integer r1, Integer r2) {
        int answer = 0;

        for(int i = 1; i <= r2; i++) {
            int max = (int) Math.floor(Math.sqrt((long)r2*r2 - (long)i*i));
            int min = (int) Math.floor(Math.sqrt((long)r1*r1 - (long)i*i));

            answer += max - min + 1;

        }

        return answer*4;
    }

}