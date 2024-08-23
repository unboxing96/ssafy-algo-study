import sys
sys.stdin = open("2110_input.txt")

N, C = map(int, sys.stdin.readline().split()) # 집의 개수 N, 공유기 개수 C
houses = [int(sys.stdin.readline()) for _ in range(N)] # 집의 좌표

houses.sort()

# 한 집에는 공유기 하나만 설치할 수 있음
# 가장 인접한 두 공유기 사이의 거리를 최대로

def set_router(d):
    global C

    count = 1 # 맨 왼쪽 집에 공유기 설치해놓기
    temp = houses[0]

    for i in range(1, len(houses)):
        if houses[i] - temp >= d:
            count += 1 #공유기 설치
            temp = houses[i]
        if count >= C: #설치해야하는 공유기 다 설치했으면
            return True
    return False #공유기 설치 다 못함

left = 1
right = houses[-1] - houses[0]

ans = 0

while left <= right:
    mid = (left+right)//2
    if set_router(mid): #공유기 설치할 수 있으면
        left = mid + 1
        ans = mid
    else: #공유기 설치 못 하면
        right = mid -1 # 거리 좀 더 키우기

print(ans)