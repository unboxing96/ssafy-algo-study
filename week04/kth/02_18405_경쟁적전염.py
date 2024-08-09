import sys
sys.stdin = open("02_18405_경쟁적전염.txt")

# 문제 분석
# S초 뒤에 X, Y 좌표에는 어떤 바이러스가 있겠는가?
# BFS

from collections import deque

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
s, ex, ey = map(int, input().split()) # 진짜 인덱스는 ex - 1, ey - 1
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

q = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            q.append((i, j, matrix[i][j], 0))  # 시간 정보 추가

q.sort(key=lambda x: x[2])  # 바이러스 낮은 순으로 정렬
q = deque(q)

def bfs():
    while q:
        x, y, virus, time = q.popleft()

        if time == s:  # 주어진 시간이 되었을 때 종료
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = virus
                    q.append((nx, ny, virus, time + 1))  # 시간 증가

bfs()
print(matrix[ex - 1][ey - 1])
