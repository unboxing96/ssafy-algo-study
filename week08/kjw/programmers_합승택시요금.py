import heapq
def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    for i in fares:
        p, q, r = i[0], i[1], i[2]
        graph[p].append((q, r))
        graph[q].append((p, r))

    def dijkstra(start):
        distance = [INF] * (n + 1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance
    distance_start = dijkstra(s)
    distance_a = dijkstra(a)
    distance_b = dijkstra(b)
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, distance_start[i] + distance_a[i] + distance_b[i])

    return answer