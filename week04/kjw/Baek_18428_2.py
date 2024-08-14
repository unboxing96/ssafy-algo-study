n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]

# 연구소 문제랑 비슷하게 장애물을 3개 모든 경우의수에 세우고 그때 감시를 피할 수 있는지 확인
# 각 경우마다 T로부터 일직선으로만 탐색, S나 O를 만나면 탐색중지

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def T_virus():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'T':
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    while 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] == 'O':  # 장애물을 만남
                            break
                        if arr[nx][ny] == 'S':  # 학생을 만남
                            return False
                        nx += dx[k]
                        ny += dy[k]
    return True


def search(cnt):
    if cnt == 3:  # 장애물 3개 세운 경우
        if T_virus():
            return True
        else:
            return False

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'  # 장애물 세우기
                if search(cnt + 1):
                    return True
                arr[i][j] = 'X'  # 다시 없애기

if search(0):
    print('YES')
else:
    print('NO')