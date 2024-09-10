import sys
sys.stdin = open("04_1865_벨만포드.txt")

INF = int(1e9)

def bf(start):
    distance[start] = 0
    for i in range(n):  # 노드 개수만큼 반복
        for j in range():  # 각 노드마다 모든 간선 확인
            cur_node, next_node, edge_cost = edges[j]
            # if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost: # 이건 틀리는 이유가 뭘까 ???????
            # 최적화를 위한 것이다.
            # 조건의 의미: 출발 노드에서 도달할 수 없는 노드(distance[cur_node] == INF)에서 다른 노드로 가는 경로는 갱신할 필요가 없다.
            # 음수 사이클이 존재하는 경우, 도달할 수 없던 노드가 도달 가능해질 수 있다.
            # 따라서 모든 조건을 탐색해야 한다.
            if distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == n - 1:  # n번째 노드에서도 갱신이 된다면 -> 음수 순환이 존재하는 것
                    return True
    return False

T = int(input())
for _ in range(1, T + 1):
    n, m, w = map(int, input().split())  # 노드, 간선, 웜홀 개수
    edges = []
    distance = [INF] * (n + 1)

    for _ in range(m):  # 간선
        a, b, c = map(int, input().split())
        edges.append((a, b, c))  # a -> b, 비용: c
        edges.append((b, a, c))  # b -> a, 비용: c (양방향 간선)

    for _ in range(w):  # 웜홀
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))  # a -> b, 비용: -c (단방향 웜홀)

    negative_cycle = bf(1)
    if negative_cycle:
        print("YES")
    else:
        print("NO")

    
