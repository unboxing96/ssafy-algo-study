import sys
sys.stdin = open("01_14502_연구소.txt")

# 문제 분석
# 빈 칸 0, 벽 1, 바이러스 2
# 벽을 세울 수 있는 모든 경우의 수 : 64 * 64 * 64 ~= 240,000
# 벽을 세운 뒤, 바이러스를 최대한 퍼트리고, 남은 0의 최대 크기를 return

from collections import deque
import copy

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0


def bfs():
    q = deque()
    new_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 2:
                q.append((i, j)) # 바이러스 좌표 찾아서 큐에 추가


    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and new_graph[nx][ny] == 0:
                new_graph[nx][ny] = 2
                q.append((nx, ny))

    # 0 개수 세기
    global result
    tmp = 0
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 0:
                tmp += 1
    
    result = max(result, tmp)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
make_wall(0)

print(result)