import sys
sys.stdin = open("01_2110_공유기설치.txt")

# 문제 분석
# 공유기 사이의 거리 m을 이분탐색의 target으로 하자.
# start를 최소 거리 1 (집은 최소 1의 간격을 두고 있으므로)
# end를 max(arr) - min(arr)
# c개를 만족하는 mid의 최대값을 return
    # c개보다 크면, 범위가 너무 좁다. mid를 늘린다. start = mid + 1
        # c개 이상이므로, 정답은 갱신한다.
    # c개보다 작으면, 범위가 너무 넓다, mid를 줄인다. end = mid - 1

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start = 1
end = arr[-1] - arr[0]

while start <= end:
    mid = (start + end) // 2
    cur_loc = arr[0] # 공유기를 설치하는 위치.
    cnt = 1 # 이번 mid에 대하여 cnt를 센다.

    for i in range(1, n):
        next_loc = arr[i]
        if next_loc - cur_loc >= mid: # 간격이 mid 이상이면
            cnt += 1 # 설치한다.
            cur_loc = next_loc # 현재 위치에서 다음 위치로 이동한다.
        
    if cnt >= c:
        start = mid + 1
    else:
        end = mid - 1

print(end)