def solution(money):
    dp = [0] * len(money)
    # 첫집을 무조건 털 경우.
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])

    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i - 1], money[i] + dp[i - 2])
    # 마지막집 털면 x 안됨
    a = max(dp)


    # 두번째 집부터 털기
    sec_dp = [0] * len(money)
    sec_dp[1] = money[1]

    for i in range(2, len(money)):
        sec_dp[i] = max(sec_dp[i - 1], money[i] + sec_dp[i - 2])
    b = max(sec_dp)

    result = max(a, b)

    return result


"""
인접한 집들과 방범 장치가 연결되어있음
인접한 두 집을 털면 경보 울림
도둑이 훔칠돈의 최대값?

# 3집은 1집의 최대값
# 4집은 2집의 최대값
# 5집은 3집의 최대값

# 첫집은 그냥 첫 번째 돈
# 둘째집은 그냥 두번째 돈
# 세번째집은 ???
두번째 돈이 크면 두번째 돈쓰고 첫번째 돈이 크면 + 지금 세번째돈이랑 비교해봐!
어? 

"""