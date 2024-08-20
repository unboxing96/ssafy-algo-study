import sys
sys.stdin = open('input.txt')

"""
배열 a를 오름차순 정렬 > 배열 a에 k번째 저장되는 수를 구하시오
배열 A에 k 번째 저장되는 수를 출력하시오. 저장 횟수가 k보다 작으면 -1 출력.
"""
def merge_sort(A,p,r):
    if p < r:
        q = (p+r) // 2 #$ 중간지점 계산
        merge_sort(A,p,q) # 앞부분 정렬
        merge_sort(A,q+1,r) # 뒷부분 정렬
        merge(A,p,q,r) # 병합 진행


def merge(A,p,q,r):
    global count, result, K
    i = p # 왼쪽부분 인덱스
    j = q+1 # 오른쪽 부분 배열의 첫 인덱스
    t = 0
    temp_arr = [0] * (r-p+1) # 임시 배열 생성

    while i<=q and j <=r: # 왼쪽과 오른쪽 부분 배열에 모두 비교할 요소가 남아 있는 동안 반복 진행
        if A[i] <= A[j]: # 왼쪽 배열의 현재요소가 오른쪽 배열 요소보다 작거나 같으면
            temp_arr[t] = A[i] #왼쪽 배열의 현재 요소를 temp#arr에 저장
            i += 1 # 왼쪽 인덱스 이동
        else:
            temp_arr[t] = A[j] # 오른쪽 배열의 현재 요소 temp에 저장
            j +=1 # 오른쪽 배열 j 이동
        t += 1  # temp 인덱스 다음위치 탐색

    while i <= q: #왼쪽 배열에 남은 요소가 있을 경우
        temp_arr[t] = A[i] # 남은 왼쪽 배열 요소 temp 저장
        i += 1 # 왼쪽 배열 인덱스 이동
        t += 1 # tmp 배열 인덱스 이동
    while j <= r : # 오른쪽 배열도 체크
        temp_arr[t] = A[j]
        j += 1
        t += 1
    for i in range(p,r+1): # p에서 r까지의 인덱스를 복사해서 넣기
        A[i] = temp_arr[i-p] #temp_arr의 병합된 결과를 A에 넣기
        count += 1
        if count == K:
            result = A[i]

N, K = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
result = -1
merge_sort(arr, 0, N-1)

print(result)



''' 의사코드 그대로 구현
merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
    if (p < r) then {
        q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
        merge_sort(A, p, q);      # 전반부 정렬
        merge_sort(A, q + 1, r);  # 후반부 정렬
        merge(A, p, q, r);        # 병합
    }
}

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
merge(A[], p, q, r) {
    i <- p; j <- q + 1; t <- 1;
    while (i ≤ q and j ≤ r) {
        if (A[i] ≤ A[j])
        then tmp[t++] <- A[i++]; # tmp[t] <- A[i]; t++; i++;
        else tmp[t++] <- A[j++]; # tmp[t] <- A[j]; t++; j++;
    }
    while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
        tmp[t++] <- A[i++];
    while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
        tmp[t++] <- A[j++];
    i <- p; t <- 1;
    while (i ≤ r)  # 결과를 A[p..r]에 저장
        A[i++] <- tmp[t++]; 
'''
