import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split()) # 세로 N 가로 M
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N) ]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

# 바이러스 증식 함수
def replicateVirus(virus, area):
    for item in virus:
        i = item[0]
        j = item[1]
        for k in range(4): # 상하좌우   
            ni, nj = i + di[k], j + dj[k] 
            if 0 <= ni < N and 0 <= nj < M and area[ni][nj] == 0: # 연구소 안에서, 벽이 아닌 곳이면
                area[ni][nj] = 2 # 바이러스 증식 !
                replicateVirus([[ni, nj]], area)
    return area

empty = []
wall = []
virus = []

for i in range(N):
    for j in range(M): 
        if area[i][j] == 0:         # 빈 칸 (0) 
            empty.append([i, j])
        elif area[i][j] == 1:       # 벽 (1)
            wall.append([i, j])
        else:                       # 바이러스 (2)
            virus.append([i, j])

import itertools
import copy

combinations = list(itertools.combinations(empty, 3)) # 모든 조합을 고려
max_safety = 0 # 최대 안전구역의 수?

for item in combinations: # 모든 경우의 수에 대해 조사
    copy_area = copy.deepcopy(area) # 복사해서 따로 담아두기 깊은복사로

    # 벽 세우기
    copy_area[item[0][0]][item[0][1]] = 3
    copy_area[item[1][0]][item[1][1]] = 3
    copy_area[item[2][0]][item[2][1]] = 3 

    result = [] 
    result = replicateVirus(virus, copy_area) # 벽 세운 연구소에서 바이러스 증식 ~~~~~

    safety = 0 # 안전구역 수 찾기
    for row in result:
        safety += row.count(0)

    if safety > max_safety: # 최댓값 찾기
        max_safety = safety
    
print(max_safety) # 출력