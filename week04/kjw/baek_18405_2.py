from collections import deque
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()
l=1
# 0초일 때 바이러스 위치 큐에 추가, 1부터 넣음
while l <= k:
    for i in range(n):
        for j in range(n):
            if arr[i][j] == l:
                queue.append((0, i, j, l))
    l += 1

while queue:
    time, a, b, virus_num = queue.popleft()
    # 주어진 시간만큼 전파
    if time == s:
        break

    for q in range(4):
        nx = a + dx[q]
        ny = b + dy[q]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 0:
                arr[nx][ny] = virus_num
                queue.append((time + 1, nx, ny, virus_num))

print(arr[x-1][y-1])