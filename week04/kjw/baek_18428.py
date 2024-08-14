n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]

# 연구소 문제랑 비슷하게 장애물을 3개 모든 경우의수에 세우고 그때 감시를 피할 수 있는지 확인
# 각 경우마다 T로부터 일직선으로만 탐색, S나 O를 만나면 탐색중지

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = False
def T_virus(i, j):
    for k in range(4):
        nx, ny = i, j
        while True:
            nx += dx[k]
            ny += dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 경계를 벗어남
                break
            if arr[nx][ny] == 'O':  # 장애물을 만남
                break
            if arr[nx][ny] == 'S':  # 학생을 만남
                return False
    return True


def search(cnt):
    global result
    if cnt == 3:  # 장애물 3개 세운 경우
        result = True
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 'T':
                    if not T_virus(i, j):
                        result = False
                        break
            if not result:
                break
        return

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':  
                arr[i][j] = 'O'  # 장애물 세우기
                search(cnt + 1)
                arr[i][j] = 'X'  # 다시 없애기
                if result:
                    return

search(0)
if result:
    print('YES')
else:
    print('NO')