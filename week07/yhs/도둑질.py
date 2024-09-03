def solution(money):
    dp = [[] for _ in range(len(money))]

    for i in range(len(money)):
        if i == 0:
            dp[0] = [money[0], 0]   # [첫번째 집부터 터는 경우, 두번째 집부터 터는 경우]
        elif i == 1:
            dp[1] = [0, money[1]]
        elif i == 2:
            dp[2] = [dp[0][0] + money[2], dp[0][1] + money[2]]
        elif i == len(money)-1:     # 마지막 집을 터는 경우: 첫번째 집과 같이 털 수 없음
            dp[i] = [max(dp[i-2][0], dp[i-3][0]), max(dp[i-2][1] + money[i], dp[i-3][1] + money[i])]
        else:
            dp[i] = [max(dp[i-2][0] + money[i], dp[i-3][0] + money[i]), max(dp[i-2][1] + money[i], dp[i-3][1] + money[i])]

    return max(max(dp[-1]), max(dp[-2]))
