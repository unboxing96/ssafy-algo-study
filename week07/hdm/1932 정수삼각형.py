import sys
sys.stdin = open('input.txt')

"""
삼각형의 크기가 500까지임.많이 큼. 
"""


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)] #[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

dp = [[0] * (i+1) for i in range(N)] # [[7], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]

dp[0][0] = arr[0][0]


def topdown(i,j):
    # 기저 조건 i랑 j가 0 이면 탈출
    if i == 0 and j == 0:
        return arr[0][0]
    # dp에 저장된 값이 없으면 탐색 시작
    if dp[i][j] == 0:
        # 제일 왼쪽 열 처리
        if j == 0:
            dp[i][j] = arr[i][j] + topdown(i-1, j)
        # 제일 오른쪽 열 처리리        elif j == i:
            dp[i][j] = arr[i][j] + topdown(i-1, j-1)
        else:
            dp[i][j] = arr[i][j] + max(topdown(i-1, j-1), topdown(i-1, j)) # 대각선들 처리
    return dp[i][j]


result = max(topdown(N-1, j) for j in range(N)) # 맨 아래서부터 위치찾기
print(result)


# 최대값으로만 지나가는 길로는 아래로 풀 수 있음. 반례: 작은 값으로 진행했는데 > 최대값이 될 수도 있음.
# 즉 지금까지의 최대값을 구하는 dp[i]의 루트가 dp[i+1]의 최대값을 보장할 수 없음.
# 단일 경로를 추적하고있음!
#
# dp[1] = arr[0][0]
#
# j = 0
# for i in range(1, N):
#     if (dp[i] + arr[i][j]) > (dp[i] + arr[i][j + 1]):
#         j = j
#         dp[i+1] = dp[i] + arr[i][j]
#     else:
#         dp[i + 1] = (dp[i] + arr[i][j + 1])
#         j = j+1
# print(dp[N])
