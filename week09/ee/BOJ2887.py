# 2887 행성 터널

import sys
from heapq import heappush, heappop
from copy import deepcopy

sys.stdin = open('2887_input.txt')

N = int(input()) # 행성의 개수 N

def prim(s):
    heap = []
    MST = [0] * N

    sum_weight = 0
    heappush(heap, (0, s)) # 가중치, 정점정보

    while heap:
        w, v = heappop(heap) # 현재 시점에서 가중치가 가장 작은 정점

        if MST[v]:
            continue

        MST[v] = 1
        sum_weight += w

        for next_weight, next in graph[v]:
            if MST[next]:
                continue
            heappush(heap, (next_weight, next))

    return sum_weight

planets = []

for i in range(N):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i)) # 행성의 x, y, z 좌표 + 행성 인덱스

# x, y, z 좌표 기준으로 정렬
planets_x = sorted(deepcopy(planets), key=lambda x: x[0])
planets_y = sorted(deepcopy(planets), key=lambda x: x[1])
planets_z = sorted(deepcopy(planets), key=lambda x: x[2])

graph = [[] for _ in range(N)]
for i in range(N-1):
    # x축에 대해 정렬한 인접 행성 그래프에 넣기
    x1, y1, z1, i1 = planets_x[i]
    x2, y2, z2, i2 = planets_x[i+1]
    tmp = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
    graph[i1].append([tmp, i2])
    graph[i2].append([tmp, i1])

    # y축 인접 행성 그래프에 넣기
    x1, y1, z1, i1 = planets_y[i]
    x2, y2, z2, i2 = planets_y[i + 1]
    tmp = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
    graph[i1].append([tmp, i2])
    graph[i2].append([tmp, i1])

    # z축 인접 행성 그래프에 넣기
    x1, y1, z1, i1 = planets_z[i]
    x2, y2, z2, i2 = planets_z[i + 1]
    tmp = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
    graph[i1].append([tmp, i2])
    graph[i2].append([tmp, i1])

result = prim(0)
print(result)