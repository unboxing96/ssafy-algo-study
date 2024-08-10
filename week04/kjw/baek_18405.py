import copy
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
new_arr = copy.deepcopy(arr)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def virus(a, b, l):  # a,b에서 l 바이러스를 퍼뜨림
    for q in range(4):
        nx = a + dx[q]
        ny = b + dy[q]
        if 0 <= nx < n and 0 <= ny < n:
            if new_arr[nx][ny] == 0:  
                new_arr[nx][ny] = l

def dfs(arr, new_arr):    
    # 각 바이러스 위치에서 바이러스를 퍼뜨림
    time = 0
    while time < s:
        for i in range(n):
            for j in range(n):
                for l in range(1,k+1):
                    if arr[i][j] == l:
                        virus(i, j, l)
        arr = copy.deepcopy(new_arr)
        time += 1

dfs(arr, new_arr)

print(new_arr[x-1][y-1])
# 문제에서 인덱스가 1부터 시작하므로 우리는 x-1, y-1 의 종류를 출력하면됨