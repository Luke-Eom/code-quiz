from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])
    
    while queue:
        n, i = queue.popleft()
        
        if i < len(numbers)-1:
            i += 1
            queue.append([n+numbers[i], i])
            queue.append([n-numbers[i], i])
            
        else:
            if n == target:
                answer += 1
                
    return answer


# DFS
def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer

def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else: return 0
    else:
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        return answer
        