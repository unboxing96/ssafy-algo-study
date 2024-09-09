def solution(money):
    """
    1) 집은.. 첫 번째 집을 털거나 마지막 집을 털거나 둘 중 하나
    첫 번째 집을 털면 마지막 집은 못 턴다

    2) i+2 번째 집 or i+3 번째 집을 털 수 있음
    """
    answer = 0

    N = len(money)
    dp = [0] * N

    dp[0] = money[0]
    dp[1] = money[1]
    dp[2] = money[0] + money[2]

    for i in range(3, N-1):
        dp[i] = max(dp[i-2], dp[i-3]) + money[i]

    tmp1 = max(dp)

    dp = [0] * N

    dp[1] = money[1]
    dp[2] = money[2]

    for i in range(3, N):
        dp[i] = max(dp[i-2], dp[i-3]) + money[i]

    tmp2 = max(dp)

    answer = max(tmp1, tmp2)
    return answer

print(solution([1, 2, 3, 1])) #4