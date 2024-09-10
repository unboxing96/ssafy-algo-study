import heapq


def solution(n, s, a, b, fares):
    answer = 1e9
    fare_dict = dict()

    for info in fares:                          # fares 배열에서 주어진 경로 정보로 dictionary 만들기
        start, end, fare = info
        if fare_dict.get(start):
            fare_dict[start].append([end, fare])
        else:
            fare_dict[start] = [[end, fare]]

        if fare_dict.get(end):
            fare_dict[end].append([start, fare])
        else:
            fare_dict[end] = [[start, fare]]

    for i in range(1, n + 1):                   # 자기 자신에서 자기 자신으로 가는 간선 정보도 추가
        if fare_dict.get(i):
            fare_dict[i].append([i, 0])
        else:
            fare_dict[i] = [[i, 0]]

    s_dist = dijkstra(n, s, fare_dict)          # s가 시작점일 때 최단거리 배열

    for key in fare_dict.keys():                # key 노드까지 합승할 때 최단거리 갱신하기
        new_dist = dijkstra(n, key, fare_dict)
        tmp = s_dist[key] + new_dist[a] + new_dist[b]
        if tmp < answer:
            answer = tmp

    return answer


def dijkstra(n, start, fare_dict):
    INF = 1e9
    distance = [INF] * (n + 1)

    q = []
    heapq.heappush(q, [0, start])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in fare_dict[now]:
            # print(i)
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

    return distance