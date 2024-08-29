import sys
sys.stdin = open('input.txt')


"""
정수 4를 123합으로 나타내느 7개 수를 1개이상사용.

정수 n이 주어지면 123합으로 나타내는 방법의 수를 구하는 프로그램?
n은 양수이며 11보다 작다

1로 다더하기 가능
2로 다더하기 가능
3로 다더하기 가능

점화식부터 만들기.
n = n-1 + n-2 + n-3
"""
# dp이기에 사용할 필요 x
# for tc in range(1, T+1):


T = int(input())

# 메모이제이션 준비
dp = [0] * 12 # n은 11개보다 작음

dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

# dp 메모이제이션 과정
for i in range(5, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] # 3을만드는 방법은 +1 을 하는거지 4

for _ in range(T):
    n = int(input())
    print(dp[n])