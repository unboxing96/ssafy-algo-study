import sys
sys.stdin = open("03_1012_유기농배추.txt")

from collections import deque

import sys
sys.setrecursionlimit(10 ** 5)

def dfs(x, y, cnt):
    matrix[x][y] = -1 # 방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
            cnt = dfs(nx, ny, cnt + 1)

    return cnt

def bfs(a, b):
    q = deque()
    q.append((a, b))
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                matrix[nx][ny] = -1
                q.append((nx, ny))
                cnt += 1
    
    return cnt


T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for tc in range(T):
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]

    for _ in range(k):
        b, a = map(int, input().split())
        matrix[a][b] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                # if dfs(i, j, 1):
                #     result += 1
                if bfs(i, j):
                    result += 1

    print(result)