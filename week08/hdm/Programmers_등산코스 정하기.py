import heapq

INF = int(1e9)

""""
산봉우리에서 휴식 가능.
휴식 없이 이동해야하는 시간 중 가장 긴 시간을 해당하는 등산 코스는 intensity

intensity가 최소가 되는 등산 코스에 포함된 산봉우리 번호 + 최솟값을 정수에 담아 return
intensity가 최소가 되는 등산 코스가 여러개면, 산봉우리의 번호가 가장 낮은 등산코스를 선택

*
point
1. 결과적으로 필요한건 최소가격으로 봉우리를 다녀오는것.
2. 최소가격 루트 중 max price를 저장하면됨.
3. 최소 합 가격이 같은 루트가 있다면 봉우리가 낮은 숫자를 return 하면됨.

"""

# n : 지점수
# paths : 등산로 정보 담은 2차원 배열 [i,j,w]
# i 번지점과 j번지점을 연결하는 등산로 w만큼 걸림.

# gatees: 출입구들의 번호가 담긴 정수 배열
# summits: 산 봉우리들의 번호가 담긴 정수 배열

def solution(n, paths, gates, summits):
    # 각 노드에 있는 정보를 담는 리스트 만들기
    graph = [[] for _ in range(n+1)]
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
    distance = [INF] * (n + 1)  # 최단거리 테이블 모두 무한 초기화

    for path in paths:
        a, b, c = path
        graph[a].append((b, c))
        graph[b].append((a, c))

    gates_set = set(gates) # set으로 한 이유: 특정 노드 확인하려고
    summits_set = set(summits)


    # 현재 start에서 최단거리를 돌 수 있는 것들임.
    # def dijkstra(start):
    q = []
    for gate in gates:  # 시작 노드로 가기 위한 최단 경로를 0 으로 설정하여 큐에 삽입.
        heapq.heappush(q, (0, gate)) # 출발지점 우선순위에 넣고
        distance[gate] = 0 # 현지 비용 0원 넣기

    while q:  # q가비지 않으면,
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드에 대한 정보 뽑기

        # 현재 경로가 이미 계산된 경로보다 크면 무시
        if dist > distance[now]:
            continue

        # 만약 현재 노드가 봉우리면 탐색 멈추기
        if now in summits_set: # 이미 봉우리에 속해있다면, 더이상 탐색할 필요없으니 종료.
            continue

        for next_node, cost in graph[now]:
            new_cost = max(dist, cost)

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))


    answer_summit = -1 # 최종 봉우리
    answer_intensity = INF # 최종 선택 경로의 intensity 출력

    for summit in sorted(summits): # 봉우리를 작은순으로 뽑아야하니
        if distance[summit] < answer_intensity:
            answer_summit = summit
            answer_intensity = distance[summit]

    return [answer_summit, answer_intensity]


n = 7
paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
gates = [1]
summits = [2, 3, 4]


print(solution(n, paths, gates, summits))
