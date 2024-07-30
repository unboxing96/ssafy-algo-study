import sys

sys.stdin = open('input.txt')

# https://www.acmicpc.net/problem/3190

# 뱀을 먹으면 길이(길이 1)가 늘어남. 
# 1. 벽에 OR 자기와 부딪히면 게임 끝남.
# 2. input 값 :
# 보드 크기 N 사과 개수 K 다음줄은 행 열 / 
# L 개의 줄에는 방향 변환 정보 X초후 방향 L 혹은 D로 90도 전환
# 몇초만에 게임이 끝날까?



board_size = int(input()) # 보드 크기

board = [[0 for x in range(board_size)]for x in range(board_size)] # 보드 크기만큼 보드 생성
apple_size = int(input()) # 사과 개수
apple = [tuple(map(int,input().split())) for x in range(apple_size)] # 사과 위치 담기 [(3, 4), (2, 5), (5, 3)]

#처음 오른쪽을 향함. 만약 사과를 만나면 이동하지않고 1회 정지(열 카운트 x).
snake = [[0,0]]
# 뱀의 방향을 설정해주기.
snake_direction = 'R' # 뱀이 처음 열로 +1 진행됨. 행,열로 이동.

# 출력 할 초
sec = 0
rotate = int(input()) # 회전 횟수
rotations = [input().split() for rotates in range(rotate)]  # ['3', 'D'], ['15', 'L']


# 뱀의 방향 전환 
def turn(current_direction, rotation):
    directions = ["R", "D", "L", "U"] # 오른쪽 아리 왼쪽 위의 뱀의 방향 
    idx = snake_direction.index(current_direction) # 뱀의 현재 방향의 값을 가지고온 후 idx 에 넣기
    if rotation == 'L':  # 왼쪽 회전
        current_direction = directions[(idx - 1) % 4] # 0 오른쪽 1 아래  2왼쪽 3위를 체크하기위해 %4
    elif rotation == 'D':  # 오른쪽 회전
        current_direction = directions[(idx + 1) % 4]
    return current_direction

# 벡터로도 구현 가능함.
# # 뱀 방향전환 L 이나 D 가 있음.
# def turn(snake_direction, rotation):
#     if rotation == 'L': # 왼쪽 회전
#         return (-snake_direction[1], snake_direction[0]) #
#     elif rotation == 'D': # 오른쪽 회전
#         return (snake_direction[1], -snake_direction[0])

rotation_index = 0
crash = False

# 뱀 움직여보기
while not crash:
    # 초 출력이니 +1
    sec +=1
    # 현재 머리위치 불러오기
    head_y, head_x = snake[-1]


     # 새로운 머리 위치 계산
    if snake_direction == "R":            # 0.0 기준으로 이동할것임
        new_y, new_x = head_y, head_x + 1 # 오른쪽으로 가야하니 행+1추가해주기
    elif snake_direction == "D":
        new_y, new_x = head_y + 1, head_x # 아래로가면 열 + 1
    elif snake_direction == "L":
        new_y, new_x = head_y, head_x - 1 # 왼쪽이니 행 -1
    elif snake_direction == "U":
        new_y, new_x = head_y - 1, head_x # 위쪽이니 열-1

        

    # 벽에 부딪히거나 자기 몸에 부딪히면 게임 종료해야함.
    # 새로운 머리위치는 
    # 열이 0이랑 같거나 이내, 보드사이즈 이내, 행도 0이랑 같거나 보드사이즈 이내 혹은 행열이 
    if not (0 <= new_y < board_size and 0 <= new_x <board_size) or [new_y, new_x] in snake :
        crash = True
        break

    # 머리를 새로운 위치로 이동해주기
    snake.append([new_y, new_x]) 

    # 사과가 있는지 확인
    # 이동한 위치에 사과가 있는지 확인해줘야해.
    # 사과는 3,4에 있지만, 보드는 2,3에 있으니 +1씩해줘서 in체크!
    if (new_y + 1, new_x + 1) in apple:
        apple.remove((new_y + 1, new_x + 1))  # 사과를 먹으면 사과 제거
    else:
        snake.pop(0)  # 사과가 없으면 꼬리 제거.
        # 머리부터 움직였으니 첫번째 인자 제거해줘야지.

     # 회전할 시간인지 확인하고 회전
     # 첫 회전: 로테이션 인덱스 0 보다 입력 3이크고, 시간초가 현재 회전을 진행해야되는지 확인
    if rotation_index < rotate and sec == int(rotations[rotation_index][0]):
        # 뱀 방향을 처음 R로 진행하긴하는데, 방향에 맞춰서 돌려줘야지?
        snake_direction = turn(snake_direction, rotations[rotation_index][1])
        # 뱀 한번더 이동하자.
        rotation_index += 1

print(sec)
    





# 1차 풀이

# # rotate 동안 진행함.
# for i in range(rotate) : 
#     move = list(map(str, input().strip().split())) # 사과를 만나면 이동하지 않고 정지
#     for x in range(move[i]): # 3회 처음 오른쪽 움직이기
        
#         # 벽을 부딪히거나 자기자신에 닿으면 게임 종료
#         if (snake == [board_size, board_size]) or (snake == [0, 0]) or (snake == [1, board_size]) or (snake == [board_size, 1]):
#             crash = True
#             break

#         # snake 움직이기 사과있으면 멈춰!
#         if tuple(snake[0],snake[1]+1) in apple:
#             sec +=1
#         else: 
#             snake[1] += 1
#             sec += 1
#     if crash:
#         break


# for tc in range(1, T+1):
#     (int(input))
#     for apple in (int(input)):
#         pass

# 현재 인풋
# 6  # 보드 크기
# 3 사과 몇개
# 3 4
# 2 5
# 5 3 #사과 위치 담았음 튜플로
# 3 # 뱀 몇번 움직일거니? rotate
# 3 D # 회전 횟수
# 15 L
# 17 D