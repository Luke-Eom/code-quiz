from itertools import permutations
def solution(n):
    a = set()
    for i in range(1, len(n) + 1):
        a |= set(map(int, map(''.join, permutations(list(n), i))))
        
    a -= set(range(0, 2))
    
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(2 * i, max(a) + 1, i))
    
    return len(a)