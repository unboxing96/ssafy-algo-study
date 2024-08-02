#2606 바이러스

import sys
sys.stdin = open('2606_input.txt')

N = int(input()) # 컴퓨터의 수 (노드 수)
M = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수 (아마 간선 수?)

graph = [[] for _ in range(N+1)] # 인접 리스트

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# print(graph)

v = 1 #1번 컴퓨터가 웜바이러스의 숙주!!

# BFS
visited = [False] * (N+1)

from collections import deque

queue = deque([v])
visited[v] = True

count = 0 # 웜 바이러스에 걸리게 되는 컴퓨터의 수

while queue:
    v = queue.popleft()
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            count+= 1
    
print(count)
