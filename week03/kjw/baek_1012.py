import sys
sys.setrecursionlimit(10**6)

T = int(input())
for tc in range(1,T+1):
    m,n,k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    for _ in range(k):      # 배추위치 표시
        x, y = map(int, input().split())
        arr[y][x] = 1

    dx = [-1, 0, 1, 0] # 북 동 남 서
    dy = [0, 1, 0, -1]
    bug = 0
    def dfs(a,b):
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] ==1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                a = nx
                b = ny
                dfs(a,b)
        else:
            return True

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                result = dfs(i,j)
                if result:
                    bug += 1
    print(bug)
