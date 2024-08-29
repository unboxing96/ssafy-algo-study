import sys
sys.stdin = open('input.txt')

"""
x가 3으로 나누어 떨어지면 3으로 나눠
2로 나누어 떨어지면 2로 나눠
1을빼

연산 사용의 최솟값? 출력
10000000 1천만 들어옴.
"""

# 인풋
N = int(input())
# dp 메모이제이션 준비
dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1 # 빼기 count 비교해야지

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1) # dp / 해줬으니 count +1 해줘야지 + 위에 뺀거랑 나누기중 최솟값 찾아야지
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])



# -------------------------------------------------
# dp로 푸는게 맞음 아래처럼돌면 안됨
"""
3 의 배수이면 3을 빼고, 2의 배수이면 2로나누고 6의 배수들은 전부 3으로 나눠
만약 마지막 숫자가 2이면 1로 빼.
"""

# count = 0
#
# N = int(input())
#
# "1이 아닐동안 반복"
# while N != 1 :
#     if N % 2 != 0 and N % 3 != 0:
#         N -= 1
#         count += 1
#     elif N % 2 == 0 and N % 6 != 0:
#         if N / 3 >= 2:
#             N -= 1
#             count += 1
#         else:
#             N = N // 2
#             count += 1
#     elif N % 3 == 0:
#         N = N //3
#         count += 1
#
# print(count)
