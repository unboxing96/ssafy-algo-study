import sys
sys.stdin = open("02_1_14501_퇴사.txt")

# 뒤에서부터 하자.
# 상담을 완료할 수 있으면 max(dp[n + T[n]] + P[n], dp[n + 1])
# 없으면 dp[n + 1]

n = int(input())
time = [0] * n
price = [0] * n

for i in range(n):
    t, p = map(int, input().split())
    time[i] = t
    price[i] = p

dp = [0] * (n + 1)
for i in range(n-1, -1, -1):
    if i + time[i] <= n:
        dp[i] = max(dp[i + time[i]] + price[i], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])