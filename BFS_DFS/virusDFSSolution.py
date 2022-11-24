#DFS
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

# error fix