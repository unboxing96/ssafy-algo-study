# 문제 분석
# 인접한 두 원소를 방문할 수 없다.

# 접근
# 선형 배열이라면 ?
# 이전 값을 그대로 가져오거나, 현재 칸 + 2개 이전 칸
# dp[n] = max(dp[n - 1], arr[n] + dp[n - 2])

# 원형 배열이라면 ?
# case 1: 처음 O, 마지막 X
# case 2: 처음 X, 마지막 O

def solution(money):
    n = len(money)
    
    # case 1: 처음 O, 마지막 X    
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, n - 1): # 마지막 원소 제외
        dp1[i] = max(dp1[i - 1], money[i] + dp1[i - 2])

    # case 2: 처음 X, 마지막 O
    dp2 = [0] * n
    dp2[1] = money[1] # 처음을 방문하지 않으므로 dp2[0] == 0
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])

    return max(dp1[n - 2], dp2[n - 1]) # dp1은 마지막 원소 제외