n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

# 데이터 입력받아서 연결되어 있다면 1로 바꾸기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플로이드 워셜 알고리즘 진행으로 연결되어 있으면 1로 바꿔줌
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == INF:
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1

# 출력하기
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] == INF:
            if graph[j][i] == INF:
                cnt += 1
    print(cnt)