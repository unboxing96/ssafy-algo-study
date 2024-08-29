#계단 오르기

"""
마지막 계단 무조건 밟아야 함 (n번째)
i) 1전 계단 밟기 (n-1번째) - 그 전에는 2전 계단을 밟았겠찌 (n-3번째)
ii) 2전 계단 밟기 (n-2번째)
"""

n = int(input())
points = [int(input()) for _ in range(n)]

dp = [0] * (n)

dp[0] = points[0] #첫 번째 계단을 밟기
if n >= 2:
    dp[1] = max(points[0]+points[1], points[1]) #두 번째 계단 밟기
if n >= 3:
    dp[2] = max(points[0]+points[2], points[1]+points[2]) #세 번째 계단 밟기
if n >= 4:
    for i in range(3, n):
        dp[i] = max(points[i]+points[i-1]+dp[i-3], points[i]+dp[i-2])

print(dp[n-1])