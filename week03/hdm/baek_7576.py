import sys
from collections import deque
sys.stdin = open('input.txt')


## 7576


def bfs(graph, start):
    queue = deque(start) # deque를 사용하여 BFS를 위한 큐 초기화.
                         # start에 있는 모든 좌표를 큐에 넣기.
    while queue:
        x, y = queue.popleft() # 큐의 왼쪽에서 하나의 좌표를 꺼냅니다.
        for i in range(4): # 오아왼위 순회
            nx = x + dr[i]
            ny = y + dc[i]
            # 배열을 벗어나지 않으면서, 익지않은 토마토가 있으면,
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] +1 #토마토를 익히고, 일수를 갱신
                queue.append((nx,ny)) # 새로운 좌표를 큐에 추가



M, N = map(int, input().split()) #M은 열의 수, N은 행의 수
arr = [list(map(int, input().split())) for _ in range(N)] #


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
start = []

# start에 익은 토마토 위치 추가
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            start.append((r,c)) # 익은 토마토의 좌표를 start에 입력해주기.
                                # bfs를 위한 그래프 그려주기

bfs(arr,start) ## BFS를 수행하여 토마토 익히기!

#bfs이후
days = 0 # 모든 토마토가 익는 데 걸린 일수를 기록할 변수

# 익지 않은 토마토가 있는지 확인하며, 없다면 최대 일수를 출력!
for r in range(N):
    for c in range(M):
        if arr[r][c] == 0: #익지않은 토마토가 있으면 그주위에 익은 토마토도 없느거자나
            print(-1) # 모두 익지 못하는 상황이라 -1출력하고 프로그램 종료시키기!
            exit()
        days = max(days, arr[r][c]) # day와 현재 arr의 값을 비교하며 최대일수 뽑아내기!

print(days - 1) # 첫날 시작점 arr[r][c]를 1로 시작해줌. 따라서 1일차에 익은것으로 간주되기에
                # 익은날을 확인하기 위해서 -1해주는것임.


