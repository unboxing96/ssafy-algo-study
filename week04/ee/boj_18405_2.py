# 경쟁적 전염

import sys
sys.stdin = open('18405_input.txt')

N, K = map(int, sys.stdin.readline().split())  # 시험관 크기 N, 바이러스 번호 최댓값 K
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 시험관 정보
S, X, Y = map(int, sys.stdin.readline().split())  # S초 뒤에 (X,Y)에 존재하는 바이러스의 종류 출력하기

virus = []

for i in range(N):
    for j in range(N):  # 바이러스 위치 저장하기
        if arr[i][j]:  # 0이 아니면 (바이러스라면)
            virus.append([arr[i][j], i, j]) # [바이러스 번호, 행, 열]

virus.sort() # 바이러스 번호가 낮은 순서대로 정렬

from collections import deque
queue = deque(virus)

di = [1, -1, 0, 0]  # 바이러스는 상하좌우로 증식
dj = [0, 0, 1, -1]

sec = 0

while queue: # 큐가 빌 때 까지!

    if sec == S: # S초까지 
        break

    for _ in range(len(queue)): # 바이러스 번호가 낮은 순서부터
        num, i, j = queue.popleft() # num 바이러스 번호, i 행, j 열

        for k in range(4): # 상하좌우로
            ni, nj = i +di[k], j + dj[k] 

            # 시험관 범위를 넘지 않고 바이러스가 증식 안 된 곳이면
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0: 
                arr[ni][nj] = num # 바이러스 증식
                queue.append([num, ni, nj]) # 큐에 추가

    sec += 1 

print(arr[X-1][Y-1])