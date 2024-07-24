import sys

sys.stdin = open('index.txt')


# 첫줄의 동전들로 만들 수 없는 양의 점수 금액 최솟값을 구하시오.

# 작은수로 list세우기. 1 1 2 3 9

N = int(input())
M = list(map(int,input().split()))

M.sort()
print(M)
target = 1 # target -1까지 가능 한지 check

# 숫자의 1, 1, 2, 3, 9가 존재
# 1이 가능한지 check 1가능.
# 1 + 1 = 2 가능한지 check
# targer 1에 + 다음숫자 1 더하면가능. = 2 업데이트.
# 2가 가능한지 여부 체크. 다음숫자 2가있으면 가능. = 4업데이트
# 4이 가능한지 여부 체크 다음숫자 3이기에 7까지 가능. = 7업데이트
# 1 1 2 3 = 7까지 가능
# 1 1 2 3 9 = 16 이니 15까지 가능. 이런 순서.

for x in M :
    #만들 수 없는 금액 찾으면 종료
    if target < x:
        break
    target += x

print(target)


