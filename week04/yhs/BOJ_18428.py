def block(depth):
    """
    장애물을 세울 수 있는 경우 완전탐색
    복도의 모든 좌표를 탐색하며 빈 칸일 경우 장애물을 세우고, 깊이를 1 늘려 함수를 재귀호출한다.
    깊이가 3이 될 경우(장애물을 3개 세웠을 때) validation 함수를 호출하여 모든 학생들을 감시로부터 피하도록 할 수 있는지 확인한다.
    validation 함수는 모든 학생들을 선생님의 시야를 가릴 수 있을 때 True를, 아니면 False를 반환
    validation의 결과가 True가 나오는 경우 즉시 True를 반환한다.
    모든 경우의 수를 탐색한 결과 학생들을 감시로부터 피하도록 하지 못한다면 최종적으로 False를 반환한다.
    """

    # 장애물 3개 세웠으면 모든 학생들 가릴 수 있는 지 확인
    if depth == 3:
        return validation()     # True면 가릴 수 있음/False면 불가

    for i in range(n):
        for j in range(n):
            what = aisle[i][j]
            if what == 'X':         # 빈 공간인지 확인
                aisle[i][j] = 'O'   # 빈 공간이면 장애물 세우기
                result = block(depth+1)
                if result:          # 모든 학생들 가릴 수 있는 경우의 수 등장 시 바로 return True
                    return True
                aisle[i][j] = 'X'   # 장애물 원복
    # 경우의 수 없으면 return False
    return False


def validation():
    """
    모든 선생님들의 좌표로부터 상하좌우 모든 칸을 탐색한다.
    탐색한 칸이 빈 칸이라면 k(delta에 곱해줄 계수)의 값을 늘려 다음 칸을 탐색한다.
    탐색한 칸에 학생이 있다면 바로 False를 반환한다.
    탐색한 칸에 선생님 혹은 장애물이 있다면 다음 반복으로 넘어간다.
    이를 인덱스 범위를 벗어나기 전까지 반복.
    모두 탐색한 결과 선생님의 시야에 학생이 들어오지 않는다면 True를 반환한다.
    """
    drow = [1, 0, -1, 0]
    dcol = [0, 1, 0, -1]

    for teacher in teachers:
        row, col = teacher  # row, col : 선생님이 위치한 행과 열 좌표
        for i in range(4):
            k = 1   # delta에 곱해줄 계수
            dr = drow[i]
            dc = dcol[i]
            while 0 <= row + k * dr < n and 0 <= col + k * dc < n:
                r = row + k * dr    # 탐색할 행
                c = col + k * dc    # 탐색할 열
                coor = aisle[r][c]
                if coor == 'X':     # 빈 칸이라면 다음 칸 탐색
                    k += 1
                elif coor == 'S':   # 학생이 있다면 바로 return False(학생 가릴 수 없는 case)
                    return False
                else:               # 그 외(선생님이거나 장애물) : 다음 반복으로
                    break

    return True     # 선생님의 시야 모두 확인했는데 학생이 보이지 않는다면 return True(모든 학생들을 가릴 수 있는 경우)


n = int(input())
aisle = [(list(input().split())) for _ in range(n)]
teachers = []   # 선생님 위치
for i in range(n):
    for j in range(n):
        who = aisle[i][j]
        if who == 'T':
            teachers.append([i, j])

answer = block(0)   # 인자 : 재귀깊이

if answer:
    print('YES')
else:
    print('NO')
