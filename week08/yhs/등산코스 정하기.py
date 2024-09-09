import heapq


def solution(n, paths, gates, summits):
    INF = 1E9
    answer = [INF, INF]     # answer 배열 초기화

    intensity_info = [[] for _ in range(n + 1)]     # i번째 인덱스의 list가 [j, k]일 때 : i번 지점에서 j번 지점으로 가는 코스의 intensity가 k
    for path in paths:
        intensity_info[path[0]].append([path[1], path[2]])
        intensity_info[path[1]].append([path[0], path[2]])

    q = []                              # 우선순위 큐
    for gate in gates:                  # 모든 gates 우선순위 큐에 삽입
        heapq.heappush(q, [0, gate])

    intensities = [INF] * (n + 1)  # Dijkstra 통해 생성할 list : 출입구 ~ i번째 지점까지의 최소 intensity
    visited = [False] * (n + 1)  # 방문 확인용 list

    summits = set(summits)  # 시간복잡도 줄이기 위해 summits을 set로 변환
    while q:
        intensity, now = heapq.heappop(q)

        # 현재 탐색중인 노드가 이미 처리된 노드이거나 산봉우리일 때 : skip
        if visited[now] or now in summits:
            continue
        visited[now] = True

        for key in intensity_info[now]:     # 모든 연결노드 탐색
            destination = key[0]
            cost = max(key[1], intensity)   # now까지의 intensity와 now ~ destination의 intensity 중 더 큰 값이 새로운 intensity

            if cost < intensities[destination]:     # intensity 갱신
                intensities[destination] = cost
                heapq.heappush(q, [cost, destination])

    # intensity가 최소인 등산코스 찾기
    for summit in summits:
        if answer[1] > intensities[summit]:                             # intensity가 작은 경우 : 해당 등산코스 선택
            answer[1] = intensities[summit]
            answer[0] = summit
        elif answer[1] == intensities[summit] and summit < answer[0]:   # intensity가 같은 경우 : 번호가 낮은 산봉우리의 등산코스 선택
            answer[1] = intensities[summit]
            answer[0] = summit

    return answer


# a, b, c, d = 6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]
# a, b, c, d = 7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]
# a, b, c, d = 7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]
a, b, c, d = 5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]
print(solution(a, b, c, d))
