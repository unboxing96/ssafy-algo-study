import sys
sys.stdin = open('input.txt')
from collections import deque

""""
# M * N 시험관이 있다.
1X1크기의 칸으로 나누어지고 특정한 위치에는 바이러스가 존재 할 수 있다.   
상하좌우 증식 / 단 매초마다 전호가 낮은 종류의 바이러스부터 증식함.  
이미 바이러스가 존재하면 그곳에는 다른 바이러스 X 못들어가 

S초가 지난 후에 X,Y에 존재하는 바이러스의 종류를 출력하는 프로그램.
해당초 해당 위치에 바이러스 없으면 0출력
X,Y는 각각 행렬 의미. 1,1기준으로 시작할것임. 

각 초가 지난이후에는 각 바이러스가 빈자리에만 뿌리기. 단 숫자가 낮은것 먼저 진행.

"""

N, K = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
S, X, Y = map(int,input().split()) #각자 잘들어와야됨

# start_point = [(r, c) for r in range(N) for c in range(N) if matrix[r][c] != 0]



def bfs(matrix,N,S):
    # 이 스타트 포인트는 전체 값을 가지고 오잖아?
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

    queue = deque()
    for r in range(N):
        for c in range(N):
            if matrix[r][c] != 0:
                queue.append((matrix[r][c], r, c)) # 바이러스 값도 입력
    queue = deque(sorted(queue)) # 번호에 따른정렬 sorted써야 시간복잡도 줄임.

    # -----------------------------------------------------------------------------------------------------------------------
    # 백준 시간초과로 파이파이 작동되지만 주석
    # # 바이러스 번호도 추가해봄
    # start_point = [(r, c) for r in range(N) for c in range(N) if matrix[r][c] != 0] # r,c 어떤부분에 뭐가 있는지 알 수 있겠지?
    # #시간초과 파이참은 잘나옴
    # # 작은수부터 담을 수 있는 스타트 포인트를 가질수는 없을까?
    # # for i in range(len(start_point)-1): #스타트 포인트의 길이만큼 순회해줄건데, #sorted안씀
    # #     if start_point[i] > start_point[i+1]: # i값이 더크면 두개 자리바꿔
    # #         start_point[i], start_point[i+1] = start_point[i+1], start_point[i] # 버블정렬할거임 # 값이 뭔지는 몰라도 순서대로 된거잖아?
    # #시간초과...로 sorted를 써봤지만 또한 시간초과... 파이참은 잘 나옴
    # # start_point = sorted(start_point, key = lambda x: matrix[x[0]][x[1]]) #여기에 x는 (0,1)과 같은 값이거든? 여기의 0와 1을 매트릭스에 넣어주는코드얌
    #
    # queue = deque(sorted(start_point))
    # -----------------------------------------------------------------------------------------------------------------------

    for _ in range(S):
        length = len(queue)
        for _ in range(length):
            virus_num, recent_x, recent_y = queue.popleft()  # x,y 좌표를 넣어주면 됨. 각 값이 들어있을거잖아 아직 퍼지기 전.
            for dr, dc in directions:
                new_x, new_y = recent_x + dr, recent_y + dc
                if 0 <= new_x < N and 0 <= new_y < N and matrix[new_x][new_y] == 0:
                    matrix[new_x][new_y] = matrix[recent_x][recent_y]  # 현재값을 새로운곳에 넣어줘바 상하좌우로
                    queue.append((virus_num, new_x, new_y))
    return matrix
    # -------------------------------------------------------------------------------------------------
    # while queue: # 1번만 하면됨.
    #     recent_x, recent_y = queue.popleft() # x,y 좌표를 넣어주면 됨. 각 값이 들어있을거잖아 아직 퍼지기 전.
    #     for dr, dc in directions:
    #         new_x, new_y = recent_x + dr, recent_y + dc
    #         if 0 <= new_x < N and 0 <= new_y < N and matrix[new_x][new_y] == 0:
    #             matrix[new_x][new_y] = matrix[recent_x][recent_y] #현재값을 새로운곳에 넣어줘바 상하좌우로
    # return matrix
    # -------------------------------------------------------------------------------------------------

matrix = bfs(matrix, N,S)
print(matrix[X-1][Y-1])


# ------------------------------------------------------------------------------------
#결과적으로 안쓰게 된 코드
    # queue = deque(start_point)
    # while queue: # 1번만 하면됨.
    #     recent_x, recent_y = start_point # x,y 좌표를 넣어주면 됨.


# 전체를 탐색하면서 1 ~ 1000개 사이의 바이러스를 순회할거야.
# 아래 코드는 지금 전체탐색을하면서 1부터 싹채우고 나머지 코드를 돌잖아?
#
# def bfs(N,K):
#     for r in range(N):
#         for c in range(N): # 모든배열을 순환한대.
#             for j in range(1, K + 1):  # 결국 N번의 배열을 도는데, 4방향으로 K를기준으로 작은수부터 다돌면 되는거잖아?
#                 if matrix[r][c] == j:  # 만약
#                     for k in range(4):
#                         nr = r + dr[k]
#                         nc = c + dc[k]
#                         if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] ==0:
#                             matrix[nr][nc] = j
#                 #  1일때 상하좌우 다채움
#             # 여기까지 돌아야 전체 1,2, 다도는것임.
#     return