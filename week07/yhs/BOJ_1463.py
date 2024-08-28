n = int(input())

dp = [0 for _ in range(n+3)]

dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    # i를 만들 수 있는 경우 : ? x 3 / ? x 2 / ? + 1
    # i를 만드는 데 필요한 최소 연산 횟수 : 위의 연산하기 전 수를 만드는데 필요한 최소 연산 횟수 + 1
    tmp = dp[i-1] + 1
    if i % 3 == 0:
        tmp = min(dp[i//3] + 1, tmp)
    if i % 2 == 0:
        tmp = min(dp[i//2] + 1, tmp)

    dp[i] = tmp

print(dp[n])