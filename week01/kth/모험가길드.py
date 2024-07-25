import sys
sys.stdin = open("모험가길드.txt", "r")

# 문제 분석
# 공포도 X인 모험가는 반드시 X명 이상으로 구성한 그룹에 참여해야 한다.

# 접근
# 직관적으로 생각했을 때는, 공포도가 큰 순서대로 그룹을 구성하는 것이 옳다.
# 오름차순으로 배열을 정리한다.
# result = 0
# while 배열:
    # 끝 값(가장 큰 값)을 pop()하여, tmp_group에 append 한다.
    # tmp_group의 가장 큰 값을 갱신한다. tmp_group_max_num
    # if len(tmp_group) == tmp_group_max_num:
        # result += 1
        # tmp_group = [] # 초기화
        # tmp_group_max_num = 0 # 초기화

# 틀린 풀이
# n = int(input())
# arr = list(map(int, input().split()))

# arr.sort()

# result = 0
# tmp_group = []
# tmp_group_max_num = 0

# while arr:
#     tmp = arr.pop()
#     tmp_group.append(tmp)
#     tmp_group_max_num = max(tmp_group)

#     if len(tmp_group) == tmp_group_max_num:
#         result += 1
#         tmp_group = []
#         tmp_group_max_num = 0

# print(result)

def solution(n, arr):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    result = 0
    count = 0

    for elem in arr:
        count += 1

        if count >= elem:
            result += 1
            count = 0

    return result

n = 7
arr = [6, 1, 1, 1, 2, 2, 3]
result = solution(n, arr)
print(result)

[1, 1, 1, 2, 2, 3, 6]
