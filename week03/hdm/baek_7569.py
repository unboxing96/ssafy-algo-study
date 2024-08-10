import sys
from collections import deque
sys.stdin = open('input.txt')


# 7576에서 z방향 추가..  진짜 몰라서 z방향 델타로 찾는법 공부 후 참고하여 풀이했습니다!@
# 익은토마토 4방향의 익지않은 토마토가 있으면 다 익음.
# 1 = 익은 토마토
# 0 = 익지 않은 토마토
# -1 = 토마토가 들어있지 않음.

def bfs(graph, start):
    queue = deque(start) # deque를 사용하여 BFS를 위한 큐 초기화.
                         # start에 있는 모든 좌표를 큐에 넣기.
    while queue:
        z, x, y = queue.popleft() # 큐의 왼쪽에서 하나의 좌표를 꺼냅니다.
        for i in range(6):
            nx = x + dx[i] # 상하좌우앞뒤
            ny = y + dy[i]
            nz = z + dz[i]
            # 배열을 벗어나지 않으면서, 익지않은 토마토가 있으면,
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] +1 #토마토를 익히고, 일수를 갱신
                queue.append((nz,nx,ny)) # 새로운 좌표를 큐에 추가



M, N, H = map(int, input().split()) #M은 가로의 수, N은 세로의 수 M은 x, y좌표상 y,x임
arr = [[list(map(int, input().split())) for _ in range(N)]for _ in range(H)]
# 입력을 n만큼 h번들어오잖아?


dx = [0, 0, -1, 1, 0, 0] # 상하좌우위아래(앞뒤)
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0 ,0 , 1 ,-1] # 상하좌우위아래(앞뒤)
start = []

# start에 익은 토마토 위치 추가
for z in range(H):
    for x in range(N):
        for y in range(M):
            if arr[z][x][y] == 1:
                start.append((z,x,y)) # 익은 토마토의 좌표를 start에 입력해주기.
                                    # bfs를 위한 그래프 그려주기

bfs(arr,start) ## BFS를 수행하여 토마토 익히기!

#bfs이후
days = 0 # 모든 토마토가 익는 데 걸린 일수를 기록할 변수

# 익지 않은 토마토가 있는지 확인하며, 없다면 최대 일수를 출력!
for z in range(H):
    for x in range(N):
        for y in range(M):
            if arr[z][x][y] == 0: #익지않은 토마토가 있으면 그주위에 익은 토마토도 없느거자나
                print(-1) # 모두 익지 못하는 상황이라 -1출력하고 프로그램 종료시키기!
                exit()
            days = max(days, arr[z][x][y]) # day와 현재 arr의 값을 비교하며 최대일수 뽑아내기!

print(days - 1) # 첫날 시작점 arr[r][c]를 1로 시작해줌. 따라서 1일차에 익은것으로 간주되기에
                # 익은날을 확인하기 위해서 -1해주는것임.