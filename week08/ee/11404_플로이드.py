import sys
sys.stdin = open("11404_input.txt")

n = int(sys.stdin.readline()) # 도시의 개수 n
m = int(sys.stdin.readline()) # 버스의 개수 m

inf = int(1e9)
graph = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c) # 같은 도시에 대한 여러 노선 중 최소 비용만 고려

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    print()