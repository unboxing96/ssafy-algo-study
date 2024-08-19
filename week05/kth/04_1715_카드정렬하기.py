import sys
sys.stdin = open("04_1715_카드정렬하기.txt")

import heapq

n = int(input())
hq = [int(input()) for x in range(n)]
heapq.heapify(hq)  # 리스트를 최소 힙으로 변환
cnt = 0

while len(hq) > 1:
    # 가장 작은 두 묶음을 꺼내서 합친다
    first = heapq.heappop(hq)
    second = heapq.heappop(hq)
    tmp_sum = first + second
    
    # 합친 결과를 총 비교 횟수에 더하고, 다시 힙에 넣는다
    cnt += tmp_sum
    heapq.heappush(hq, tmp_sum)

print(cnt)
