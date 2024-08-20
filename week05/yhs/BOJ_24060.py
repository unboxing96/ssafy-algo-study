def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = int(len(lst) / 2 + 0.5)   # 문제에서 요구하는 중간 : 홀수번째면 반올림한 값
    left = lst[:mid]
    right = lst[mid:]

    merged_left = merge_sort(left)  # 중간 기준 왼쪽 배열 정렬하기
    # if not merged_left:
    #     return
    merged_right = merge_sort(right)    # 중간 기준 오른쪽 배열 정렬하기
    # if not merged_right:
    #     return
    merged = merge(merged_left, merged_right)   # 양쪽 병합 후 정렬
    # if not merged:
    #     return

    return merged


def merge(left, right):
    global k

    i, j = 0, 0
    tmp = []

    # 정렬된 left와 right 비교해서 작은 수부터 담기 (k번째 추가된 수 출력)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            k -= 1
            if not k:
                print(left[i])
                return
            i += 1
        else:
            tmp.append(right[j])
            k -= 1
            if not k:
                print(right[j])
                return
            j += 1

    # 남은 배열의 수 모두 담기
    while i < len(left):
        tmp.append(left[i])
        k -= 1
        if not k:
            print(left[i])
            return
        i += 1
    while j < len(right):
        tmp.append(right[j])
        k -= 1
        if not k:
            print(right[j])
            return
        j += 1

    return tmp


n, k = map(int, input().split())
A = list(map(int, input().split()))

A = merge_sort(A)   # 병합정렬 시작
if k > 0:           # 만약 k가 저장횟수보다 작으면 -1 출력
    print(-1)