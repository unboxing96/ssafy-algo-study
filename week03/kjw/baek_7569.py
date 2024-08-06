# 토마토 흉년
from collections import deque

m,n,h = map(int, input().split())
tomato = []
queue = deque()
# 1 익음 0 안익음 -1 없음
for h in range(h):
    toma = []
    for n in range(n):
        hor = list(map(int, input().split()))
        for m in range(m):
            if hor[m] == 1:
                queue.append((n,m,h))
            toma.append(hor)
        tomato.append(toma)

def bfs(tomato, queue):
    turn = [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]
    days = 0
    
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            for dx, dy, dz in turn:
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                    if tomato[nz][nx][ny] == 0:
                        tomato[nz][nx][ny] = 1
                        queue.append((nx, ny, nz))
    
    return days

result = bfs(tomato, queue)
tomatoma = True
for h in range(h):
    for n in range(n):
        for m in range(m):
            if tomato[h][n][m] == 0:
                tomatoma = False
                break
        if not tomatoma:
            break
    if not tomatoma:
        break

if tomatoma:
    print(result)
else:
    print(-1)