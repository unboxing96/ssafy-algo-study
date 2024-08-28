import sys
sys.stdin = open("01_1_1463_1로만들기.txt")

# 문제 분석
# 3가지 조건을 모두 확인해서 dp 테이블을 업데이트한다.

n = int(input())
dp = [0] * (n + 1) # i 위치를 1로 만들기 위해 필요한 연산 횟수

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])

print(dp[n])