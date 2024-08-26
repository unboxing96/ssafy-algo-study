import sys
sys.stdin = open("04_12015_가장긴증가하는부분수열2.txt")

# 문제 분석
# 이진 탐색으로 최적화한 LIS를 구한다.

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        # 현재 위치가 target보다 크면 -> target을 더 작은 위치와 비교해야 함.
        # 왼쪽 경곗값을 찾는 것이 목표이므로.
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return start


n = int(input())
arr = list(map(int, input().split()))
LIS = [arr[0]]

for i in range(1, n):
    if LIS[-1] < arr[i]:
        LIS.append(arr[i])
    else:
        idx = binary_search(LIS, arr[i])
        LIS[idx] = arr[i]

print(len(LIS))