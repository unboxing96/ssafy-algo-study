import sys
sys.stdin = open("04_7576_토마토.txt")

# 문제 분석
# 토마토의 동서남북은 하루 뒤에 익는다.
# 모든 토마토가 익는 최소 일수를 구하라.
# 익은 토마토(1), 싱싱 토마토(0), 토마토 없음(-1)

# 모든 토마토가 익어있으면 0
# 토마토가 모두 익지 못 하는 상황이면 -1

# 접근
# 행렬 탐색해서 1을 만난 곳에서 탐색을 시작한다.
    # 큐가 빌 때까지 bfs를 진행한다.
    # 큐에 들어갈 원소에 cnt를 추가하여, 며칠 차인지 판단한다.
    # 큐가 빈다는 것은 탐색 가능한 곳을 모두 한 것이다.
# 탐색이 종료되면, 다시 행렬을 탐색하며 정답을 출력한다.
    # 0이 하나라도 있으면 -1
    # 하나도 없으면, 가장 큰 값 return - 1

from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
            matrix[nx][ny] = matrix[x][y] + 1
            q.append((nx, ny))

print(matrix)

max_cnt = 0
isZero = False
for i in range(n):
    max_cnt = max(max_cnt, max(matrix[i]))
    if 0 in matrix[i]:
        isZero = True

if isZero:
    print(-1)
else:
    print(max_cnt - 1)