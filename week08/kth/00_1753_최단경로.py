import sys
sys.stdin = open("00_1753_최단경로.txt")

import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        now_dist, now = heapq.heappop(q)

        # 현재 노드의 비용 > 최단 거리 테이블에 기록된 비용 -> 탐색할 필요가 없다.
        if now_dist > distance[now]:
            continue
        
        # 모든 노드의 인접 노드를 확인하며, 최단 거리 테이블 모두 갱신
        for next_dist, next in graph[now]:
            cost = distance[now] + next_dist # now -> next로 거쳐가는 비용이
            if cost < distance[next]: # next에 갱신된 비용보다 작다면
                distance[next] = cost # 해당 비용으로 갱신
                heapq.heappush(q, (cost, next))

# def dijkstra(start):
#     visited[start] = 1 # 방문 처리
#     distance[start] = 0 # 초기화

#     for dist, start in graph[start]: # 현재 노드와 연결된 정보로 초기화
#         distance[start] = dist
    
#     for i in range(v - 1): # n - 1까지 하면 마지막 노드는 이미 갱신되어 있음
#         now = find_smallest_node() # 최단 거리가 가장 작은 노드
#         visited[now] = 1 # 방문 처리
#         for next_dist, next in graph[now]:
#             cost = distance[now] + next_dist
#             if distance[next] > cost:
#                 distance[next] = cost


# def find_smallest_node():
#     min_value = INF
#     min_idx = 0
#     for i in range(1, v + 1):
#         if min_value > distance[i] and not visited[i]:
#             min_value = distance[i]
#             min_idx = i
    
#     return min_idx



INF = int(1e9)
v, e = map(int, input().split())
start = int(input())
distance = [INF] * (v + 1)
visited = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b)) # 노드 번호, 비용

dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])