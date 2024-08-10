# def solution(p):

#     answer = ''
#     return answer
# print(solution(input()))

def cor_string(data): # 올바른 문자열인지 계산하는 함수
    stack = []
    for i in range(len(data)):
        if stack:
            if data[i] == '(':
                stack.append(data[i])
            else:
                stack.pop()
        else:
            if data[i] == ')':
                return False
            else:
                stack.append(data[i])
    if not stack:
        return True
    
def solution(p):
    if not p:   # 빈 문자열 들어오면 빈거 반환
        return ''
    
    for i in range(2, len(p)+1, 2): # u,v로 나누기
        u = p[:i]
        v = p[i:]
        if u.count('(') == u.count(')'):
            break
    
    if cor_string(u):
        return u + solution(v)  # v를 재귀호출
    else:
        result = '('
        result += solution(v)
        result += ')'
        u = u[1:-1]
        u = ''.join(')' if q == '(' else '(' for q in u) # 이부분 검색함..
        result += u
        return result
