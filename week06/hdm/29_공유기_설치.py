# 1일차: 백준 2110 공유기 설치(교재 29번)
# 2일차: 프로그래머스 입국심사
# 3일차: 프로그래머스 가사 검색 (교재 30번)
# 4일차: 백준 12015 가장 긴 증가하는 부분 수열2
# 5일차: 백준 32136 소신발언
#
#
# 필수 풀이: 1, 3일차 문제
# 선택 풀이: 2, 4, 5일차 문제
# - 백준 2805 나무자르기
# - 백준 1654 랜선자르기
# - 백준 2470 두 용액


import sys
sys.stdin = open('input.txt')

"""
도현이집 N개 수직선 위에 있음.
공유기 c개 설치하려함. 최대한 많은곳에 와이파이 사용하려함.
가장 인접한 두 공유기 사이의 거리르 가능한 크게하려함.

적당히 공유기 설치하고, `가장인접`한 공유기 최대거리 

1 2 3 이렇게 설치하면  = 거리 1
1 3 5 = 거리 2
1 4 8 = 거리 3
1 4 9 = 거리 3

가장인접한게 1
1 2 4
가장 인접한게 2
1 4 8
가장 인접한게 3
1 4 8 / 1 4 9
가장 인접하게 4
1 8 9 못만들어. 1됨.
집간의 거리 체크 필요. 

x 변수

i + 1 - i = 둘 사이의 거리. 최대까지 진행 언제까지?
if 둘사이의 거리가 어떠한 변수 x 보다 크면 저장


"""

N, C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)]) # [1, 2, 4, 8, 9]

max_distance = house[-1] - house[0]
d = 1
# d를 1부터 1씩 증가하면서 c만큼 진행해보기
result=0

while d <= max_distance :
    mid = (d + max_distance) // 2
    value = house[0]
    count = 1
    for i in range(1, N):
        if house[i] >= value + mid:
            value = house[i]
            count +=1
    if count >= C:
        d = mid +1
        result = mid
    else:
        max_distance = mid -1
print(result)





#------------------------------------------------

# X
# need = N // (C-1)
#
# result = house[need] - house[0]
#
# print(result)