import sys
sys.stdin = open("04_1932_정수삼각형.txt")

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = matrix[:]

for i in range(1, n):
    for j in range(len(matrix[i])):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i - 1][j]
        elif j == i:
            dp[i][j] = dp[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i][j] + max(dp[i - 1][j] , dp[i - 1][j - 1])

print(max(dp[n - 1]))