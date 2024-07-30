N, M = map(int, input().split())
A, B, direction = map(int, input().split())
empty_map = [[0]*M for _ in range(N)]
''' 빈 N*M맵 생성, 2차원 데이터, 1로 변한 육지와 1인 바다를 구분하기위해 사용
[
 [0, 0, 0, 0],
 [0, 0, 0, 0], 
 [0, 0, 0, 0], 
 [0, 0, 0, 0]
 ]
'''
empty_map[A][B] = 1 # 처음 내 위치, 육지임

# 맵 정보 입력
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

# 북 동 남 서 순서로 x,y 좌표의 변화
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

result = 1
turn_count = 0
while True:
    turn_left()
    move_A = A + dx[direction]
    move_B = B + dy[direction]
    # 이동할 때
    if empty_map[move_A][move_B] == 0 and arr[move_A][move_B] == 0:
        result += 1
        empty_map[move_A][move_B] = 1
        # 값 초기화
        A = move_A
        B = move_B
        turn_count = 0
        continue
    # 이동 못할 때
    else:
        turn_count += 1
    # 4방향 다막힘
    if turn_count == 4:
        move_A = A - dx[direction]
        move_B = B - dy[direction]
        if arr[move_A][move_B] == 0: # 안 가본 곳이면 이동
            A = move_A
            B = move_B
        else: # 바다로 막힘
            break
        turn_count = 0
print(result)





