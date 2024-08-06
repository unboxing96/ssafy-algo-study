import sys
sys.setrecursionlimit(10**6)

T = int(input())
for tc in range(1,T+1):
    m,n,k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]

    for _ in range(k):      # 배추위치 표시
        x, y = map(int, input().split())
        arr[y][x] = 1

    def dfs(a,b,arr,visited,n,m):
        stack = [(a,b)]
        turn = [(-1,0), (1,0), (0,1), (0,-1)]
        while stack:
            c,d = stack.pop()
            for dx, dy in turn:
                nx,ny = c + dx, d+dy
                if 0<=nx<n and 0<=ny<m:
                    if arr[nx][ny] ==1 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        stack.append((nx,ny))
                        
                  
    def count_bug(arr,n,m):
        visited = [[0]*m for _ in range(n)]
        bug = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1 and visited[i][j] == 0:
                    dfs(i,j,arr,visited,n,m)
                    bug += 1
        return bug

    result = count_bug(arr,n,m)

    print(result)
