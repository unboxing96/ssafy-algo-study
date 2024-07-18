import sys
sys.stdin = open("일이될때까지.txt", "r")

# 문제 분석
# 나누는 게 항상 좋다.
# 나누어 떨어질 때까지 빼고, 나누어 떨어지면 나누자.

# n, k = map(int, input().split())
# cnt = 0

# while n > 1:
#     if n % k == 0:
#         n //= k
#         cnt += 1
#     else:
#         n -= 1
#         cnt += 1

# print(cnt)

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k # n 이하의 k 배수 중 가장 큰 값. (e.g. n = 25, k = 3 이라면 -> 24)
    result += (n - target) # 빼기 횟수 (e.g. 25 - 24 = 1)

    n = target

    if n < k:
        break

    n //= k
    result += 1

result += (n - 1) # 1을 만드는 것이니까 n이 아닌 n - 1
print(result)
