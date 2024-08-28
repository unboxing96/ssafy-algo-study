# 1, 2, 3 더하기

T = int(input())

dp = [0] * 12
dp[1] = 1
dp[2] = 2 # 1+1, 2
dp[3] = 4 # 1+1+1, 1+2, 2+1, 3

for _ in range(T):
    n = int(input())
    for i in range(n+1):
        if dp[i] != 0: #이미 값이 있으면
            continue
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])