from collections import deque # 큐를 사용하기 위한 collections library 사용

n, m, v = map(int,input().split()) # n, m, v에 대한 입력을 받음
graph = [[] for _ in range(n+1)] # n+1개의 graph list 공간을 만듬 (0번째 list는 1부터 시작하는 것을 유도하기 위해서 추가)

for i in range(m): # m개의 간선에 대해서,
    temp_list = list(map(int,input().split())) # 간선의 정보 입력
    graph[temp_list[0]].append(temp_list[1]) # 0 은 시작, 1은 종결
    graph[temp_list[1]].append(temp_list[0]) # 양방향임으로 서로 저장

for i in range(n+1): # 작은 것을 먼저 방문 함으로, 
    graph[i].sort() # 각 간선의 정보에서 sorting을 해줌

def dfs(graph,v,visited): # DFS 선언
    visited[v] = True
    print(v, end= ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited): # BFS 선언
    queue = deque([start])

    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False]*(n+1) # 방문 여부 표시
dfs(graph,v,visited) # DFS 실행
print() # 줄바꿈
visited = [False]*(n+1) # 방문 여부 표시
bfs(graph,v,visited) # BFS 실행