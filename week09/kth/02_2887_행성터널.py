import sys
sys.stdin = open("2887.txt")

# 문제 분석
# 주어진 노드 N개에 대한 MST를 구하라
# 각 노드는 3차원 좌표로 주어져 있다.
# 연결 비용은 min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
# 입력은 노드 개수 n. n은 100,000 이하.
# n개의 노드 위치 좌표가 주어진다. 각 좌표의 값은 -10^9 ~ 10^9

# 접근
# 노드에 대한 정보가 주어졌으므로 프림 . . .?
# 최소 힙을 사용하는 경우 ElogV의 시간복잡도를 갖는다.
# 그냥 프림으로 구하면 왜 안 될까 ?

# 접근2
# 메모리 초과가 발생한다.
# 사실상 모든 노드 조합을 테스트하므로 힙큐에 N^2개가 들어가는 것이 문제이다.
# 입력을 보면 각 노드의 최소 하나의 좌표가, 다른 노드의 좌표와 맞닿아있다. (인접)
# 애초에 프림 알고리즘이 인접한 노드를 기준으로 이동 가능한 간선을 탐색하는 것이다.
# 이것들만 힙큐에 추가하면 어떨까 ?
# 다시 말해 기존 프림에서 사용했던 a -> cost -> b의 형태로 입력값을 바꿔준다.
    # a 노드를 탐색하는 경우 인접한 노드만 확인하여 힙큐에 추가한다.

# 인접하다는 것은 ?
# 한 노드에는 x, y, z 3개의 축이 있다.
# 각 축마다 인접한 노드가 있을 것이다.
    # 가령 노드 1은 
    # x축을 기준으로 노드 0, 노드 2와 인접할 수 있다.
    # y축을 기준으로 노드 3과 인접할 수 있다.
    # z축을 기준으로 노드 1과 인접할 수 있다.
    # 따라서 하나의 노드는 3개의 축 * 축당 2개의 간선 == 최대 6개의 간선을 갖는다.
# 전체 간선은 몇 개인가 ?
    # 하나의 축은 n-1개의 축과 연결된다.
    # 축은 3개이다.
    # 총 3(n - 1)개의 간선을 탐색하는 것이다.
# 인접리스트의 형태는 ?
    # graph[a] = (cost, b)
    # graph[b] = (cost, a)


import heapq

def prim(start):
    hq = []
    heapq.heappush(hq, (0, start))
    visited = [0] * (n)
    result = 0

    while hq:
        now_cost, now = heapq.heappop(hq)
        if not visited[now]:
            visited[now] = 1
            result += now_cost
        
            for next_cost, next in graph[now]:
                if not visited[next]:
                    heapq.heappush(hq, (next_cost, next))

    return result

n = int(input())
nodes = []
for i in range(n):
    x, y, z = map(int, input().split())
    nodes.append((i, x, y, z)) # 노드 번호, x, y, z


graph = [[] for _ in range(n)]
for i in range(1, 3 + 1): # x, y, z축 탐색
    nodes.sort(key = lambda x : x[i]) # '인접'리스트를 만들기 위해 해당 축으로 정렬
    for j in range(n - 1): # 각 축마다 n - 1개의 인접 축 탐색
        cost = abs(nodes[j + 1][i] - nodes[j][i]) # j번 노드의 i번 축의 값 차이
        a, b = nodes[j][0], nodes[j + 1][0] # 출발 노드, 도착 노드
        graph[a].append((cost, b))
        graph[b].append((cost, a)) # 양방향 그래프

answer = prim(0)
print(answer)