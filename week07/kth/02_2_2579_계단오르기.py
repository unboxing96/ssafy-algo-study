import sys
sys.stdin = open("02_2_2579_계단오르기.txt")

# 문제 분석
# 마지막 계단은 반드시 밟아야 한다.
# 그렇다면 그전은 ?
    # f(n - 2)
    # f(n - 1) -> 문제가 있다. 이전에 밟은 것이 n - 1이면 조건에 위배된다.
# 점화식으로 나타내면 아래와 같다.
# dp[n] = max(arr[n] + dp[n - 2], arr[n] + arr[n - 1] + dp[n - 3])

n = int(input())
arr = [0] * 301
for i in range(1, n + 1):
    arr[i] = int(input())

dp = [0] * 301 # 해당 인덱스를 밟고 있는 경우, 해당 인덱스까지의 최댓값
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
dp[3] = max(arr[1] + arr[3], arr[2] + arr[3])
for i in range(4, n + 1):
    dp[i] = max(arr[i] + arr[i - 1] + dp[i - 3], arr[i] + dp[i - 2])

print(dp[n])
