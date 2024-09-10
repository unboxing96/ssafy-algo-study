# baek 1865 웜홀
import sys
sys.stdin = open('input.txt')

"""
백준이는 월드나라의 국민.
N개의 지점이 있고, n개의 지점 사이에는 m개의 도로와 w개의 웜홀 존재. (웜홀 방향 존재)

한지점에서 출발 > 출발위치로 돌아옴> 웜홀을 거쳤니? 묻는거임

시간이 줄어들 수 있기때문에 걸리는 시간1이 줄어드는시간 8로인해서 - 음수가 될수도있음> 벨만포드 써야함. 다익스트라X
출발시점보다 시간이 되돌아가면 yes 안되면 no

"""
# 벨만포드 개선된 버전인 SPFA 사용해야 풀림.  (Shortest Path Faster Algorithm)
# 1. 우선순위 큐 사용.
# 2. 효율적 업데이트

from collections import deque

INF = int(1e9)  # 무한대값 설정

def spfa(vertices, edges, start):
    # 시작 정점에서 모든 정점까지의 거리를 INF로 초기화
    distance = {vertex: INF for vertex in vertices}
    in_queue = {vertex: False for vertex in vertices}  # 큐 안에 있는지 여부
    count = {vertex: 0 for vertex in vertices}  # 각 정점이 큐에 들어간 횟수

    distance[start] = 0
    queue = deque([start])
    in_queue[start] = True

    while queue:
        u = queue.popleft()
        in_queue[u] = False

        for v, weight in edges[u]:
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight

                # 음수 사이클 확인: 정점이 V번 이상 큐에 들어가면 음수 사이클
                count[v] += 1
                if count[v] >= len(vertices):
                    return True  # 음수 사이클 발견

                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True

    return False

T = int(input())  # 테스트 케이스 수 입력

for _ in range(T):
    node, road, W = map(int, input().split())  # 지점의 수, 도로 수, 웜홀 수

    # 간선 정보 초기화
    edges = {i: [] for i in range(1, node + 1)}

    # 도로 정보 입력
    for _ in range(road):
        s, e, t = map(int, input().split())
        edges[s].append((e, t))  # 양방향 도로
        edges[e].append((s, t))  # 반대 방향 추가

    # 웜홀 정보 입력
    for _ in range(W):
        s, e, t = map(int, input().split())
        edges[s].append((e, -t))  # 웜홀은 단방향 (음의 가중치)

    vertices = list(range(1, node + 1))  # 노드 리스트 생성

    # 모든 정점에 대해 SPFA를 실행하여 음수 사이클을 확인
    found_negative_cycle = False
    for i in range(1, node + 1):
        if spfa(vertices, edges, i):
            found_negative_cycle = True
            break

    if found_negative_cycle:
        print('YES')
    else:
        print('NO')



# INF = int(1e9) # 무한대값 설정
#
# def bellman_ford(vertices, edges, start):
#     # 시작 정점에서 모든 정점까지의 거리를 INF로 초기화.
#     distance = {}
#     for vertex in vertices:
#         distance[vertex] = INF
#
#     distance[start] = 0
#
#     # 모든 엣지에 대해서 릴렉스 수행
#     for _ in range(len(vertices) - 1):
#         for u, v, weight in edges:
#             if distance[u] != INF and distance[u] + weight < distance[v]:
#                 distance[v] = distance[u] + weight
#
#     # 음수 사이클 체크
#     for u, v, weight in edges:
#         if distance[u] != INF and distance[u] + weight < distance[v]:
#             return True  # 음수 사이클 발견
#
#     return False
#
# T = int(input())
#
# for tc in range(1, T+1):
#     node, road, W = map(int, input().split()) # 지점의 수
#
#     road_list = [list(map(int, input().split())) for _ in range(road)]
#     # s, e는 연결된 지점의 번호 t는 이동시간
#     whole_list = [list(map(int, input().split())) for _ in range(W)] #  S, E, T
#     # S: 시작점 E: 도착점 T: 줄어드는 시간
#     vertices = list(range(1, node + 1)) # 노드 만들어주기. 각 정점의 초기 거리값 설정 가능.
#
#     # 간선을 만들어줘야 함
#     edges =[]
#
#     for s, e, t in road_list:
#         edges.append((s, e, t))
#         edges.append((e, s, t))
#
#     for s, e, t in whole_list:
#         edges.append((s, e, -t))
#
#     if bellman_ford(vertices, edges, 1):
#         print('YES')
#     else:
#         print('NO')