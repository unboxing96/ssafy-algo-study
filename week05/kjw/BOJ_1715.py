import heapq
n = int(input())
numbers = [int(input()) for _ in range(n)]

total = 0
heapq.heapify(numbers)      # 힙은 최소값 추출이 기본

while len(numbers) > 1:         # 2개를 빼야하므로, 인덱스 실수 하지말기
    a = heapq.heappop(numbers)      # 가장 작은값 추출
    total += a
    b = heapq.heappop(numbers)      # 두번째로 작은값 추출
    total += b
    c = a+b
    heapq.heappush(numbers, c)         # 그 값 더한거 힙에 다시 넣어주기


print(total)