import sys
sys.stdin = open('input.txt')

N, C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)]) # [1, 2, 4, 8, 9]

max_distance = house[-1] - house[0]
d = 1
# d를 1부터 1씩 증가하면서 c만큼 진행해보기
result=0

while d <= max_distance :
    mid = (d + max_distance) // 2
    value = house[0]
    count = 1
    for i in range(1, N):
        if house[i] >= value + mid:
            value = house[i]
            count +=1
    if count >= C:
        d = mid +1
        result = mid
    else:
        max_distance = mid -1
print(result)





#------------------------------------------------

# X
# need = N // (C-1)
#
# result = house[need] - house[0]
#
# print(result)