# 백준 12015번 가장 긴 증가하는 부분 수열 2
# 수열을 순회하며 lis 배열의 마지막 원소보다 큰 원소일 경우 lis에 추가
# 아닐 경우 이진탐색을 통해 수열의 원소보다 작은 lis의 원소 중 최대값의 자리에 갱신 (길이만 구하면 된다)

def binary_search(arr, target):
    s, e = 0, len(arr) - 1

    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            s = mid + 1
        else:
            e = mid - 1

    return s


n = int(input())
nums = list(map(int, input().split()))
lis = [nums[0]]

for num in nums:
    if num > lis[-1]:
        lis.append(num)
    else:
        idx = binary_search(lis, num)
        lis[idx] = num

print(len(lis))