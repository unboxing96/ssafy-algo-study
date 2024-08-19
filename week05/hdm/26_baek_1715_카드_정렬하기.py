import sys
import heapq
sys.stdin = open('input.txt')

N = int(input())
card_list = [int(input()) for _ in range(N)] #[10, 20, 40]


heapq.heapify(card_list)  ## 최소힙으로 변환

total_sum = 0

while len(card_list) > 1: # 카드 리스트 수 만큼 순회

    comparison1 = heapq.heappop(card_list) # 최소힙꺼내고 정렬
    comparison2 = heapq.heappop(card_list)

    sum_comparison = comparison1 + comparison2
    heapq.heappush(card_list, sum_comparison) # sum comparison을 cardlist에 넣고 힙에 넣어 재정렬

    total_sum += sum_comparison

print(total_sum)


# 생각을 다시하자
#-----------------------------------------
# sorted_card = sorted(card_list)
#
# total_sum = 0
#
# comparison = sorted_card[0]
#
# for i in range(len(sorted_card)-1):
#     comparison += sorted_card[i+1]
#     total_sum += comparison
#
# if len(sorted_card) == 1 :
#     print(sorted_card[0])
# else: print(total_sum)