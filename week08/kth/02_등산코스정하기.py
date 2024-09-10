# 문제 분석
# 휴식 없이 이동하는 거리intensity가 최소가 되는 경로를 구하라
# 출입구는 시작과 끝이 동일해야 한다.
# 산봉우리는 반드시 한 번만 방문해야 한다.
# 나머지 모든 노드는 쉼터이다.
# paths는 양방향에 대한 정보를 나타낸다.
# intensity가 최소가 되는 경로가 여러 개라면, 번호가 가장 낮은 코스를 선택하라.
# 선택한 코스의 [방문한 산봉우리 노드, intensity 최솟값] return
# 노드가 50,000이므로 플로이드-워셜은 부적합.

# 접근
# 출입구 -> 산봉우리 / 산봉우리 -> 출입구 2번을 구한다. -> 아니다. 하나만 해도 된다.
# 오르는 길에 방문했던 곳을, 내려가는 길에 다시 방문해도 된다.
# 출입구 출발, 경로를 저장하는 다익스트라 (한 점에서 다른 모든 노드로 가는 최단 경로)
    # 경로를 저장할 것도 없다. 현재 탐색의 now_max_intesity를 갱신하면서, 전체 intenisty를 갱신하면 된다.
# 각 출입구에서, 여러가지 경로 중에 산봉우리로 도착하는 것, 그 중에 경로에서 찾은 intensity가 가장 작은 것

import heapq

def dijkstra(gates, graph, n, summits_set):
    INF = int(1e9)
    # 가장 먼저 해당 노드에 도달한 경우. 출입구 ~ 해당 노드까지 intensity
    intensity = [INF] * (n + 1)
    h = []
    
    # 출입구를 시작점으로 하는 초기 설정
    for gate in gates:
        heapq.heappush(h, (0, gate))  # (intensity, node)
        intensity[gate] = 0
    
    while h:
        now_intensity, now = heapq.heappop(h)

        # 현재 비용 > 기록되어 있는 비용이라면 진행X
        if now_intensity > intensity[now]:
            continue
        
        # 산봉우리 노드라면 탐색 중단
        if now in summits_set:
            continue
        
        # 현재 노드와 연결된 노드들 탐색
        for next_intensity, next in graph[now]:
            max_intensity_in_current_path = max(now_intensity, next_intensity) # max_intensity_in_current_path: 현재 탐색 중인 경로의 intensity 중 최댓값
            if intensity[next] > max_intensity_in_current_path: # intensity[node]: 다른 경로를 통해 next에 도달한 경우의 intensity
                intensity[next] = max_intensity_in_current_path # 다른 경로보다 현재 경로가 효율적인 경우 갱신
                heapq.heappush(h, (max_intensity_in_current_path, next))
    
    return intensity

def solution(n, paths, gates, summits):
    # 인접 리스트 형태로 그래프 만들기
    graph = [[] for _ in range(n + 1)]
    for path in paths:
        a, b, c = path
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    summits_set = set(summits)  # in 연산 시간 감소를 위해
    
    # 출입구에서 시작하는 다익스트라 알고리즘 실행
    intensity = dijkstra(gates, graph, n, summits_set)
    
    # 산봉우리 중에서 intensity가 최소인 산봉우리 찾기
    answer_summit = -1
    answer_intensity = int(1e9)
    
    for summit in sorted(summits):
        if intensity[summit] < answer_intensity:
            answer_intensity = intensity[summit]
            answer_summit = summit
    
    return [answer_summit, answer_intensity]


n = 7
paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
gates = [1]
summits = [2, 3, 4]
print(solution(n, paths, gates, summits))
