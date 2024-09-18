import sys
sys.stdin = open('input.txt')


"""
매일 서울에서 포천까지 출퇴근 진행.
돈이 많대... 부럽다,,, 나도 10억만,,...
K개의 도로를 포장해서 서울 -> 포천 단축.. (차라리 집을 사..)

N개의 도시 > 최소시간 k이하의 도로 포장
이미 있는 도로만 포장 가능. > 걸리는 시간 0 
서울은 1 포천은 n번

1 ~ n번까지 항상 갈 수 있는 데이터만 주어짐.
# 최소 비용구하기? 다익스트라.
INF = float('inf') 하면 pass고 1e9하면 실패.
"""

import heapq
INF = float('inf')

# 도시의 수 / 도로의 수 / 포장할 도로의 수
city_cnt, road_cnt, pave_cnt = map(int,input().split())
# 도로의 수에 대해 도로가 연결하는 두 도시와 도로 통과 걸리는 시간 주어짐. 양방
# 1 2 10이면 / 1번도로에서 > 2번도로로 가는데 10의 시간(비용)이 듦.

# pave 이하의 도로를 포장하여 얻을 수 있는 최소 시간 출력.

# 비용 담을 리스트, # 노드에 연결된 정보 담을 리스트
graph = [[]for i in range(city_cnt+1)]
distance = [[INF] * (pave_cnt + 1) for _ in range(city_cnt+1)]
# 최댄 거리 테이블


for _ in range(road_cnt):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start, 0))
    distance[start][0] = 0

    while q:
        dist, now, count = heapq.heappop(q)

        if distance[now][count] < dist:
            continue

        for next, weight in graph[now]:
            cost = dist + weight

            # 포장하지 않았을때
            if cost < distance[next][count]:
                distance[next][count] = cost
                heapq.heappush(q, (cost, next, count))
            # 포장하면
            if count < pave_cnt and dist < distance[next][count+1]:
                distance[next][count+1] = dist
                heapq.heappush(q, (dist, next, count+1))

dijkstra(1)

print(min(distance[city_cnt]))