import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 1;
        
        int totalWeight = truck_weights[0];
        Queue<Truck> bridge = new LinkedList<>();
        Queue<Truck> wait = new LinkedList<>();
        
        for (int i : truck_weights) {
            wait.offer(new Truck(i, 0));
        }
        
        bridge.offer(wait.poll());
        
        while (!wait.isEmpty()) {
            
            for (Truck truck : bridge) {
                truck.time++;
            }
            
            if (bridge.peek().time == bridge_length) {
                Truck truck = bridge.poll();
                totalWeight -= truck.weight;
            }
            
            if (bridge.size() <= bridge_length) {
                int nextWeight = totalWeight + wait.peek().weight;
                
                if (nextWeight <= weight) {
                    bridge.add(wait.poll());
                    totalWeight = nextWeight;
                }
            }
            answer++;
        }
        
        return answer + bridge_length;
    }
    
    private class Truck {
        int weight, time;
        
        public Truck(int weight, int time) {
            this.weight = weight;
            this.time = time;
        }
            
    }
}