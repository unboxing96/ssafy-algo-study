import sys
sys.stdin = open("03_10159_저울.txt")

# 문제 분석
# 플로이드 워셜
# 각 행에서 업데이트 되지 않은 노드의 개수를 출력하라.

n = int(input())
m = int(input())
distance = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    distance[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if distance[i][k] and distance[k][j]: # 다른 모든 노드(k)를 확인하여 연결이 되면
                distance[i][j] = 1
                
for i in range(1, n + 1):
    tmp_cnt = 0
    for j in range(1, n + 1):
        if distance[i][j] == 0 and distance[j][i] == 0: # i가 다른 모든 j와 연결되지 않은 경우
            tmp_cnt += 1
    print(tmp_cnt - 1)