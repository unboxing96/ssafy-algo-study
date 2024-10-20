T = int(input())
for _ in range(1, T+1):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        # 점화식으로 나타내면 dp(n) = dp(n-1) + dp(n-2) + dp(n-3)
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        print(dp[n])