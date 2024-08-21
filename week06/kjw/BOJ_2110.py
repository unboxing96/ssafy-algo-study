import sys
sys.stdin = open("input.txt")
'''
이진 탐색을 하기 위해 집들의 위치 오름 차순 정렬
가능한 최소 거리 1, 가능한 최대 거리는 가장 멀리 떨어진 두 집의 거리 house[-1] - house[0]

이진탐색은 mid값을 return 하는 것이니까 문제에서 구하고자 하는 값을 mid로 잡자고 생각
>> 이진 탐색의 mid를 최소 거리로 설정, 이 조건을 만족 하도록 공유기를 설치
첫 번째 집에 공유기를 설치 하고, 그 다음 mid 이상의 거리에 있는 집에 설치
이렇게 해서 설치한 공유기 개수가 c보다 크거나 같으면, 최소 거리를 더 크게 할 수 있음, 반대는 최소 거리를 줄여야 함
이진 탐색을 통해 최소 거리의 최대값을 갱신
'''
n, c = map(int, sys.stdin.readline().split())
houses = []
for i in range(n):
    houses += [int(input())]
houses.sort()

def cnt_install(houses, n, c, min_distance):
    cnt = 1  # 첫 번째 집에 하나 설치한다는 뜻, 이래야 최대한 많이 설치할 수 있음
    last_install = houses[0]  # 공유기 설치

    for i in range(1, n):
        if houses[i] - last_install >= min_distance:
            cnt += 1
            last_install = houses[i]  # 새로운 집에 공유기 설치

        if cnt >= c:
            return True
    return False


def find_min_distance(houses, n, c):
    start = 1
    end = houses[-1] - houses[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2

        if cnt_install(houses, n, c, mid):
            result = mid  # 가능한 최댓값 갱신
            start = mid + 1  # 더 큰 최소 거리를 시도
        else:
            end = mid - 1  # 더 작은 최소 거리를 시도

    return result

print(find_min_distance(houses, n, c))
