import sys
import heapq
sys.stdin = open('input.txt')

"""
# 2일차: 프로그래머스 합승 택시 요금

택시비 아낄 수 있는 방법?
4번지점 출발 - A는 6 B는 2번 최저 택시요금?
- s a b
  4 6 2

일단 개선된 다익스트라로 각각의 목적지까지의 최소 요금을 찾아보기.
- 중간 과정에서 동일한 루트로 가는 경로가 있으면 그만큼 제해주면될듯.
    - 최소 cost를 구하는게 목표이니 마지막에 최솟값 찾아주면 될듯
"""



def solution(n, s, a, b, fares):

    INF = int(1e9) # 무한으로 설정
    graph = [[] for _ in range(n+1)]

    for c, d, f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))

    def dijkstra(s): # s 출발지점부터 시작.
        distance = [INF] * (n + 1)  # 최단 거리 테이블 무한으로 초기화
        q = []
        heapq.heappush(q, (0,s)) # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 넣기!
        distance[s] = 0

        while q:
            dist, now = heapq.heappop(q) # 가장 최단거리인 짧은 노드에 대한 정보 dist, now에 넣기

            if distance[now] < dist:
                continue

            for next_node, cost in graph[now]:
                new_cost = dist + cost

                if new_cost < distance[next_node]:
                    distance[next_node] = new_cost
                    heapq.heappush(q, (new_cost, next_node))
        return distance

    distance_from_s = dijkstra(s)
    distance_from_a = dijkstra(a)
    distance_from_b = dijkstra(b)

    min_cost = INF

    for i in range(1, n+1):
        cost = distance_from_s[i] + distance_from_a[i] + distance_from_b[i]
        min_cost = min(min_cost,cost)

    return min_cost



n = int(input()) # 지점의 개수
s = int(input()) # 출발지점
a = int(input()) # a의 도착지점
b = int(input()) # b의 도착지점
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# c , d, f 형태
# c -> d로가는 요금이 f라는 뜻.


print(solution(n, s, a, b, fares))