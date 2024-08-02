# 문제분석
# 1번 노드와 연결된 노드의 개수를 return 하라

# from collections import deque

def dfs(v, cnt):
    visited[v] = True

    for next_node in graph[v]:
        if not visited[next_node]:
            cnt = dfs(next_node, cnt + 1)
    
    return cnt 

# def bfs(v):
#     q = deque([v])
#     visited[v] = False
#     cnt = 0

#     while q:
#         x = q.popleft()
#         for next_node in graph[x]:
#             if visited[next_node]:
#                 visited[next_node] = False
#                 q.append(next_node)
#                 cnt += 1
    
#     return cnt
    

n = int(input()) # 노드의 개수
m = int(input()) # 연결 정보의 개수
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result1 = dfs(1, 0)
print(result1)

# result2 = bfs(1)
# print(result2)