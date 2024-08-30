import sys
sys.stdin = open('input.txt')

"""
그림과 같이 각각의 계단에 점수 얻음
1. 1계단 or 2계단 가능
2. 연속 3번 밟기x
3 마지막 반드시 밟아

"""
stair_count = int(input())

# 메모이제이션 준비
stair = [0] * (stair_count + 1)
dp = [0] * (stair_count + 1)

# 계단의 점수 입력
for i in range(1, stair_count + 1):
    stair[i] = int(input())

# 예외 처리: 계단이 하나 또는 두 개일 경우
if stair_count == 1:
    print(stair[1]) # 런타임 에러떠서 예외처리 진행
elif stair_count == 2:
    print(stair[1] + stair[2])
else:
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])

    for i in range(4, stair_count + 1):
        # 3전에서 뛰고 2칸 올라온 후 본인 / 2칸 한 번에 점프
        dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

    print(dp[stair_count])
