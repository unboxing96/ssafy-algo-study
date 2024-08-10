# 토마토
# 골드 5 실화?

import sys
from collections import deque

sys.stdin = open('7569_input.txt')

M, N, H = map(int, sys.stdin.readline().split())
tomatoes = [[[0] * M for _ in range(N)] for _ in range(H)]
for i in range(H): # 토마토의 위치
    for j in range(N):
        tomatoes[i][j] = list(map(int, sys.stdin.readline().split()))

queue = deque()

for k in range(H):
    for j in range(N):
        for i in range(M):
            if tomatoes[k][j][i] == 1:
                queue.append([i, j, k]) # 맨 처음에 토마토 어디있는지 큐에 넣어주기

dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

days = 0

while queue: #큐가 빌 때 까지
    for _ in range(len(queue)): #하루에는 큐에 들어있는 만큼의 토마토가 영향을 줌
        
        x, y, z = queue.popleft() 

        # 여섯 방향으로 영향을 준다
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
          # 범위를 벗어나지 않고 토마토가 안 익었으면
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and tomatoes[nz][ny][nx] == 0:
                tomatoes[nz][ny][nx] = 1
                queue.append((nx, ny, nz))
    days += 1


def check():
    for k in range(H):
        for j in range(N):
            for i in range(M):
                if tomatoes[k][j][i] == 0:
                    return False
    return True

if check():
    print(days-1)
else:
    print(-1)