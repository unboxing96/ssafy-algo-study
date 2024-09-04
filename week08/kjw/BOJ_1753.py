import heapq

INF = int(1e9)
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)  # 최단거리 저장할 리스트

for _ in range(e):  # 간선의 개수만큼 정보
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a에서 b로가는 가중치c인 경로


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # start에서 start로 가는길은 길이가 0
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]  # now 노드에서 i[0]노드까지 가는데 드는 비용
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])