from collections import deque

def function(arr, s, k, n, row, col):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # category의 i번째 인덱스에 모든 i+1번 바이러스 위치 넣기
    for i in range(n):
        for j in range(n):
            virus = arr[i][j]
            if virus:
                category[virus-1].append([i, j])

    queue = deque(category)

    time = 0

    while queue:
        if time == s or arr[row][col]:  # s초가 지났거나 (x,y)에 이미 바이러스가 전염됐을 경우 return
            # for _ in arr:
            #     print(_)
            return arr[row][col]

        for i in range(k):      # i+1번 바이러스에 대하여
            v = queue.popleft() # i+1번 바이러스 위치 리스트
            next_category = []  # 다음 턴에 큐에 넣을 i+1번 바이러스 위치 리스트

            for spot in v:  # 각 i+1번 바이러스에 대해
                for j in range(4):  # 인접노드 탐색
                    nx = spot[0] + dx[j]
                    ny = spot[1] + dy[j]
                    if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
                        arr[nx][ny] = i+1
                        next_category.append([nx, ny])
            queue.append(next_category)
        time += 1

    '''
    1~k번 바이러스 차례대로 증식
    인접 노드가 0일 경우에만
    x, y 확인
    만약 s초 전에 x, y에 바이러스가 채워졌다면 ?
    그냥 바이러스 종류 return
    '''


n, k = map(int, input().split())
testtube = [list(map(int, input().split())) for _ in range(n)]
category = [[] for _ in range(k)]
s, x, y = map(int, input().split())

answer = function(testtube, s, k, n, x-1, y-1)
print(answer)
