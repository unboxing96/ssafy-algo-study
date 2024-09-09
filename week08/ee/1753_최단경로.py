# 최단경로
import sys
from heapq import heappush, heappop

sys.stdin = open('1753_input.txt')

V, E = map(int, sys.stdin.readline().split()) # 정점의 개수 V, 간선의 개수 E
K = int(sys.stdin.readline()) # 시작 정점의 번호 K
distance = [1e9] * (V+1)

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dijkstra(s):
    q = []
    heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
dijkstra(K)

for i in range(1, V+1):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])