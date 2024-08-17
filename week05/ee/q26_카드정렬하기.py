N = int(input())

nums = [int(input()) for _ in range(N)]
nums.sort() # 일단 정렬

ans = 0
while len(nums) > 1:
    temp = nums.pop(0) + nums.pop(0)    # 젤 작은 두 요소 더해주기
    ans += temp                         # 총 비교 횟수 업데이트

    # append 후 sort 했더니 시간초과
    # 삽입 정렬도 시간초과
    # 그래서 이진 탐색 후 insert로 ..

    left, right = 0, len(nums)
    while left < right:                 # left랑 right값이 같아질 때 까지
        mid = (left + right) // 2
        if nums[mid] < temp:
            left = mid + 1
        else:
            right = mid

    nums.insert(left, temp)

print(ans)