import sys
# sys.stdin = open("24060_input.txt")

N, K = map(int,sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

def merge_sort(arr, p, r):
    if p < r:
        q = (p + r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(A, p, q, r)

def merge(arr, p, q, r):
    global K, count

    i, j = p, q+1

    temp = []
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= q:
        temp.append(arr[i])
        i += 1

    while j <= r:
        temp.append(arr[j])
        j += 1

    i = p
    t = 0
    while i <= r:
        arr[i] = temp[t]
        i += 1
        t += 1
        count += 1
        if count == K:
            print(arr[i-1])
            return

count = 0
merge_sort(A, 0, N-1)
if count < K:
    print(-1)
