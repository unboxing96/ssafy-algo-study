# 토마토
# 골드 5 실화?

import sys
sys.stdin = open('7569_input.txt')

M, N, H = map(int, sys.stdin.readline().split())
tomatoes = [[[0] * M for _ in range(N)] for _ in range(H)]

rest = 0
for i in range(H):
    for j in range(N):
        tomatoes[i][j] = list(map(int, sys.stdin.readline().split()))
        for tomato in tomatoes[i][j]: #안 익은 토마토 개수세기
            if tomato == 0:
                rest += 1

# 정수 1은 익은 토마토, 
# 정수 0 은 익지 않은 토마토, 
# 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다

from collections import deque

def bfs(x, y, z, M, N, H, tomatoes, today, rest):

    # 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 
    # 여섯 방향에 있는 토마토를 의미한다.
    dx = [0, 0, 1, -1, 0, 0]
    dy = [0, 0, 0, 0, 1, -1]
    dz = [1, -1, 0, 0, 0, 0]

    for i in range(6): # 여섯 방향으로 영향을 준다
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if (0<=nx<M) and (0<=ny<N) and (0<=nz<H) and (tomatoes[nz][ny][nx] == 0): # 안 익은 토마토
            tomatoes[nz][ny][nx] = 1 # 토마토가 익었어요
            today[nz][ny][nx] = 1 # 방문처리
            rest -= 1

    return rest
            


days = 0
yesterday_rest = 0

while rest > 0:
    today = [[[0] * M for _ in range(N)] for _ in range(H)] #방문 처리 할 리스트(하루마다 초기화)
    for k in range(H):
        for j in range(N):
            for i in range(M):
                if tomatoes[k][j][i] == 1 and today[k][j][i]==0:
                    rest = bfs(i, j, k, M, N, H, tomatoes, today, rest)
    if yesterday_rest == rest: #어제랑 변화가 없으면 토마토가 모두 익지 못하는 상황
        days = -1
        break
    else: # 잘 익고 있다
        days += 1
        yesterday_rest = rest

print(days)