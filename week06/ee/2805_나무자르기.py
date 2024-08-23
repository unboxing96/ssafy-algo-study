# 나무자르기

import sys
sys.stdin = open("2805_input.txt")

N, M = map(int, sys.stdin.readline().split()) #나무의 수 N, 가져가려는 나무 길이 M
trees = list(map(int, sys.stdin.readline().split())) #나무의 높이

#절단기의 높이 H를 구하기
#H를 찾는 이분탐색?

trees.sort() #정렬이 되어 있어야 함

def cut_trees(H):
    result = 0 #절단된 나무 총 길이
    for tree in trees:
        if tree > H:
            result += tree-H
    return result

#H의 범위: 0~ 나무의 최댓값
left = 0
right = trees[-1]

ans = 0
pre = 0

while left < right:

    mid = (left+right)//2

    if cut_trees(mid) == M:
        ans = mid
        break
    elif cut_trees(mid) > M:
        left = mid+1
        pre = mid # M보다 더 많이 잘랐을 때의 절단기의 높이를 예비로 저장해두기
    else:
        right = mid
else:
    # "적어도 M 미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값"
    # 정확하게 딱 떨어지는 게 없다면? 더 많이 잘라도 됨
    ans = pre

print(ans)