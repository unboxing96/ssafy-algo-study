#이분 탐색을 활용하는 경우에는 정확한 LIS가 아닌 LIS의 길이를 구할 때 사용

import sys
sys.stdin = open('12015_input.txt')


A = int(sys.stdin.readline()) #수열의 크기
arr = list(map(int, sys.stdin.readline().split()))

def binary_search(target, lis):
    left = 0
    right = len(lis)-1

    while left < right:
        mid = (left + right)//2
        if target > lis[mid]:
            left = mid + 1
        elif target == lis[mid]:
            return mid
        else:
            right = mid

    return left

lis = []
lis.append(arr[0])

for i in range(1, A):
    if arr[i] > lis[-1]: #lis의 마지막 원소보다 크면
        lis.append(arr[i]) #맨뒤에 추가
    else: #마지막 원소보다 작으면
        idx = binary_search(arr[i], lis)
        # lis.insert(idx, arr[i])
        lis[idx] = arr[i]

# print(lis)
print(len(lis))