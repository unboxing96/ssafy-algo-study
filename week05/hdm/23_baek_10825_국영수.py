import sys
sys.stdin = open('input.txt')


"""
1. N명의 이름과 국어 영어 수학 점수 주어짐

아래 조건으로 정렬
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (아스키코드에서 대문자는 소문자보다 작으므로 사전 순 앞에옴)
5. 정렬한 순서에 따른 학생의 이름 출력
"""


# 학생 수
N = int(input())
student_score = [] # ['Junkyu', 50, 60, 100], ['Sangkeun', 80, 60, 50] ...

for i in range(N):
    name, korean, english, math = map(str, input().split())
    student_score.append([name,int(korean),int(english),int(math)])

# 국어가 감소하는 순서로, 영어가 증가하는 순서로, 수학이 감소하는 순서로, 점수가 같으면 사전순으로 sorted 활용해서 구현.
sorted_scores = sorted(student_score, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for row in range(len(sorted_scores)):
    print(sorted_scores[row][0])




#------------------------------------------------------------------------------------------------------------
# 정답이지만 시간초과
# for i in range(N):
#     name, korean, english, math = map(str, input().split())
#     student_score.append([name,int(korean),int(english),int(math)])
#
# # 1. 국어 점수가 감소하는 순서로
# korean_sorted = sorted(student_score, key = lambda x: x[1], reverse = True)
#
# def sort_kr_en(korean_sorted):
#     for k in range(len(korean_sorted)-1):
#         # 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
#         if korean_sorted[k][1] == korean_sorted[k+1][1]:
#             # 영어 점수가 증가하는 순서로
#             if korean_sorted[k][2] > korean_sorted[k+1][2]: # 만약 앞의 영어점수가 뒤에 영어점수보다 작다면
#                 korean_sorted[k], korean_sorted[k + 1] = korean_sorted[k + 1], korean_sorted[k] # 두개 자리바꾸기
#
#             # 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
#             if korean_sorted[k][2] == korean_sorted[k+1][2]: # 만약 국어점수와 영어점수가 같지 않다면,
#                 # 수학 점수가 감소하는 순서로
#                 if korean_sorted[k][3] < korean_sorted[k+1][3]: # 큰수가 앞에와야지
#                     korean_sorted[k], korean_sorted[k + 1] = korean_sorted[k + 1], korean_sorted[k]
#
#                 #모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (아스키코드에서 대문자는 소문자보다 작으므로 사전 순 앞에옴)
#                 if korean_sorted[k][3] == korean_sorted[k+1][3]:
#                     if ord(korean_sorted[k][0][0]) > ord(korean_sorted[k+1][0][0]):
#                         korean_sorted[k], korean_sorted[k + 1] = korean_sorted[k + 1], korean_sorted[k]
#
#
# for _ in range(len(korean_sorted)):
#     sort_kr_en(korean_sorted)
#
#
# for row in range(len(korean_sorted)):
#     print(korean_sorted[row][0])
