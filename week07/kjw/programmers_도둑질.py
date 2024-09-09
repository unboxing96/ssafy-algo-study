def solution(money):
    n = len(money)
    # 처음꺼를 뽑을 때 >> 마지막꺼 못뽑음
    dp = [0]*n
    fir_money = money[:-1]
    dp[1] = fir_money[0]
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + fir_money[i-1])
    fir = dp[n-1]

    # 마지막꺼를 뽑을 때 >> 처음꺼 못 뽑음
    dp = [0]*n
    sec_money = money[1:]
    dp[1] = sec_money[0]
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + sec_money[i-1])
    sec = dp[n-1]

    answer = max(fir, sec)
    return answer

