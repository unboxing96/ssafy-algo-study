# 토마토 풍년!
from collections import deque

m,n,h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]


q = deque()
day = -1 # while문에서 첫날에도 day가 1 더해지므로
test = []
# 덱 안에 우선 토마토 위치 넣기, 토마토 값 빈 리스트에 넣기
for k in range(h):
    for i in range(n):
        for j in range(m):
            test.append(tomato[k][i][j])
            if tomato[k][i][j] == 1:
                q.append([k, i, j])

# 만약 모든 토마토가 0이나 -1이면 0출력
# if 0 not in test:
#     print(0)  << 실수함, 그냥 빼도 while문에서 +1 돌아가서 괜찮음

while q: # 큐가 비게되면 영향을 끼치는 토마토 위치가 더이상 없음
    one_day = len(q) # 하루동안

    dx = [0, 0, 1, -1, 0, 0]    # 3차원 데이터이므로 6방향탐색 동서남북상하
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for _ in range(one_day):
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nz<h and 0<=nx<n and 0<=ny<m and tomato[nz][nx][ny] == 0: # 토마토 빈 곳은 무시
                tomato[nz][nx][ny] = 1
                q.append([nz, nx, ny])   
    day += 1

def remain_nomat_tomato():
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == 0: # 안 익은 토마토가 남아있다면
                    return 0
    return 1
                
if remain_nomat_tomato() == 1:
    print(day)
else:
    print(-1)
