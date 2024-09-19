N = int(input()) # 물건의 개수 N
M = int(input()) # 미리 측정된 물건 쌍의 개수 M

INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):


for row in graph:
    print(row)


