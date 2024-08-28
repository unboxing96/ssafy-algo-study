# 1로 만들기

n = int(input())
dp = [0] * 1000001

dp[1] = 0
dp[2] = 1
dp[3] = 1

if n > 3:
    for i in range(4, n+1):
        dp[i] = dp[i - 1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i//3] + 1, dp[i])
        if i % 2 == 0:  # 6의 배수면 3으로도 나눠지고 2로도 나눠지니깐 elif로 하면 안되고 if로!!
            dp[i] = min(dp[i//2] + 1, dp[i])

print(dp[n])