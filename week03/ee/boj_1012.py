import sys
sys.stdin = open('1012_input.txt')
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기

def dfs(grounds, x, y, M, N):

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    grounds[y][x] = -1 # 방문 처리

    for i in range(4):
        nx, ny = x+ dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and grounds[ny][nx] == 1:
            dfs(grounds, nx, ny, M, N)

T = int(sys.stdin.readline().strip())  # 테스트 케이스 수

for tc in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())  # 배추밭 가로길이 M, 세로길이 N, 배추 위치 개수 K
    cabbages = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(K)]
    grounds = [[0] * M for _ in range(N)]
    
    for x, y in cabbages:
        grounds[y][x] = 1

    count = 0  # 배추흰지렁이 마리 수

    for i in range(M):
        for j in range(N):
            if grounds[j][i] == 1:
                dfs(grounds, i, j, M, N)
                count += 1
                    
    print(count) 

