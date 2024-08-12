# 문제 분석
# 벽 세우고, 4방으로 모든 방향 델타 탐색

import sys
sys.stdin = open("04_18428_감시피하기.txt")

import copy

def make_wall(cnt):
    if cnt == 3:
        return search()

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "X":
                matrix[i][j] = "O"
                if make_wall(cnt + 1):
                    return True # search()가 True를 반환한 경우
                matrix[i][j] = "X"
    
    return False # 끝까지 True를 반환하지 못 한 경우

def search():
    new_matrix = copy.deepcopy(matrix)

    for x, y in stack:
        for i in range(4):
            nx = x
            ny = y

            while True:
                nx += dx[i]
                ny += dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    break
                if new_matrix[nx][ny] == "O":
                    break
                if new_matrix[nx][ny] == "S":
                    return False # 학생 마주치면 발각
    return True # 마주치지 못 하면 숨기 성공


n = int(input())
matrix = [list(input().split()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
stack = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "T":
            stack.append((i, j))

if make_wall(0):
    print("YES")
else:
    print("NO")