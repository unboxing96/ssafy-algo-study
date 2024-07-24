import sys
sys.stdin = open("만들수없는금액.txt", "r")

# 문제 분석
# 주어진 동전으로 만들 수 '없는' 금액 중 '최솟값'을 return

# 접근
# 동전의 개수도 1,000개인데 O(N ** 2) 해버리자 -> 안 되지 .. 두 개의 쌍으로만 하는 게 아니니까.
# 사실상 조합이라서 O(2 ** N)
# 조합 말고 ... 그리디 하게 ...
# [1, 1, 1, 2, 5, 9]

n = int(input())
data = list(map(int, input().split()))

data.sort()

target = 1
for elem in data:
    if target < elem:
        break
    target += elem

print(target)