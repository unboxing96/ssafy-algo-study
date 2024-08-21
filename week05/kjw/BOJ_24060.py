n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
a = -1      # 만약에 병합정렬이 일어나는 과정의 단계가 k보다 작다면 k 에 도달하지 못하므로 -1출력
def merge_sort(A, p, r):
    if p < r:
        q = (p+r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global cnt
    global a
    global k
    i = p
    j = q+1
    temp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1
    while i <= q:
        temp.append(A[i])
        i += 1
    while j <= r:
        temp.append(A[j])
        j += 1
    i = p
    t = 0
    while i <= r:
        A[i] = temp[t]
        cnt += 1
        if cnt == k:
            a = A[i]
            break
        i += 1
        t += 1
merge_sort(arr, 0, len(arr)-1)
print(a)
