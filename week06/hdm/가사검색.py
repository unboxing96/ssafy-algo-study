import sys
sys.stdin = open('input.txt')

'https://school.programmers.co.kr/learn/courses/30/lessons/60060'

"""
??는 와일드카드. 어떤 문자든 될 수 있음.
# queries는 중복될 수도 있다.
1. queries를 for문 순회하며 맞는 words가 있나 체크필요.
1.1. queries의 ?를 만나는순간 queries의 남은 문자열의 개수를 파악하고, ?를 만난순간 len이 같으면됨.

"""

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value): # a에서 left value와 right value 사이 값을 가진 요소 개수를 반환 하기.
    right_index = bisect_right(a, right_value) # rightvalue 보다 큰 값이 나오는 첫번재 인덱스 반환
    left_index = bisect_left(a, left_value) # left value보다 크거나 같은 값이 나오는 첫번째 인덱스 반환
    return right_index - left_index # 범위에 속하는 값의 개수 구하기

array = [[] for _ in range(10001)] # 각 검색 키워드의 길이는 1 이상 10,000 이하
reversed_array = [[] for _ in range(10001)] #접두사에 와일드카드가 있는 패턴 처리하기 위함.

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word) # 각 단어를 가져와서 그 길이에따라 array와 reversed array에 저장. 사실상 여기가 핵심 1
        reversed_array[len(word)].append(word[::-1])
    for i in range(10001):
        array[i].sort() # 각 길이에 대한 정렬 수행 / 이진 탐색을 하기 위함임
        reversed_array[i].sort()
    for q in queries:
        if q[0] != '?': # 각 쿼리 q의 첫 요소가 ? 아니면(접두사에 와일드카드가 아니면) 여기가 핵심 2
            res = count_by_range(array[len(q)], q.replace("?", 'a'), q.replace('?', 'z'))
            # array 배열 마지막 요소에서,  ?를 사전적으로 가장 낮은 문자 a로 대체함. / right에는 사전적으로 가장 높은 문자 z로 대체함        """
            # 해당 과정에서, q.replace("?", 'a')는 heaa로,
            # q.replace('?', 'z')는 hezz로 변환되어, he로 시작하는 모든 단어가 검색 후

        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
            # 접두사가 와일드 카드니, 거꾸로 뒤집은 array의 마지막요소에서, 사전적으로 가장 낝은 문자a대체, 사전적으로 가장 높은 문자 z대체

        answer.append(res) # 쿼리에 대해 결과를 계산한 후 answer에 append시켜주기.

    return answer


# ------------------------------------------------------------------
# 성공한 솔루션이지만, 효율성 실패. (시간초과)
# ------------------------------------------------------------------
# def solution(words, queries):
#
#     # queries 중복제거
#     # new_queries = list(set(queries))
#     # print(new_queries)
#     answer = []
#     for q in queries: # 쿼리s 안에 요소 하나 뽑기.
#         count = 0
#         for word in words:
#             a = True
#             # 모든 queries를 순회하며 word와 비교해보기
#             if len(q) == len(word):
#                 for q_index in range(len(q)):
#                     # 만약 Q인덱스가 물음표이면
#                     if q[q_index] == '?': # 물음표이면 일단 다 패스하게 될 것임.
#                         continue
#                     elif q[q_index] != word[q_index]: # 둘이 같아도 설정 안했기에 패스, 같지 않으면 a= False 변경
#                         a = False
#                 if a is True:
#                     count += 1
#
#             else:  # 길이 다르면 다음것으로 넘어가봐.
#                 continue
#
#         answer.append(count)
#
#     return answer
#
# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# print(solution(words,queries))