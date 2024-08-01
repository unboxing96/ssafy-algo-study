def change_dir(idx, sec, turn):
    for _ in turn:
        if sec == _[0]:
            if _[1] == 'L':
                # print('turn left')
                return (idx+1)%4
            elif _[1] == 'D':
                # print('turn right')
                return (idx-1)%4
    return idx
    

N = int(input())
graph = [[0 for i in range(N)] for i in range(N)]
graph[0][0] = 1

# 사과 위치 인덱스 저장
K = int(input())
apples = []
for i in range(K):
    row, col = map(int, input().split())
    apples.append([row-1, col-1])

# 방향 변환 정보
L = int(input())
turn = []
for i in range(L):
    sec, direction = input().split()
    turn.append([int(sec), direction])


drow = [0, -1, 0, 1]
dcol = [1, 0, -1, 0]


# 초기값
dir_idx = 0         # 방향 리스트 인덱스
sec = 0             # 시간
cur_row, cur_col = 0, 0     # 현재 머리 위치
path = [[0, 0]]             # 뱀 좌표

while True:
    sec += 1
    
    # 진행할 위치
    goto = [cur_row+drow[dir_idx], cur_col+dcol[dir_idx]]

    # 자기 몸과 만나거나 벽에 부딪히면 종료
    if goto in path or (goto[0]<0 or goto[0]>N-1 or goto[1]<0 or goto[1]>N-1):
        break
    
    # goto에 사과 있는지 확인
    for i in range(len(apples)):
        if goto == apples[i]:
            path.append(goto)
            apples.pop(i)           # 사과 제거
            break
    else:
        poin = path.pop(0)
        # graph[poin[0]][poin[1]] = 0
        path.append(goto)


    # 위치 갱신
    cur_col = goto[1]
    cur_row = goto[0]

    # 방향 바꾸기
    dir_idx = change_dir(dir_idx, sec, turn)

    
    # graph[goto[0]][goto[1]] = 1
    # for _ in graph:
    #     print(_)
    
    # print('-------------------')
    # print(path)

print(sec)