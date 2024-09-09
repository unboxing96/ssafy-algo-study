import sys
sys.stdin = open("03_12865_평범한배낭.txt")

# 문제 분석
# 0,1 배낭 문제
# dp 배열: 행은 물건, 열은 각 한계 무게 이하에서 최댓값을 저장

n, k = map(int, input().split())
bags = [[0, 0]]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n):
    bags.append(list(map(int, input().split())))

for i in range(1, n + 1): # 물건 개수만큼
    weight, value = bags[i - 1][0], bags[i - 1][1]

    for weight_limit in range(1, k + 1): # 무게 한계만큼
        if weight_limit < weight: # 한계 무게보다 현재 무게가 크다면 담을 수 없다.
            dp[i][weight_limit] = dp[i - 1][weight_limit] # 이전 단계의 값을 그대로
        else:
            dp[i][weight_limit] = max(dp[i - 1][weight_limit], value + dp[i - 1][weight_limit - weight])

print(max(dp[n]))