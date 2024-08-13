import sys
sys.stdin = open("05_16234_인구이동.txt")

# 문제 분석
# 인접한 노드의 값이 L 이상 R 이하라면 국경을 개방한다.
# 연합은 인구 수를 1/N 한다.
# 인구 이동이 발생하는 날이 총 며칠인지 구하라.

# 접근
# DFS() 탐색
# 탐색 중인 노드와 다음 노드의 값이 L 이상 R 이하일 때, union_sum에 추가
# 탐색이 종료되면 해당 위치를 union_sum // n으로 바꿔줌
# path를 기억하고, path를 돌면서 값 변경

def dfs(x, y, cnt, tmp_sum, visited, path):
    visited[x][y] = True
    tmp_sum += matrix[x][y]
    cnt += 1
    path.append((x, y))  # 현재 위치를 path에 추가

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if l <= abs(matrix[nx][ny] - matrix[x][y]) <= r:
                cnt, tmp_sum = dfs(nx, ny, cnt, tmp_sum, visited, path)

    return cnt, tmp_sum

def move_population():
    visited = [[0] * n for _ in range(n)]
    is_moved = False  # 인구 이동이 발생했는지 여부

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                path = []
                cnt, tmp_sum = dfs(i, j, 0, 0, visited, path)
                
                # 연합이 형성된 경우
                if cnt > 1:
                    is_moved = True
                    new_value = tmp_sum // cnt
                    for x, y in path:
                        matrix[x][y] = new_value

    return is_moved

# 입력 받기
n, l, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

days = 0

# 인구 이동이 더 이상 발생하지 않을 때까지 반복
while True:
    if not move_population():
        break
    days += 1

print(days)
