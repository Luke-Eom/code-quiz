import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> queue = new LinkedList<>();
        List<Integer> list = new ArrayList<>();
       
        
        for (int i = 0; i < progresses.length; i++) {
            int work = 100 - progresses[i];
            
            if (work % speeds[i] == 0) {
                queue.add(work / speeds[i]);
            }
            else {
                queue.add(work / speeds[i] + 1);
            }
        }
        
        while (!queue.isEmpty()) {
            int count = 1;
            int day = queue.poll();
            
            while (!queue.isEmpty() && day >= queue.peek()) {
                count++;
                queue.poll();
            }
            
            list.add(count);
        }
        
        int[] answer = new int[list.size()];
        
        for (int i = 0; i < answer.length; i++) {
            answer[i]= list.get(i);
        }
        
        return answer;
    }
}