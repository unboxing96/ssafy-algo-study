import sys
import bisect
sys.stdin = open('input.txt')


"수열 A가 주어졌을때 가장 긴 증가하는 부분 수열을 구하는 프로그램작성"
"가장 긴 증가 부분 수열?"

def length_of_lis(sequence, N):
    dp = [1] * N

    for i in range(1, N):
        for j in range(N): # 0번째 인덱스부터 체크
            if sequence[j] < sequence[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


N = int(input())
sequence = list(map(int, input().split()))

print(length_of_lis(sequence, N))



# ----------------------------------------------------
# bisect 사용x
# def length_of_lis(sequence):
#     lis = [] # 개수체크할 리스트 선언
#
#     for num in sequence: # sequence다 체크하기.
#         pos = bisect.bisect_left(lis, num) # lis에서 num이 들어갈 위치를 체크
#
#         if pos == len(lis): # pos와 lis의 길이가 같으면 마지막에 숫자 넣으면됨.
#             lis.append(num) # pos는 인덱스 요소이기 때문
#         else:
#             lis[pos] = num # num이 들어갈 위치에 lis를 넣어주기.
#             # 중복은 추가되지 않고 해당 값으로 교체되는 중임.
#             # ex) [10, 10, 20]
#             # bisect.bisect_left(lis,10) = 0반환되어 lis = [10]
#             # 두번째 bisect_left(lis,10)도 0이 반환되어 lis = [10]
#             # 이후 20이 적용되면 bisect_left(lis, 20) =1이 반환되어서 lis = [10,20]
#             # 결과적으로 최대값이 나오게됨.
#
#     return len(lis) # 길이 출력해주면 가장 긴 증가하는 부분 수열 길이 나옴