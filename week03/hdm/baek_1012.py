import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 배추 밭의 가로 세로 배추수 입력받기
    M, N, K = map(int, input().split())
    # 배추의 위치 담기
    positions = [tuple(map(int, input().split())) for _ in range(K)]

    farm = [[0] * M  for _ in range(N)] # 배추밭 2차원배열 초기화

    # 배추의 위치를 배추밭(farm) 2차원 배열에 표시합니다.
    # 입력에서 x, y 순서이지만, 배열에서는 y, x 순서로 저장합니다.
    for x, y in positions:
        farm[y][x] = 1

    # 간곳 방문여부 체크
    visited_arr = [[False]* M for _ in range(N)]
    worm_count = 0

    # 델타사용
    dr = [ 0 , 1, 0 , -1]
    dc = [1, 0  , -1 ,0]

    def bfs_farm(start_r, start_c):
        #시작 위치에 큐를 추가함.
        queue = deque([(start_r, start_c)])
        # 시작 위치를 방문 처리함.
        visited_arr[start_r][start_c] = True

        while queue: # 탐색을 다 할때까지 끝내지 않을거라는 얘기임.
            # 큐에서 현재 위치를 가지오고,
            row, col = queue.popleft()
            # 델타로 방향탐색
            for i in range(4):
                nr, nc = row + dr[i], col + dc[i]
                # 벽에 부딪히지 않고
                if 0 <= nr < N and 0<= nc < M :
                    # 방문한적 없으며, 농장의 배추수도 1로 확인되면,
                    if not visited_arr[nr][nc] and farm[nr][nc] == 1:
                        # 새위치를 큐에 추가하고
                        queue.append((nr, nc))
                        # 방문처리함.
                        visited_arr[nr][nc] = True
        return

    # 배추밭 순회하면서 배추찾기
    for r in range(N):
        for c in range(M):
            if farm[r][c] == 1 and not visited_arr[r][c]: # 방문한적이 없는것을 넣어주며 중복제거해줌.
                bfs_farm(r, c) #새로운 배추 찾으면 bfs탐색하기
                worm_count += 1 # 흰지렁이수 추가.

    print(worm_count)





