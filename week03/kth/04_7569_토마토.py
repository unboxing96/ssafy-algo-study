import sys
sys.stdin = open("04_7569_토마토.txt")

# 문제 분석
# 6방 탐색: 동서남북상하

# 접근
# 3차원 배열을 만들어야 한다.
# dh = [1, -1, 0, 0, 0, 0]
# dx = [0, 0, 1, -1, 0, 0]
# dy = [0, 0, 0, 0, -1, 1]

from collections import deque

m, n, h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
q = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if matrix[k][i][j] == 1:
                q.append((k, i, j))

while q:
    z, x, y = q.popleft()

    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and matrix[nz][nx][ny] == 0:
            matrix[nz][nx][ny] = matrix[z][x][y] + 1
            q.append((nz, nx, ny))

isZero = False
max_cnt = 0

for k in range(h):
    for i in range(n):
        if isZero in matrix[k][i]:
            isZero = True
            break
        max_cnt = max(max(matrix[k][i]), max_cnt)

if isZero:
    print(-1)
else:
    print(max_cnt - 1)