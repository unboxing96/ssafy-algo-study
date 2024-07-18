# 문제 분석
# 큰 수 최대한 반복 -> 그 다음 큰 수 한 번 -> 큰 수 최대한 반복
# 이것보다 나은 풀이가 있을까 ?

import sys
sys.stdin = open("큰수의법칙.txt", "r")

# n, m, k = map(int, input().split())
# arr = list(map(int, input().split()))

# max1 = sorted(arr)[-1]
# max2 = sorted(arr)[-2]

# tot = 0
# cnt = 1
# while cnt <= m:
#     if cnt % (k + 1) == 0:
#         tot += max2
#     else:
#         tot += max1
#     cnt += 1

# print(tot)

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[-1]
second = arr[-2]

# 가장 큰 수가 등장하는 횟수
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += first * count
result += second * (m - count)

print(result)

