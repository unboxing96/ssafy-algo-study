# 평범한 배낭

import sys
sys.stdin = open("12865_input.txt")

N, K = map(int, input().split()) # 물품의 수 N, 준서가 버틸 수 있는 무게 K
items = [list(map(int, input().split())) for _ in range(N)]

dp = [0]*(K+1)

for w, v in items:
    for i in range(K, -1, -1): # 뒤에서부터
        if i + w <= K: # 1) 최대 무게를 넘지 않고
            if dp[i+w] < dp[i]+v: # value[기존 무게+ 현재 넣을 물건의 무게]< value[기존 무게] + 현재 넣을 물건의 value이면
                dp[i+w] = dp[i]+v #업데이트해주기

print(dp[K])