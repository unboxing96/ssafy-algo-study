import sys
sys.stdin = open("03_1162_도로포장.txt")

# 문제 분석
# 1번 노드에서 N번 노드까지 최단 경로 -> 다익스트라
# 최대 k개까지, 입력값으로 주어지는 도로의 비용을 0으로 변경할 수 있다.
# 이때 N번 노드까지 도달하는 최소 시간을 구하라.

# 접근
# 완전 탐색으로 구하면 . . . 최대 50,000 ** 20 -> 시간초과
# 그렇게 해보자 . . . 마치 배낭 문제처럼

# 다익스트라는 한 점에서 다른 모든 점까지 최단 경로를 구한다. 그것을 으레 distance에 기록한다.
# distance의 각 인덱스를 k개 만큼 확장한다.
# distance = [[INF] * (k + 1) for _ in range(n + 1)]
# 각 열은 도로 포장을 i번 했을 떄, 1번 노드부터 해당 노드까지 최단 거리를 기록한다.

# 다익스트라를 진행하며
# 현재 포장 수가 k보다 작은 경우에는, 포장하는 경우와 포장하지 않는 경우를 모두 힙큐에 넣는다.
# k 이상인 경우에는 포장하지 않는 경우만 힙큐에 넣는다.
# 탐색이 완료되면 min(distance[n])을 return 한다.

# 시간 초과
# 간선 수가 5 * 10 ** 4이고 가중치는 10 ** 6이므로, 최대 값은 5 * 10 ** 10
# INF를 int(1e9)로 설정하면 특정 경로를 아예 확인하지 않는 문제가 생긴다.

import heapq

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start, 0)) # cost, node, wrap_up_cnt
    distance[start][0] = 0

    while hq:
        now_cost, now, wrap_up_cnt = heapq.heappop(hq)
        if now_cost > distance[now][wrap_up_cnt]:
            continue
        for next_cost, next in graph[now]:
            new_cost = now_cost + next_cost
            # 포장X
            if distance[next][wrap_up_cnt] > new_cost:
                distance[next][wrap_up_cnt] = new_cost
                heapq.heappush(hq, (new_cost, next, wrap_up_cnt))
            # 포장O
            # 포장하는 경우 다음 노드 이동 비용이 0 -> now_cost를 그대로 사용
            if wrap_up_cnt < k and distance[next][wrap_up_cnt + 1] > now_cost:
                distance[next][wrap_up_cnt + 1] = now_cost
                heapq.heappush(hq, (now_cost, next, wrap_up_cnt + 1))


INF = int(5 * 1e10 + 1) # 최대로 가능한 값보다 1크게
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a)) # 양방향 그래프

distance = [[INF] * (k + 1) for _ in range(n + 1)]

dijkstra(1)
print(min(distance[n]))