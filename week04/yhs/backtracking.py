

import time



# 작업 코드





def backtracking(depth):
    if depth == 3:
        print(arr)
        global num
        num += 1
        # print(arr)
        return

    if True in visited:
        idx = length - visited[::-1].index(True)
    else:
        idx = 0

    for i in range(idx, length):
        if not visited[i]:
            visited[i] = True
            arr[depth] = empty[i]
            backtracking(depth + 1)
            visited[i] = False
    # print(result)


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

start = time.time()  # 시작 시간 저장

empty = []  # 여기에 빈 칸의 좌표들이 들어감
virus = []  # 여기에 바이러스의 좌표들이 들어감
length = 0  # 벽 세우기 전의 빈 칸 개수

for i in range(n):
    for j in range(m):
        filled = lab[i][j]
        if not filled:
            empty.append([i, j])    # 빈 칸 좌표 추가
            length += 1             # 빈 칸 개수 하나 추가
        if filled == 2:
            virus.append([i, j])    # 바이러스 좌표 추가

visited = [False for _ in range(length)]
result = []
arr = [0, 0, 0]
num = 0
wall_list = backtracking(0)

# for i in range(length - 2):
#     for j in range(i + 1, length - 1):
#         for k in range(j + 1, length):
#             print([empty[i], empty[j], empty[k]])



print("time :", time.time() - start, num)  # 현재시각 - 시작시간 = 실행 시간