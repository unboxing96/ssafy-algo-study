T = int(input())
INF = int(1e9)
def bellman_ford(start):
    distance[start] = 0
    for i in range(n):
        for j in range(len(edges)):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            if distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                # n-1까지 순환돌면 음수순환이 존재한다는 뜻
                if i == n - 1:
                    return True
    return False

for tc in range(1, T+1):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))
    distance = [INF]*(n+1)
    time_trip = bellman_ford(1)

    if time_trip:
        print('YES')
    else:
        print('NO')