import sys

sys.stdin = open('input.txt')


# 아직 못품...
def solution(key, lock):
    answer = True
    return answer


# 90도를 회전하는 로직 필요함.
# key를 lock에 겹치는 모든 경우의 수를 순회하고 좌표의 합이 정확히 1이되는지 확인 필요.

# 90도 회전 알고리즘:
# for i in range(N):
#     for j in range(N):
#         arr[i][j] = arr[N-1-j][i]