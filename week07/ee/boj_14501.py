# 퇴사

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0]*(n+1) #그 날짜의 최대 수익

for i in range(1, n+1):
    T, P = arr[i-1]
    if i+T-1 <= n:
        dp[i+T-1] = max(dp[i+T-1], dp[i-1]+P)
    dp[i] = max(dp[i-1], dp[i])

print(dp[n])