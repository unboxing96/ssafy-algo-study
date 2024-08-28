n = int(input())
dp = [0]*(n+1)
# dp내에 연산사용 최솟값 저장
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1     # 우선 1빼는 방법
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 아우 이거 elif로 하면 안됨!
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])