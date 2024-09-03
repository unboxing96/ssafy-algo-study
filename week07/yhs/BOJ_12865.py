import sys

n, k = map(int, input().split())

items = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    if w <= k:
        items.append([w, v])      # 물건의 무게가 배낭에 넣을 수 있는 무게보다 큰 경우는 제외

n = len(items)

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]      # 행: 무게 / 열: item

for i in range(1, n+1):              # [무게, 가치]
    w, v = items[i-1][0], items[i-1][1]

    for j in range(1, w):           # i번째 물품의 무게(w_i)보다 작은 행의 테이블 : 현재 반복에서 갱신되지 않으므로 i-1번째 테이블의 정보를 그대로 가져옴
        dp[j][i] = dp[j][i-1]

    for j in range(w, k+1):         # w_i번째 행부터는 i-1번째 테이블의 값과 비교했을 때 더 큰 값으로 갱신
        dp[j][i] = max(dp[j][i-1], v + dp[j-w][i-1])

print(dp[-1][-1])
