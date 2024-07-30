import sys
sys.stdin = open("11_뱀.txt", "r")

# 문제 분석
# 매초마다 다음 칸을 확인한다.
# 사과가 있으면 해당 칸을 칠한다.
# 사과가 없으면 해당 칸으로 이동하고, 가장 오래 전에 추가한 칸을 삭제한다.
# '가장 오래 전'을 판단하기 위해, 모든 이동 경로를 큐로 관리하자.

# 방향 전환
# L을 입력 받으면 왼쪽으로 (-y, x)
# D를 입력 받으면 오른쪽으로 방향 전환한다. (y, x)
# 왼쪽 이동: (0, 1) (-1, 0) (0, -1) (1, 0)
# 오른쪽 이동: (0, 1) (1, 0) (0, -1) (-1, 0)
# 같은 배열을 왼쪽 이동은 역방향, 오른쪽 이동은 정방향으로 이동

# 접근
from collections import deque

N = int(input()) # 정사각형의 2차원 배열이 주어짐
K = int(input()) # 사과의 개수
matrix = [[0] * N for _ in range(N)] # 2차원 배열 생성
for _ in range(K): # 사과 배치
    i, j = map(int, input().split())
    matrix[i - 1][j - 1] = 2 # 사과는 2로 표시. # 문제에서 행렬의 좌상단을 (1, 1)로 정의했기에, 1씩 빼줘야 정확한 위치를 참조할 수 있음.

d = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 이동 방향 경우의 수
d_idx = 0 # 이동 방향을 결정하는 인덱스
def direction_change(operation, d_idx):
    if operation == "L":
        return (d_idx - 1) % 4
    else:
        return (d_idx + 1) % 4 # 오른쪽을 입력하면 d배열을 정방향 탐색

direction_change_count = int(input())   # 방향 전환 횟수 입력
direction_change_list = deque()         # (전환 시간, 전환 방향)
for _ in range(direction_change_count):
    t, op = input().split()
    direction_change_list.append((int(t), op))
    
q = deque()
q.append((0, 0)) # 초기 위치 설정
matrix[0][0] = 1 # 뱀이 있는 위치는 1로 설정
time = 0

while q:
    time += 1
    x, y = q[-1] # 현재 머리 위치
    nx = x + d[d_idx][0] # 에러 발생: TypeError: unsupported operand type(s) for +: 'int' and 'str'
    ny = y + d[d_idx][1]

    if nx < 0 or nx >= N or ny < 0 or ny >= N: # 범위를 벗어나면 break
        break

    if matrix[nx][ny] == 1: # 뱀의 몸통을 만나면 break
        break

    if matrix[nx][ny] == 2: # 사과를 만나면
        q.append((nx, ny)) # 머리는 진행
        matrix[nx][ny] = 1 # 뱀의 몸통으로 표시
    else: # 아무것도 만나지 않으면
        q.append((nx, ny)) # 머리는 진행
        matrix[nx][ny] = 1 # 뱀의 몸통으로 표시
        tx, ty = q.popleft() # 꼬리 제거
        matrix[tx][ty] = 0 # 꼬리가 있던 자리 0으로
    

    if direction_change_list and time == direction_change_list[0][0]: # 방향 전환 타이밍일 때
        _, op = direction_change_list.popleft()
        d_idx = direction_change(op, d_idx)
    

print(time)