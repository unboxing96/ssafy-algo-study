# 김태현
# 정답!
def merge_sort(arr):
    def sort(low, high):
        if high - low <= 1:
            return
        
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
    
    def merge(low, mid, high):
        l = low
        h = mid
        tmp = []

        while l < mid and h < high:
            if arr[l] < arr[h]:
                tmp.append(arr[l])
                l += 1
            else:
                tmp.append(arr[h])
                h += 1

        while l < mid:
            tmp.append(arr[l])
            l += 1
        
        while h < high:
            tmp.append(arr[h])
            h += 1
    
        for i in range(low, high):
            arr[i] = tmp[i - low]

    sort(0, len(arr))
    return arr


# 이다이
# 오답!
def quick_sort(arr):
    if len(arr) <= 1:
        return 
    
    pivot = arr[0]
    tail = arr[1:]
    
    leftside = [x for x in tail if x >= pivot]
    rightside = [x for x in tail if x < pivot]

    return quick_sort(leftside) + [pivot] + quick_sort(rightside)


# 한동민
# 오답!
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = arr[len(arr) // 2]
    left = merge_sort(arr[mid:])
    right = merge_sort(arr[:mid])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.append(left[i:])
    result.append(right[j:])
    return result

# 김정우
# 정답!
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    return merge(left_arr, right_arr)

def merge(left, right):
    i = j = 0
    merge_array = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merge_array.append(left[i])
            i += 1
        else:
            merge_array.append(right[j])
            j += 1
            
    merge_array += left[i:]
    merge_array += right[j:]
    return merge_array


# 여현승
# 오답!
def quick_sort(arr):
    pivot = arr[0]
    left = 1
    right = len(arr) - 1

    while left < right:
        for i in range(left, len(arr)):
            if arr[i] < pivot:
                left = i
                break
        for i in range(right, pivot - 1):
            if arr[i] > pivot:
                right = i
                break
        
        arr[left], arr[right] = arr[right], arr[left]
        arr[left], arr[pivot] = arr[pivot], arr[left]

    quick_sort(arr[:pivot])
    quick_sort(arr[pivot:])


# 테스트
def test_merge_sort():
    test_cases = [
        ([38, 27, 43, 3, 9, 82, 10], [3, 9, 10, 27, 38, 43, 82]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 3, 1, 2, 3], [1, 1, 2, 2, 3, 3, 3]),
        ([], []),
        ([1], [1]),
        ([0, -1, -2, -3, 4, 3, 2, 1], [-3, -2, -1, 0, 1, 2, 3, 4]),
        ([100, 23, 45, 67, 89, 1, 0, 2], [0, 1, 2, 23, 45, 67, 89, 100]),
        ([8, 5, 9, 1, 3, 6, 7, 2, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2])
    ]

    for i, (input_arr, expected) in enumerate(test_cases):
        result = merge_sort(input_arr[:])  # merge_sort인 경우
        # result = quick_sort(input_arr[:])  # quick_sort인 경우
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# 테스트 실행
test_merge_sort()