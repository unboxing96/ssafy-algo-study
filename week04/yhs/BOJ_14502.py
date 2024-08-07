from copy import deepcopy
from collections import deque


def wall(lab, *args):
    # 벽 세우기
    walled_lab = deepcopy(lab)  # 원본 행렬 바뀌는 것 방지

    # *args(3개)의 좌표에 벽 세우기
    for coor in args:
        walled_lab[coor[0]][coor[1]] = 1

    return walled_lab


def bfs(lab, virus):
    infected = deepcopy(lab)    # 원본 행렬 바뀌는 것 방지
    # delta
    drow = [1, 0, -1, 0]
    dcol = [0, 1, 0, -1]

    queue = deque(virus)    # 큐에 바이러스 위치 넣기
    # bfs 시작
    while queue:
        s = queue.popleft()
        # 인접행렬 탐색하기
        for i in range(4):
            row = s[0]+drow[i]
            col = s[1]+dcol[i]
            # 인덱스 범위 내에 있고 빈 칸일 경우 바이러스 감염
            if 0 <= row < n and 0 <= col < m and infected[row][col] == 0:
                queue.append([row, col])    # 큐에 추가
                infected[row][col] = 2

    # 안전 영역 개수 세기
    count = 0
    for r in infected:
        for c in r:
            if c == 0:
                count += 1

    return count


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

empty = []  # 여기에 빈 칸의 좌표들이 들어감
virus = []  # 여기에 바이러스의 좌표들이 들어감
length = 0  # 벽 세우기 전의 빈 칸 개수

for i in range(n):
    for j in range(m):
        filled = lab[i][j]
        if not filled:
            empty.append([i, j])    # 빈 칸 좌표 추가
            length += 1             # 빈 칸 개수 하나 추가
        if filled == 2:
            virus.append([i, j])    # 바이러스 좌표 추가

# 안전 영역의 최대 개수 구하기
max_area = 0
# for문 3개 --> 빈 칸에 3개의 벽을 세우는 모든 경우
for i in range(length - 2):
    for j in range(i + 1, length - 1):
        for k in range(j + 1, length):
            walled_lab = wall(lab, empty[i], empty[j], empty[k])    # 벽 세운 후의 행렬
            temp = bfs(walled_lab, virus)   # 바이러스가 퍼진 수 안전 영역의 개수
            # 안전영역 최대값 갱신하기
            if temp > max_area:
                max_area = temp

print(max_area)