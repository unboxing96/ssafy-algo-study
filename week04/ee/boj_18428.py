# 감시 피하기
import sys
sys.stdin = open("18428_input.txt")

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().split()) for _ in range(N)] # 학생 S, 선생님 T, 아무것도 존재하지 않으면 X

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

teachers = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            teachers.append([i, j])

def can_avoid():
    for i, j in teachers:
        for k in range(4):
            ni = i +di[k]
            nj = j +dj[k]
            while 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 'S': # 학생이 보이면 실패
                    return False
                elif arr[ni][nj] == 'O': # 장애물로 가로막힘
                    break
                ni += di[k]
                nj += dj[k]
    return True

def set_obstacle(count):
    if count == 3: #장애물이 3개가 되면
        if can_avoid():
            return True
        else:
            return False

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X': # 빈 공간에
                arr[i][j] = 'O' # 장애물 세우기
                if set_obstacle(count+1): # 감시 피할 수 있는지 True 반환받으면
                    return True # True 반환하기!
                arr[i][j] = 'X' # 다시 돌려놓기

if set_obstacle(0):
    print("YES")
else:
    print("NO")

