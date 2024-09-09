from heapq import heappush, heappop

def solution(n, paths, gates, summits): # gates 출입구, summits 산봉우리
    INF = int(1e9)
    distance = [INF] * (n+1)

    graph = [[] for _ in range(n+1)]
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))

    min_intensity = int(1e9)
    summit_num = 0

    summits.sort()

    for summit in summits: # 도착점
        for gate in gates:  # 츌발점
            q = []
            heappush(q, (0, gate))
            distance[gate] = 0
            # tmp = 0
            while q: # 큐가 빌 때 까지
                dist, now = heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기

                if now in summits:
                    continue

                if dist > distance[now]:#현재 노드가 이미 처리된 적 있는 노드라면 무시
                    continue

                for i in graph[now]:  # 현재 노드와 연결된 다른 인접한 노드들을 확인
                    tmp = max(dist, i[1])

                    if i[0] not in gates: #다른 출입구 방문하면 안 됨
                        if tmp < distance[i[0]]:
                            distance[i[0]] = tmp
                            heappush(q, (tmp, i[0]))

        if distance[summit] < min_intensity:
            min_intensity = distance[summit]
            summit_num = summit

    return [summit_num, min_intensity] # [산봉우리의 번호, intensity의 최솟값]

paths = [[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
         [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]	,
         [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]	,
         [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]	]

print(solution(6, paths[0], [1, 3], [5])) # [5, 3]
print(solution(7, paths[1], [1], [2, 3, 4])) # [3, 4]
print(solution(7, paths[2], [3, 7], [1, 5])) # [5, 1]
print(solution(5, paths[3], [1, 2], [5])) # [5, 6]
