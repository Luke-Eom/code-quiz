# BFS
from collections import deque
N = int(input()) # 컴퓨터 수 
M = int(input()) # 컴퓨터 연결 수 

graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0]*(N+1)

def BFS(V):
    queue = deque()
    queue.append(V)
    visited[V] = 1
    cnt = 0

    while queue:
        V = queue.popleft()
        for i in range(1, N+1):
            if graph[V][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                cnt += 1
    return cnt
print(BFS(1))

# DFS

n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
seen = [0] * (n+1)

for _ in range(m):
	a,b = map(int, input().split())
	graph[a][b] = graph[b][a] = 1
    
result = []
def dfs(v):
	seen[v] = 11
    	for i in range(1, n+1):
    		if graph[v][i] == 1 and seen[i] == 0:
        	result.append(i)
        	dfs(i)
        
	return len(result)
    
print(dfs(1))