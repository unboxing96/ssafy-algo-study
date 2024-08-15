import sys
sys.stdin = open('input.txt')

"""
짝이 맞지 않은 형태의 괄호로 오류가 발생.
모든 괄회를 뽑아서 올바른 순서로 배치후 문자열 알려주세요.
"""


# (와 )로 이루어진 문자열의 경우 (의 개수와 )가 같다면 균형잡힌
# () 짝이 다맞으면 올바른 문자열
p = input()


def balance_index(p):
    count = 0  # 왼쪽 괄호 '(' 의 개수를 세는 변수
    for i in range(len(p)):  # 문자열 p의 각 문자를 확인하면서
        if p[i] == '(':  # '(' 이면 count를 1 증가
            count += 1
        else:  # ')' 이면 count를 1 감소
            count -= 1
        if count == 0:  # count가 0이 되면, 이는 균형잡힌 상태를 의미
            return i  # 이때의 인덱스를 반환 (u와 v를 나누는 지점)


def check_proper(p):
    count = 0  # 왼쪽 괄호 '(' 의 개수를 세는 변수
    for i in p:  # 문자열 p의 각 문자를 확인하면서
        if i == '(':  # '(' 이면 count를 1 증가
            count += 1
        else:  # ')' 이면
            if count == 0:  # 만약 count가 0이라면 이는 잘못된 짝을 의미
                return False  # 올바르지 않은 문자열임을 반환
            count -= 1  # 올바른 짝이라면 count를 1 감소
    return True  # 모두 통과하면 올바른 괄호 문자열이므로 True 반환


def solution(p):
    if p == '':  # 1. 입력이 빈 문자열이면, 빈 문자열을 반환
        return ''

    index = balance_index(p)  # 2. 문자열 p를 두 균형잡힌 부분 u와 v로 분리
    u = p[:index + 1]  # 문자열의 앞부분을 u로 지정
    v = p[index + 1:]  # 나머지 뒷부분을 v로 지정

    if check_proper(u):  # 3. u가 올바른 괄호 문자열인 경우
        return u + solution(v)  # v에 대해 solution 함수를 재귀적으로 호출한 결과를 u 뒤에 붙여 반환
    else:  # 4. u가 올바른 괄호 문자열이 아닌 경우
        answer = '(' + solution(v) + ')'  # 새로운 문자열로 '(' + v를 재귀적으로 처리한 결과 + ')' 를 생성
        u = u[1:-1]  # u의 첫 번째와 마지막 문자를 제거
        u = ''.join([')' if ch == '(' else '(' for ch in u])  # 나머지 u의 괄호를 뒤집기 ( '(' -> ')', ')' -> '(' )
        answer += u  # 뒤집어진 u를 answer에 붙임
        return answer  # 최종 결과 문자열을 반환



# ------------------------------------------------------------
    # if len(p) == 0: # 빈 문자열인 경우 빈 문자열 반환환
    #    return ""
    #
    # # 짝을 맞춰가면서 u,v랑 분류.
    # # 전체 p만큼 일단 돌아
    # stack = []
    # result = [] #올바른 괄호 문자열
    # u = []
    # v = []
    # for i in range(len(p) - 1): #u,v 분류할거야. 균형잡힌 문자열을 뽑을거야.
    #     count = 0
    #     if p[i] == ')' and p[i+1] == '(':
    #         u.append(p[i])
    #         u.append(p[i+1])
    #         v = p[i+2:] # 나머지 p에 슬라이싱하면됨.
    #         break
    #     elif p[i] == '(' and p[i+1] == ')': # 올바른 괄호 문자열
    #         result.append(p[i])
    #         result.append(p[i+1])
    #     elif p[i] == ')' and p[i+1] == ')':
    #         count +=1
    #         stack.append(p[i+1])
    #         continue
    #     elif

    # 첫째로, 올바른 문자열인지 체크가능해야함.
#     # stack으로 확인가능함.
#
#     for i in range(len(p)-1):
#         stack.append(p(i+1))
#         if stack.pop() == '(' and p[i] == ')': #만약 직전 것이 (이고, i가 )라면,
#             result.append('(')
#             result.append(p[i])
#         elif stack.pop() == ')' and p[i] == ')': # 만약 둘다 닫는 괄호라면 스택에 다시쌓아주기
#             stack.append(')')
#             stack.append(')')
#
#
# solution(p)
#

