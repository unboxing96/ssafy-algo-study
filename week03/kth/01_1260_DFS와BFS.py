import sys
sys.stdin = open("01_1260_DFS와BFS.txt")

from collections import deque

n, m, v = map(int, input().split())
# graph = [[] for _ in range(n + 1)] # 인접 리스트
graph = [[0] * (n + 1) for _ in range(n + 1)] # 인접 행렬
visited = [0] * (n + 1)

# 인접 리스트 ###################################################
# def dfs(v, visited):
#     visited[v] = 1
#     print(v, end=" ")

#     for next_node in graph[v]:
#         if not visited[next_node]:
#             dfs(next_node, visited)

# def bfs(v, visited):
#     q = deque()
#     q.append(v)
#     visited[v] = 0 # DFS와 반대로

#     while q:
#         x = q.popleft()
#         print(x, end=" ")

#         for next_node in graph[x]:
#             if visited[next_node]: # DFS와 반대로 
#                 visited[next_node] = 0 # DFS와 반대로
#                 q.append(next_node)

# # 인접 그래프
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#     graph[a].sort()
#     graph[b].sort()


# 인접 헹렬 ###################################################
def dfs(v, visited):
    visited[v] = 1
    print(v, end=" ")

    for next_node in range(1, n + 1):
        if graph[v][next_node] == 1 and not visited[next_node]:
            dfs(next_node, visited)


def bfs(v, visited):
    q = deque()
    q.append(v)
    visited[v] = 0 # DFS와 반대로

    while q:
        x = q.popleft()
        print(x, end=" ")

        for next_node in range(1, n + 1):
            if graph[x][next_node] == 1 and visited[next_node]:
                visited[next_node] = 0 # DFS와 반대로
                q.append(next_node)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


dfs(v, visited)
print()
bfs(v, visited)

