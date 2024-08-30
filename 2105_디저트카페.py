import sys
sys.stdin = open("2105_디저트카페.txt")

# 문제분석
# 백트래킹
# 시작 위치로 돌아온 경우 && 4번째 방향인 경우에만 값을 갱신
# 먹을 수 없는 경우 -1

def dfs(cx, cy, direction, visited):
    global max_cnt
    
    # 시작점으로 돌아오고, 네 방향 모두 탐색한 경우
    if cx == i and cy == j and direction == 3 and len(visited) > 2:
        max_cnt = max(max_cnt, len(visited))
        return
    
    for d in range(direction, direction + 2):
        if d > 3:
            break
            
        nx = cx + dx[d]
        ny = cy + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if matrix[nx][ny] not in visited:
            dfs(nx, ny, d, visited + [matrix[nx][ny]])

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, 1, -1, -1]
    dy = [-1, 1, 1, -1]
    max_cnt = -1

    for i in range(n):
        for j in range(n):
            dfs(i, j, 0, [])

    print(f"#{tc} {max_cnt}")
