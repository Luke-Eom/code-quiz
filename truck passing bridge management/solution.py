from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridgeWeight = 0 
    waiting = deque(truck_weights) # deque (= que in python)
    bridge = deque([0 for _ in range(bridge_length)]) # 다리 길이만큼 0으로 채운다.
    
    while len(waiting) or bridgeWeight > 0: 
        removedTruck = bridge.popleft() 
        bridgeWeight -= removedTruck
        
        if len(waiting) and bridgeWeight + waiting[0] <= weight:
            newTruck = waiting.popleft()
            bridgeWeight += newTruck
            
            bridge.append(newTruck) 
            
        else: 
            bridge.append(0)
            
        time += 1
    return time