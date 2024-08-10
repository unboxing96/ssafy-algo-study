import sys
from copy import deepcopy
from collections import deque

sys.stdin = open('input.txt')

# 벽 세울 위치를 선택하여 바이러스가 퍼지는것을 막기
# 벽을 세운후 안전지역 최대! 출력


def walls(idx, selected, count):
    if count == 3:   # 3번째 벽이 세워지면
        matrix_copy = deepcopy(matrix)  # 딥카피로 연구소 복사해버려
        for r, c in selected:
            matrix_copy[r][c] = 1 # 해당 좌표에 벽세우기
        virus_musawa = safe_count(bfs(matrix_copy),row, col) #바이러스 몇개인지 체크하고, 안전한거 몇갠지 체크
                                                            # bfs를 통해서 바이러스감염된것의 count를 뽑을거야
        global max_safe_area # 최대값 저장해야지
        max_safe_area = max(max_safe_area, virus_musawa) # max로 최대값 계속 업데이트 해주기
        return
    if idx >= len(zero_spaces): # 모든 빈칸을 다 확인했을 경우 종료
        return

    r, c = zero_spaces[idx]

    # 벽 세우는 경우
    selected.append((r, c)) # 벽을 세우려는 좌표를 배열에 넣어줌으로써
                            # 2번째에서 또 벽세울거야. 0 아무곳이나 세울거임.

    walls(idx+1, selected, count +1) # 다음 벽 선택하러가기
                                    # 벽을 계속 선택해주고 idx를 1추가시켜서 zero count의 배열을 초과할때까지 순회해야지

    selected.pop() #선택된 좌표 제거하고 다음 조합을 위해 초기화

    # 벽 안세우면
    walls(idx+1, selected, count)


def safe_count(arr, r, c):
    count = 0  # 35
    for r in range(row):
        for c in range(col):
            if arr[r][c] == 0:
                count += 1
    return count

def bfs(arr): # 출발하려는 번호와 배열이 들어가도 되겠지?

    directions = [(0,1), (1,0), (0, -1), (-1,0)] # 오아왼위 시계방향 체크

    start_point = [(r, c) for r in range(row) for c in range(col) if arr[r][c] == 2]
    # 바이러스 시작지점을 큐에 넣기.

    queue = deque(start_point)
    # for start_row, start_col in start_point:
    #     queue = deque([(start_row, start_col)])  # 2를 찾아 queue에 넣어 출발지점 넣기

    while queue:
        current_row, current_col = queue.popleft() # 큐가 빌동안 돌아주세요
        # virus_matrix.append(v) # 어디 방문했는지 체크하는법
        for dr, dc in directions :
            new_row, new_col = current_row + dr, current_col + dc
            if 0 <= new_row < row and 0 <= new_col < col and arr[new_row][new_col] == 0:
                # 배열 내에 있어야하고 빈칸이면
                arr[new_row][new_col] = 2 # 바이러스 지지직
                queue.append((new_row, new_col))
    return arr




row, col = map(int, input().split()) # row 세로크기 # col 가로크기
matrix = [list(map(int,input().split())) for _ in range(row)]


# 빈칸의 좌표를 모두 찾아서 빈칸중 3개를 선택하여 벽을 세움. 바이러스 퍼지고 가장 안전한 영역 몇개인지 체크
# 0 좌표 리스트 만들자.
zero_spaces =[(r,c) for r in range(row) for c in range(col) if matrix[r][c] == 0]
max_safe_area = 0
walls(0,[],0)

print(max_safe_area)



# ------------------------------------------------------------------------------
# 결과적으로 필요 없어진 코드

# def bueckjohap(n, r):
#     return factorial(n) // (factorial(r) * factorial((n-r))) # float으로 안뽑을거야. // 로 몫만 챙겨
#
# def factorial(num):
#     if num == 0: # 만약 num이 0이되면 1을 리턴하면됨.
#         return 1
#
#     return num * factorial(num-1)
#     # while 도되고, 재귀도됨.
#     # num을 1까지 곱해가는 과정 1~ n까지 곱해야함.



# 벽세우기
# 2차원 배열에서 빈칸0인곳에 벽을 세우기 가능한 모든 조합을 구해보기. 빈칸수 C3일것임.
# n! / r!(n-r)! = bueckjohap() 으로 구현함.
# 빈칸수 몇개니? 개수 구하는 공식
# count = safe_count(matrix, row, col) #35
# check_bueck = bueckjohap(count, 3) # 벽조합 6545개임.




# 안전영역계산
# 바이러스가 모두 퍼진 후 안전 영역의 빈칸수를 계산해야됨 // 즉 아무도 막지않은상태에서 바이러스 퍼지면 안전한거 몇개임?
# 전환을 체크하자
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# 바이러스가 모두 퍼진 후 안전영역의 빈칸수 체크
# for r in range(row):
#     for c in range(col):
#         for k in range(4):
#             nr = r + dr[k]
#             nc = c + dc[k]
#             if 0 <= nr < row and 0 <= nc < col and matrix[nr][nc] == 0 and matrix[r][c] == 2 and matrix[nr][nc] != 1: #만약 [nr][nc]값이 0이고, 배열을 벗어나지 않고 현재 배열값이 2면
#                 matrix[nr][nc] = 2 # 넌 전염됐어.
#
# virus_musawa = safe_count(matrix, row, col) #0 바이러스가 퍼진 후 안전영역의 빈칸 수

# print(virus_musawa)

# or bfs로 바이러스 퍼트리기
# virus_musawa = (safe_count(bfs(matrix), row, col))



# walls를 재귀가 아닌, for문으로 반복하게 된다면?
# walls(N)
#     for i1 in range(N):
#         for i2 in range(N):
#             if i2 != i1:
#                 for i3 in range(N):
#                     if i3 != i1 and i3 != i2:
#                         selected = [zero_spaces[i1], zero_spaces[i2], zero_spaces[i3]]
#
#                         matrix_copy = deepcopy(matrix)  # 연구소 복사
#                         for r, c in selected:
#                             matrix_copy[r][c] = 1  # 벽 세우기
#
#                         virus_musawa = safe_count(bfs(matrix_copy), row, col)  # 바이러스 확산 후 안전 영역 계산
#                         max_safe_area = max(max_safe_area, virus_musawa)  # 최대값 업데이트