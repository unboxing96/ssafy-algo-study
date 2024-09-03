import sys
sys.stdin = open("1932_input.txt")

n = int(input()) #삼각형의 크기
triangles = [list(map(int, input().split())) for _ in range(n)]

"""
양 옆이랑 가운데 분리하기.......
"""
dp = [[0] * (k+1) for k in range(n)]
dp[0][0] = triangles[0][0]

for i in range(1, n): #행
    for j in range(i+1): #열
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangles[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangles[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + triangles[i][j], dp[i-1][j] + triangles[i][j])

print(max(dp[n-1]))
