# 백준 1715번 카드 정렬하기

'''
heap에 대한 사전학습 필요

- heap이란 ?
힙은 특정한 규칙을 가지는 트리로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 한다.

힙 property: A가 B의 부모노드이면 A의 키값과 B의 키값 사이에는 대소 관계가 성립한다.
최소 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
최대 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙

이러한 속성으로 인해 힙에서는 가장 낮은(혹은 높은) 우선순위를 가지는 노드가 항상 루트에 오게 되고 이를 이용해 우선순위 큐와 같은 추상적 자료형을 구현할 수 있다.
이때 키값의 대소 관계는 부모 / 자식 간에만 성립하고, 형제노드 사이에는 대소 관계가 정해지지 않는다.
'''

import sys
import heapq

N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

heapq.heapify(num_list)
ans = 0

for i in range(N-1):
    num1 = heapq.heappop(num_list)
    num2 = heapq.heappop(num_list)
    min_sum = num1 + num2
    ans += min_sum
    heapq.heappush(num_list, min_sum)

print(ans)
