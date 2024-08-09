from copy import deepcopy
from collections import deque


def wall(lab, *args):
    # 벽 세우기
    walled_lab = deepcopy(lab)  # 원본 행렬 바뀌는 것 방지하기 위해 copy 모듈 사용

    # *args(3개)의 좌표에 벽 세우기
    for coor in args:
        walled_lab[coor[0]][coor[1]] = 1

    return walled_lab


def bfs(lab, virus):
    infected = deepcopy(lab)
    # delta
    drow = [1, 0, -1, 0]
    dcol = [0, 1, 0, -1]

    queue = deque(virus)    # 큐에 바이러스 위치 넣기
    # bfs 시작
    while queue:
        s = queue.popleft()
        # 인접행렬 탐색하기
        for i in range(4):
            row = s[0]+drow[i]
            col = s[1]+dcol[i]
            # 인덱스 범위 내에 있고 빈 칸일 경우 바이러스 감염
            if 0 <= row < n and 0 <= col < m and not infected[row][col]:
                queue.append([row, col])    # 큐에 추가
                infected[row][col] = 2      # 방문처리

    # 안전 영역 개수 세기
    count = 0
    for r in infected:
        for c in r:
            if c == 0:
                count += 1

    return count


def backtracking(depth, max_area):
    # 깊이가 3까지 도달하면 bfs 함수 호출하여 안전 영역 구하기
    if depth == 3:
        walled = wall(lab, *arr)
        area = bfs(walled, virus)

        return area

    # 가장 최근에 방문한 노드의 인덱스 구하기
    if True in visited:
        idx = length - visited[::-1].index(True)
    else:
        idx = 0

    # 가장 최근에 방문한 노드의 다음 인덱스부터:
    for i in range(idx, length):
        # 방문하지 않았을 경우
        if not visited[i]:
            visited[i] = True   # 방문 처리 후
            arr[depth] = empty[i]   # 벽을 세울 위치 리스트에 추가
            temp = backtracking(depth + 1, max_area)    # backtracking 재귀호출, return 값(bfs 결과) temp에 저장
            visited[i] = False  # 방문한 노드 초기화
            # 안전 영역의 최대값 갱신하기
            if temp > max_area:
                max_area = temp

    return max_area

'''
1. 벽을 세울 수 있는 위치(빈 칸)을 리스트에 모두 담는다
2. 백트래킹으로 리스트 내 원소가 3개인 부분집합 모두 구한다
3. 모든 부분집합에 대하여 bfs 실시
4. bfs 실행한 결과 안전 영역의 최대 개수 구하기
'''


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

empty = []  # 여기에 빈 칸의 좌표들이 들어감
virus = []  # 여기에 바이러스의 좌표들이 들어감
length = 0  # 벽 세우기 전의 빈 칸 개수

# 행렬 조회하며 빈 칸과 바이러스 위치 확인
for i in range(n):
    for j in range(m):
        filled = lab[i][j]
        if not filled:
            empty.append([i, j])    # 빈 칸 좌표 추가
            length += 1             # 빈 칸 개수 하나 추가
        if filled == 2:
            virus.append([i, j])    # 바이러스 좌표 추가

visited = [False for _ in range(length)]    # 방문여부 체크하는 리스트
arr = [0, 0, 0]                             # 길이 3짜리 리스트에 세울 벽의 위치 담기
result = backtracking(0, 0)
print(result)
