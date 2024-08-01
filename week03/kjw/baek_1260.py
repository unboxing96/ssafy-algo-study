#DFS
n, m, v = map(int, input().split())
# 계산편하게 하려고 빈 리스트를 하나 만드네.. 그래서 N+1
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# graph에 연결된 정보를 리스트 자료형으로 표현
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    # 재귀적으로 방문
    for j in graph[v]:
        if not visited[j]: # 방문하지 않았다면
            dfs(graph, j, visited)

dfs(graph, v, visited)
print()
visited = [False] * (n+1)
# BFS
from collections import deque # 쓰는이유가 속도가 빨라서..? 
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, v, visited)