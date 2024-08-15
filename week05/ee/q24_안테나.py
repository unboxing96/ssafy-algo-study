import sys
sys.stdin = open("q24_input.txt")

# 이게 왜 정렬이지?
N = int(input()) # 집의 수
houses = list(map(int, input().split())) # 집 위치

diff = []
for i in range(N):
    temp = []
    antenna = houses[i] # 안테나의 위치
    for house in houses:
        temp.append(abs(house - antenna))
    diff.append(sum(temp))
idx = 0
min_dis = diff[idx]
for j in range(1, N):
    if min_dis > diff[j]:
        min_dis = diff[j]
        idx = j
print(houses[idx])

