import sys
sys.stdin = open('input.txt')


"""
여러채의 집이 위치함
특정 집에 한개의 안테나 설치 ( 안테나로부터 모든집 까지의 거리의 총합이 최소 목표)
집이 위치한곳에만 설치가능 / 동일한 위치에 여러개의 집이 존재 가능.

1. 집의 위치를 정렬하고
2. 처음과 끝의 집의 중간값을 찾기. 첫집 + 마지막집 / 2
3. 그 중간값이 정답임
"""


# 집의 수
N = int(input())
# 1. 집의 위치 받아서 동일집 없애주기
house_location = set(map(int, input().split()))

# 정렬하기
house_location = sorted(house_location)

# 값을 인덱스로 가지와야 정확한 중간값을 체크할 수 있음.
middle_location = ((N-1) // 2)

print(house_location[middle_location])

# 아래와 같이 정렬하면, 1,1,1,1, 10000에서 문제 발생
# middle_location = ((house_location[0] + house_location[-1]) // 2)







# --------------------------------------------------------------------------------------------
# 정답인데 시간초과
# 집의 수
# N = int(input())
# # 1. 집의 위치 받아서 동일집 없애주기
# house_location = set(map(int, input().split()))
#
# # 정렬하기
# house_location = sorted(house_location)
# result = 200000
# check_num = 0
#
# # 2. 나로부터 얼마나 떨어졌나 체크해야됨.
# # 2-1 모든 리스트를 순회하면서 각값을 빼준 합 저장
#
# for i in range(len(house_location)):
# #     check_sum = 0
# #
# #     for j in range(len(house_location)):
#         # 뒤에서 -1씩 진행하는 인덱스와 앞부터 비교하는 인덱스를 더해가면서 구해주기
#         A =  abs(house_location[i] - house_location[j]) # 본인 빼기 다음 인덱스
#         check_sum += A # checksum에 더해줘.
#
#     if check_sum < result:
#         result = check_sum
#         check_num = house_location[i]
#
# print(check_num)



""""
1. 집의 위치를 정렬하고
2. 처음과 끝의 집의 중간값을 찾기. 첫집 + 마지막집 / 2
3. 그 중간값 으로 부터 가까운곳 찾기
3-1 만약 중간값이 5 이고 5에 집이없고 3과 6에 있으면 어떻게 비교할거야?:
    if 5+1 in [house_location] or 5-1 in [house_location]:
    중간값에서 +-1 한것이 house location에 있으면 print하고 없으면 i값을 더하면되겠찌? (houselocation의 절반만순회하면돼)
    


----------------------------------------------------------------------
필요없어진 코드
# middle_location = ((house_location[0] + house_location[-1]) // 2)
# 
# # 3. 그 중간값 으로 부터 가까운곳 찾기
# def check_antenna_house(middle_location):
#     for i in range(1, (len(house_location)//2 +1)):
#         if middle_location in house_location:
#             return middle_location
# 
#         if middle_location + i in house_location:
#             return middle_location + i
#         elif middle_location - i in house_location:
#             return middle_location - i
#     else: return -1
# 
# 
# 
# 
# print(check_antenna_house(middle_location))
"""