# 도로포장

import sys
N, M, K = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

INF = int(1e90)
# distance = [INF] * (N+1)
distance = [[INF] * (K+1) for _ in range(N+1)]
"""
도로 K개를 포장 
1개를 포장했을 때.. 최소
2개..K개의 최소를 다 계산해야할듯
"""

from heapq import heappush, heappop
def dijkstra(s):
    q = []
    heappush(q, (0, s, 0)) # 가중치, 노드, 포장횟수
    for i in range(K):
        distance[s][i] = 0

    while q:
        dist, now, cnt = heappop(q)
        if distance[now][cnt] < dist:
            continue

        if cnt < K: # 현재 노드와 이어지는 도로를 포장
            for next, cost in graph[now]: # 현재 노드와 이어지는 도로 그래프를 돌면서
                if dist < distance[next][cnt+1]: # 값 업데이트
                    distance[next][cnt+1] = dist
                    heappush(q, (dist, next, cnt+1))
        # else: # 도로 포장하지 않기
        for next, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next][cnt]:
                distance[next][cnt] = new_cost
                heappush(q, (new_cost, next, cnt))

dijkstra(1)
# print(distance)
print(min(distance[N]))