n = int(input())
arr = list(map(int, input().split()))

# 시간복잡도 O(N^2)인 dp풀이
# dp = [1] * (n)
# for i in range(1, n):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j]+1)


# 시간복잡도 O(NlogN)의 이진탐색 풀이
def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while start < end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid-1] < target < lst[mid]:
            return mid
        elif target < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start

lst = [arr[0]]    # 최장수열 담을 리스트
for i in range(1, n):
    target = arr[i]
    if lst[-1] < target:    # 더 크면 그냥 담음 됨
        lst.append(target)
    else:
        idx = binary_search(lst, target)    # 작으면
        lst[idx] = target

print(len(lst))