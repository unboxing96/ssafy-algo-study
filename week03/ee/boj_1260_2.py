#########태현님이 내 준 과제###########
# 인접 행렬 말고 인접 리스트로 해 보기
# 방문 처리 리스트 하나만 써서 해 보기
#######################################

N, M, v = map(int, input().split()) # N: 노드 개수, M: 간선 개수, V: 시작 노드

datas = [list(map(int, input().split())) for _ in range(M)] # 간선이 연결하는 두 노드의 번호

# 인접 리스트 만들기
def adjacency_list(datas, N):
    matrix = [[] for _ in range(N+1)]

    for data in datas:
        i, j = data
        matrix[i].append(j)
        matrix[j].append(i)
        
    return matrix

graph = adjacency_list(datas, N)
print(graph)

visited = [False] * (N+1)

# DFS
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, v, visited)

from collections import deque

# BFS
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = False
    print(v, end = ' ')
