import heapq
def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    INF = int(1e9)
    for path in paths:
        a, b, c = path[0], path[1], path[2]
        graph[a].append((b, c))
        graph[b].append((a, c))

    summits = set(summits) # in함수 쓸 때 탐색 빠르게 하기 위하여

    def dijkstra():
        intensity = [INF] * (n+1)
        q = []
        for i in gates:
            intensity[i] = 0
            heapq.heappush(q, (0, i))
        while q:
            current_intensity, current = heapq.heappop(q)
            if current in summits:
                continue
            if current_intensity > intensity[current]:
                continue
            # 이거땜에 인덱스 오류가 났네요 이거 왜 나지??? 이해안됨 ! 리뷰어님 부탁드려요
            # for i in graph[current]:
            #     max_intensity = max(i[0], current_intensity)
            #     if intensity[i[1]] > max_intensity:
            #         intensity[i[1]] = max_intensity
            #         heapq.heappush(q, (max_intensity, i[1]))
            for next_node, path_intensity in graph[current]:
                max_intensity = max(current_intensity, path_intensity)
                if intensity[next_node] > max_intensity:
                    intensity[next_node] = max_intensity
                    heapq.heappush(q, (max_intensity, next_node))
        return intensity

    intensity = dijkstra()

    top_point = 0
    min_intensity = INF
    for top in summits:
        if intensity[top] < min_intensity:
            min_intensity = intensity[top]
            top_point = top
        elif intensity[top] == min_intensity:
            top_point = min(top, top_point)
    return [top_point, min_intensity]
